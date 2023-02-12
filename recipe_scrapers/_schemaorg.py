# mypy: disallow_untyped_defs=False
# IF things in this file continue get messy (I'd say 300+ lines) it may be time to
# find a package that parses https://schema.org/Recipe properly (or create one ourselves).


from itertools import chain

import extruct

from recipe_scrapers.settings import settings

from ._exceptions import SchemaOrgException
from ._utils import get_minutes, get_yields, normalize_ingredients, normalize_string

SCHEMA_ORG_HOST = "schema.org"

SYNTAXES = ["json-ld", "microdata"]


class SchemaOrg:
    @staticmethod
    def _contains_schematype(item, schematype):
        itemtype = item.get("@type", "")
        itemtypes = itemtype if isinstance(itemtype, list) else [itemtype]
        return schematype.lower() in "\n".join(itemtypes).lower()

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

        for syntax in SYNTAXES:
            # make sure entries of type Recipe are always parsed first
            syntax_data = data.get(syntax, [])
            try:
                index = [x.get("@type", "") for x in syntax_data].index("Recipe")
                syntax_data.insert(0, syntax_data.pop(index))
            except ValueError:
                pass

            for item in syntax_data:
                if SCHEMA_ORG_HOST not in item.get("@context", ""):
                    continue

                # If the item itself is a recipe, then use it directly as our datasource
                if self._contains_schematype(item, "Recipe"):
                    self.format = syntax
                    self.data = item
                    return

                # Check for recipe items within the item's entity graph
                for graph_item in item.get("@graph", []):
                    if self._contains_schematype(graph_item, "Recipe"):
                        self.format = syntax
                        self.data = graph_item
                        return

                # If the item is a webpage and describes a recipe entity, use the entity as our datasource
                if self._contains_schematype(item, "WebPage"):
                    main_entity = item.get("mainEntity", {})
                    if self._contains_schematype(main_entity, "Recipe"):
                        self.format = syntax
                        self.data = main_entity
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
        author = self.data.get("author") or self.data.get("Author")
        if (
            author
            and isinstance(author, list)
            and len(author) >= 1
            and isinstance(author[0], dict)
        ):
            author = author[0]
        if author and isinstance(author, dict):
            author = author.get("name")
        if author:
            return author.strip()

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
        if not (self.data.keys() & {"recipeYield", "yield"}):
            raise SchemaOrgException("Servings information not found in SchemaOrg")
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

        if ingredients and isinstance(ingredients[0], list):
            ingredients = list(chain(*ingredients))  # flatten

        return normalize_ingredients(ingredients)

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
            name = schema_item.get("name") or schema_item.get("Name")
            if name is not None:
                instructions_gist.append(name)
            for item in schema_item.get("itemListElement"):
                instructions_gist += self._extract_howto_instructions_text(item)
        return instructions_gist

    def instructions(self):
        instructions = self.data.get("recipeInstructions") or ""

        if instructions and isinstance(instructions[0], list):
            instructions = list(chain(*instructions))  # flatten

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
        if description and isinstance(description, list):
            description = description[0]
        return normalize_string(description)
