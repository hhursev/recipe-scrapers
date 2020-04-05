import extruct
from ._utils import get_minutes, normalize_string

SCHEMA_ORG_HOST = "schema.org"
SCHEMA_NAME = "Recipe"
SCHEMA_URL = "https://" + SCHEMA_ORG_HOST + "/" + SCHEMA_NAME

SYNTAXES = ["microdata", "json-ld"]


class SchemaOrgException(Exception):
    def __init__(self, message):
        super().__init__(message)


class SchemaOrg:

    def __init__(self, url, page_data):
        self.format = None
        self.data = {}

        data = extruct.extract(
            page_data,
            syntaxes=SYNTAXES,
            uniform=True,
        )

        for syntax in SYNTAXES:
            for item in data.get(syntax, []):
                if (
                    SCHEMA_ORG_HOST in item.get("@context", "") and
                    item.get("@type", "").lower() == SCHEMA_NAME.lower()
                ):
                    self.format = syntax
                    self.data = item
                    return

    def title(self):
        return self.data.get("name")

    def total_time(self):
        total_time = get_minutes(self.data.get("totalTime"))
        if not total_time:
            return (
                get_minutes(self.data.get('prepTime')) +
                get_minutes(self.data.get('cookTime'))
            )
        return total_time

    def yields(self):
        return str(self.data.get("recipeYield"))

    def image(self):
        image = self.data.get('image')

        if image is None:
            raise SchemaOrgException("Image not found in SchemaOrg")

        if type(image) == dict:
            return image.get('url')
        elif type(image) == list:
            return image[0]

        return image

    def ingredients(self):
        return [
            normalize_string(ingredient)
            for ingredient in self.data.get("recipeIngredient", [])
        ]

    def instructions(self):
        recipeInstructions = self.data.get('recipeInstructions')
        if type(recipeInstructions) == list:
            return '\n'.join(
                instruction.get('text')
                for instruction in recipeInstructions
            )
        return self.data.get('recipeInstructions')

    def ratings(self):
        ratings = self.data.get("aggregateRating", None)
        if ratings is None:
            raise SchemaOrgException('No ratings data in SchemaOrg.')

        if type(ratings) == dict:
            return float(ratings.get('ratingValue'))
        return float(ratings)
