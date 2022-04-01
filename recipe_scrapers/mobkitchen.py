import json
import re

from ._abstract import AbstractScraper
from ._schemaorg import SchemaOrg


class MobKitchen(AbstractScraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        recipe_schema = None
        for schema in self.soup.head.find_all("script", type="application/ld+json"):
            recipe_schema = schema.find(string=re.compile('"@type":"Recipe"'))

            if recipe_schema:
                break

        recipe_schema = json.loads(recipe_schema)

        # MobKitchen don't follow the Recipe schema correctly, so this fixes
        # the formatting so the Schema is parsed correctly.
        for instruction in recipe_schema["recipeInstructions"]:
            instruction["text"] = instruction["text"]["result"]

        self.schema = SchemaOrg(recipe_schema, raw=True)

    @classmethod
    def host(cls):
        return "mobkitchen.co.uk"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
