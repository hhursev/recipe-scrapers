# IF things in this file continue get messy (I'd say 300+ lines) it may be time to
# find a package that parses https://schema.org/Recipe properly (or create one ourselves).


import extruct

from recipe_scrapers.settings import settings

from ._exceptions import SchemaOrgException
from ._utils import get_minutes, get_yields, normalize_string

SCHEMA_ORG_HOST = "schema.org"
SCHEMA_NAMES = ["Recipe", "WebPage"]

SYNTAXES = ["json-ld", "microdata"]


class SchemaOrg:
    def __init__(self, page_data, raw=False):
        if raw:
            self.format = "raw"
            self.data = page_data
            return
        self.format = None
        self.data = {}

        data = extruct.extract(
            page_data,
            syntaxes=SYNTAXES,
            errors="log" if settings.LOG_LEVEL <= 10 else "ignore",
            uniform=True,
        )

        low_schema = {s.lower() for s in SCHEMA_NAMES}
        for syntax in SYNTAXES:
            # make sure entries of type Recipe are always parsed first
            syntax_data = data.get(syntax, [])
            try:
                index = [x.get("@type", "") for x in syntax_data].index("Recipe")
                syntax_data.insert(0, syntax_data.pop(index))
            except ValueError:
                pass

            for item in syntax_data:
                in_context = SCHEMA_ORG_HOST in item.get("@context", "")
                item_type = item.get("@type", "")
                if isinstance(item_type, list):
                    for type in item_type:
                        if type.lower() in low_schema:
                            item_type = type.lower()
                if in_context and item_type.lower() in low_schema:
                    self.format = syntax
                    self.data = item
                    if item_type.lower() == "webpage":
                        self.data = self.data.get("mainEntity")
                    return
                elif in_context and "@graph" in item:
                    for graph_item in item.get("@graph", ""):
                        graph_item_type = graph_item.get("@type", "")
                        if not isinstance(graph_item_type, str):
                            continue
                        if graph_item_type.lower() in low_schema:
                            in_graph = SCHEMA_ORG_HOST in graph_item.get("@context", "")
                            self.format = syntax
                            if graph_item_type.lower() == "webpage" and in_graph:
                                self.data = self.data.get("mainEntity")
                                return
                            elif graph_item_type.lower() == "recipe":
                                self.data = graph_item
                                return

    def language(self):
        return self.data.get("inLanguage") or self.data.get("language")

    def title(self):
        return normalize_string(self.data.get("name"))

    def category(self):
        category = self.data.get("recipeCategory")
        if isinstance(category, list):
            return ",".join(category)
        return category

    def author(self):
        author = self.data.get("author")
        if (
            author
            and isinstance(author, list)
            and len(author) >= 1
            and isinstance(author[0], dict)
        ):
            author = author[0]
        if author and isinstance(author, dict):
            author = author.get("name")
        return author

    def total_time(self):
        if not (self.data.keys() & {"totalTime", "prepTime", "cookTime"}):
            raise SchemaOrgException("Cooking time information not found in SchemaOrg")

        def get_key_and_minutes(k):
            source = self.data.get(k)
            # Workaround: strictly speaking schema.org does not provide for minValue (and maxValue) properties on objects of type Duration; they are however present on objects with type QuantitativeValue
            # Refs:
            #  - https://schema.org/Duration
            #  - https://schema.org/QuantitativeValue
            if type(source) == dict and "minValue" in source:
                source = source["minValue"]
            return get_minutes(source, return_zero_on_not_found=True)

        total_time = get_key_and_minutes("totalTime")
        if not total_time:
            times = list(map(get_key_and_minutes, ["prepTime", "cookTime"]))
            total_time = sum(times)
        return total_time

    def cook_time(self):
        if not (self.data.keys() & {"cookTime"}):
            raise SchemaOrgException("Cooktime information not found in SchemaOrg")
        return get_minutes(self.data.get("cookTime"), return_zero_on_not_found=True)

    def prep_time(self):
        if not (self.data.keys() & {"prepTime"}):
            raise SchemaOrgException("Preptime information not found in SchemaOrg")
        return get_minutes(self.data.get("prepTime"), return_zero_on_not_found=True)

    def yields(self):
        yield_data = self.data.get("recipeYield") or self.data.get("yield")
        if yield_data and isinstance(yield_data, list):
            yield_data = yield_data[0]
        recipe_yield = str(yield_data)
        return get_yields(recipe_yield)

    def image(self):
        image = self.data.get("image")

        if image is None:
            raise SchemaOrgException("Image not found in SchemaOrg")

        if isinstance(image, list):
            # Could contain a dict
            image = image[0]

        if isinstance(image, dict):
            image = image.get("url")

        if "http://" not in image and "https://" not in image:
            # some sites give image path relative to the domain
            # in cases like this handle image url with class methods or og link
            image = ""

        return image

    def ingredients(self):
        ingredients = (
            self.data.get("recipeIngredient") or self.data.get("ingredients") or []
        )
        return [
            normalize_string(ingredient) for ingredient in ingredients if ingredient
        ]

    def nutrients(self):
        nutrients = self.data.get("nutrition", {})

        # Some recipes contain null or numbers which breaks normalize_string()
        # We'll ignore null and convert numbers to a string, like Schema validator does
        for key, val in nutrients.copy().items():
            if val is None:
                del nutrients[key]
            elif type(val) in [int, float]:
                nutrients[key] = str(val)

        return {
            normalize_string(nutrient): normalize_string(value)
            for nutrient, value in nutrients.items()
            if nutrient != "@type" and value is not None
        }

    def _extract_howto_instructions_text(self, schema_item):
        instructions_gist = []
        if type(schema_item) is str:
            instructions_gist.append(schema_item)
        elif schema_item.get("@type") == "HowToStep":
            if schema_item.get("name", False):
                # some sites have duplicated name and text properties (1:1)
                # others have name same as text but truncated to X chars.
                # ignore name in these cases and add the name value only if it's different from the text
                if not schema_item.get("text").startswith(
                    schema_item.get("name").rstrip(".")
                ):
                    instructions_gist.append(schema_item.get("name"))
            instructions_gist.append(schema_item.get("text"))
        elif schema_item.get("@type") == "HowToSection":
            instructions_gist.append(schema_item.get("name") or schema_item.get("Name"))
            for item in schema_item.get("itemListElement"):
                instructions_gist += self._extract_howto_instructions_text(item)
        return instructions_gist

    def instructions(self):
        instructions = self.data.get("recipeInstructions") or ""

        if isinstance(instructions, list):
            instructions_gist = []
            for schema_instruction_item in instructions:
                instructions_gist += self._extract_howto_instructions_text(
                    schema_instruction_item
                )

            return "\n".join(
                normalize_string(instruction) for instruction in instructions_gist
            )

        return instructions

    def ratings(self):
        ratings = self.data.get("aggregateRating")
        if ratings is None:
            raise SchemaOrgException("No ratings data in SchemaOrg.")

        if isinstance(ratings, dict):
            ratings = ratings.get("ratingValue")

        if ratings is None:
            raise SchemaOrgException("No ratingValue in SchemaOrg.")

        return round(float(ratings), 2)

    def cuisine(self):
        cuisine = self.data.get("recipeCuisine")
        if cuisine is None:
            raise SchemaOrgException("No cuisine data in SchemaOrg.")
        elif isinstance(cuisine, list):
            return ",".join(cuisine)
        return cuisine

    def description(self):
        description = self.data.get("description")
        if description is None:
            raise SchemaOrgException("No description data in SchemaOrg.")
        return normalize_string(description)
