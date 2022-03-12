import json

from ._abstract import AbstractScraper
from ._exceptions import SchemaOrgException
from ._utils import normalize_string


class AkisPetretzikis(AbstractScraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.recipe_json = json.loads(
            self.soup.find("script", {"id": "__NEXT_DATA__"}).get_text()
        )

    @classmethod
    def host(cls):
        return "akispetretzikis.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        make_time = self.recipe_json["props"]["pageProps"]["ssRecipe"]["data"][
            "make_time"
        ]
        bake_time = self.recipe_json["props"]["pageProps"]["ssRecipe"]["data"][
            "bake_time"
        ]
        return make_time + bake_time

    def yields(self):
        return self.recipe_json["props"]["pageProps"]["ssRecipe"]["data"]["shares"]

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredient_sections = self.recipe_json["props"]["pageProps"]["ssRecipe"][
            "data"
        ]["ingredient_sections"]
        ingredients_list = []
        if len(ingredient_sections) == 0:
            return ingredients_list
        for ingredient in ingredient_sections[0]["ingredients"]:
            parts = []
            if ingredient["quantity"]:
                parts.append(ingredient["quantity"])
            if ingredient["unit"]:
                parts.append(ingredient["unit"])
            parts.append(ingredient["title"])
            ingredients_list.append(" ".join(parts))
        return ingredients_list

    def instructions(self):
        method = self.recipe_json["props"]["pageProps"]["ssRecipe"]["data"]["method"]
        if len(method) == 0:
            return ""
        instructions_list = [
            normalize_string(step["step"]) for step in method[0]["steps"]
        ]
        return "\n".join(instructions_list)

    def ratings(self):
        average_score = self.recipe_json["props"]["pageProps"]["ssRecipe"]["data"][
            "average_score"
        ]
        return round(float(average_score), 2)

    def cuisine(self):
        try:
            return self.schema.cuisine()
        except SchemaOrgException:
            return None

    def description(self):
        return self.schema.description()

    def language(self):
        return self.recipe_json["locale"]
