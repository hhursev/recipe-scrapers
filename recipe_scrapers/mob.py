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
