import extruct
from ._utils import get_minutes, normalize_string

SCHEMA_ORG_HOST = "schema.org"
SCHEMA_NAMES = ["Recipe", "WebPage"]

SYNTAXES = ["microdata", "json-ld"]


class SchemaOrgException(Exception):
    def __init__(self, message):
        super().__init__(message)


class SchemaOrg:

    def __init__(self, page_data, host):
        self.format = None
        self.host = host
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
                    item.get("@type", "").lower() in [schema.lower() for schema in SCHEMA_NAMES]
                ):
                    self.format = syntax
                    self.data = item
                    if item.get("@type").lower() == 'webpage':
                        self.data = self.data.get('mainEntity')
                    return

    def language(self):
        return self.data.get("inLanguage") or self.data.get("language")

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
        recipe_yield = str(self.data.get("recipeYield"))
        if len(recipe_yield) <= 3:  # probably just a number. append "servings"
            return recipe_yield + " serving(s)"

        if '\n' in recipe_yield:
            recipe_yield = recipe_yield.split('\n')[-1]

        return recipe_yield

    def image(self):
        image = self.data.get('image')

        if image is None:
            raise SchemaOrgException("Image not found in SchemaOrg")

        if type(image) == dict:
            return image.get('url')
        elif type(image) == list:
            if type(image[0]) == dict:
                return image[0].get('url')
            return image[0]

        if self.host not in image:
            # some sites give image path relative to the domain
            # in cases like this handle image url with class methods or og link
            return ''

        return image

    def ingredients(self):
        ingredients = (
            self.data.get("recipeIngredient") or
            self.data.get("ingredients") or
            []
        )
        return [
            normalize_string(ingredient)
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = (
            self.data.get('recipeInstructions') or
            ''
        )
        if type(instructions) == list:
            return '\n'.join(
                instruction.get('text') if type(instruction) is dict else instruction
                for instruction in instructions
            )
        return instructions

    def ratings(self):
        ratings = self.data.get("aggregateRating", None)
        if ratings is None:
            raise SchemaOrgException('No ratings data in SchemaOrg.')

        if type(ratings) == dict:
            return round(float(ratings.get('ratingValue')), 2)
        return round(float(ratings), 2)
