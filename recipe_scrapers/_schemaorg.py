# IF things in this file continue get messy (I'd say 300+ lines) it may be time to
# find a package that parses https://schema.org/Recipe properly (or create one ourselves).
import extruct
from ._utils import get_minutes, normalize_string

SCHEMA_ORG_HOST = "schema.org"
SCHEMA_NAMES = ["Recipe", "WebPage"]

SYNTAXES = ["json-ld", "microdata"]


class SchemaOrgException(Exception):
    def __init__(self, message):
        super().__init__(message)


class SchemaOrg:
    def __init__(self, page_data):
        self.format = None
        self.data = {}

        data = extruct.extract(page_data, syntaxes=SYNTAXES, uniform=True)

        for syntax in SYNTAXES:
            for item in data.get(syntax, []):
                in_context = SCHEMA_ORG_HOST in item.get("@context", "")
                low_schema = [s.lower() for s in SCHEMA_NAMES]
                if in_context and item.get("@type", "").lower() in low_schema:
                    self.format = syntax
                    self.data = item
                    if item.get("@type").lower() == "webpage":
                        self.data = self.data.get("mainEntity")
                    return
                elif in_context and "@graph" in item:
                    for graph_item in item.get("@graph", ""):
                        in_graph = SCHEMA_ORG_HOST in graph_item.get("@context", "")
                        if (
                            in_graph
                            and graph_item.get("@type", "").lower() in low_schema
                        ):
                            self.format = syntax
                            self.data = graph_item
                            if graph_item.get("@type").lower() == "webpage":
                                self.data = self.data.get("mainEntity")
                            return

    def language(self):
        return self.data.get("inLanguage") or self.data.get("language")

    def title(self):
        return normalize_string(self.data.get("name"))

    def author(self):
        author = self.data.get("author")
        if author is not None:
            if type(author) == str:
                return author
            return author.get("name")

    def total_time(self):
        total_time = get_minutes(self.data.get("totalTime"))
        if not total_time:
            prep_time = get_minutes(self.data.get("prepTime")) or 0
            cook_time = get_minutes(self.data.get("cookTime")) or 0
            total_time = prep_time + cook_time
        return total_time

    def yields(self):
        yield_data = self.data.get("recipeYield")
        if isinstance(yield_data, list) and len(yield_data) > 0:
            recipe_yield = str(yield_data[0])
        else:
            recipe_yield = str(yield_data)
        if len(recipe_yield) <= 3:  # probably just a number. append "servings"
            return recipe_yield + " serving(s)"

        if "\n" in recipe_yield:
            recipe_yield = recipe_yield.split("\n")[-1]

        return recipe_yield

    def image(self):
        image = self.data.get("image")

        if image is None:
            raise SchemaOrgException("Image not found in SchemaOrg")

        if type(image) == dict:
            return image.get("url")
        elif type(image) == list:
            if type(image[0]) == dict:
                return image[0].get("url")
            return image[0]

        if "http://" not in image and "https://" not in image:
            # some sites give image path relative to the domain
            # in cases like this handle image url with class methods or og link
            return ""

        return image

    def ingredients(self):
        ingredients = (
            self.data.get("recipeIngredient") or self.data.get("ingredients") or []
        )
        return [
            normalize_string(ingredient) for ingredient in ingredients if ingredient
        ]

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
            instructions_gist.append(schema_item.get("name"))
            for item in schema_item.get("itemListElement"):
                instructions_gist += self._extract_howto_instructions_text(item)
        return instructions_gist

    def instructions(self):
        instructions = self.data.get("recipeInstructions") or ""

        if type(instructions) is list:
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
        ratings = self.data.get("aggregateRating", None)
        if ratings is None:
            raise SchemaOrgException("No ratings data in SchemaOrg.")

        if type(ratings) == dict:
            return round(float(ratings.get("ratingValue")), 2)
        return round(float(ratings), 2)

    def cuisine(self):
        cuisine = self.data.get("recipeCuisine")
        if isinstance(cuisine, list):
            return ",".join(cuisine)
        return cuisine
