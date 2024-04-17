# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class HomeChef(AbstractScraper):
    @classmethod
    def host(cls):
        return "homechef.com"

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def instructions(self):
        return "\n".join(
            [
                element.get("name") + "\n\n" + element.get("description")
                for element in self.schema.data.get("recipeInstructions").get(
                    "itemListElement"
                )
            ]
        )

    def description(self):
        return self.schema.description()
