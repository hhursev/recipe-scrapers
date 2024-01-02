# mypy: disallow_untyped_defs=False
import json

from ._abstract import AbstractScraper


class Mob(AbstractScraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.recipe_json = json.loads(
            self.soup.find("script", {"id": "__NEXT_DATA__"}).get_text()
        )["props"]["pageProps"]["recipe"]

    @classmethod
    def host(cls, domain="mob.co.uk"):
        return domain

    def author(self):
        return " & ".join([chef["title"] for chef in self.recipe_json.get("chefs", [])])

    def title(self):
        return self.recipe_json["title"]

    def category(self):
        return " & ".join([type["title"] for type in self.recipe_json.get("types", [])])

    def total_time(self):
        return self.recipe_json["time"]

    def yields(self):
        return self.recipe_json["servingSize"]

    def image(self):
        return self.recipe_json["image"][0]["url"]

    def ingredients(self):
        return [
            ingredient["label"]
            for ingredient in self.recipe_json.get("recipeIngredients", [])
        ]

    def instructions(self):
        return "\n".join(
            [
                instruction["description"]
                for instruction in self.recipe_json.get("method", [])
            ]
        )

    def cuisine(self):
        return self.recipe_json["cuisines"][0]["title"]

    def description(self):
        return self.recipe_json["summary"]

    def ratings(self):
        return self.recipe_json["averageRating"]
