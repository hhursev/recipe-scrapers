import json

from ._abstract import AbstractScraper


class Mob(AbstractScraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.recipe_json = json.loads(
            self.soup.find("script", {"id": "__NEXT_DATA__"}).get_text()
        )["props"]["pageProps"]["recipe"]

    @classmethod
    def host(cls):
        return "mob.co.uk"

    def author(self):
        chefs = self.recipe_json.get("chefs", [])
        return " & ".join([chef["title"] for chef in chefs]) if chefs else "Mob Team"

    def title(self):
        return self.recipe_json.get("title", "")

    def category(self):
        return ", ".join([type["title"] for type in self.recipe_json.get("types", [])])

    def total_time(self):
        return self.recipe_json.get("time", "")

    def yields(self):
        servings = self.recipe_json.get("servingSize", "")
        return f"{servings} servings"

    def image(self):
        return self.recipe_json.get("image", [])[0]["url"]

    def instructions(self):
        return "\n".join(
            [
                instruction["description"]
                for instruction in self.recipe_json.get("method", [])
            ]
        )

    def cuisine(self):
        return ", ".join(
            [cuisine["title"] for cuisine in self.recipe_json.get("cuisines", [])]
        )

    def description(self):
        return self.recipe_json.get("summary", "")

    def ratings(self):
        return round(float(self.recipe_json.get("averageRating", "0")), 2)
