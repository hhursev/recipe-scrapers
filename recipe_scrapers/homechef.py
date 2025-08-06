from ._abstract import AbstractScraper


class HomeChef(AbstractScraper):
    @classmethod
    def host(cls):
        return "homechef.com"

    def instructions(self):
        return "\n".join(
            [
                element.get("name") + "\n\n" + element.get("description")
                for element in self.schema.data.get("recipeInstructions").get(
                    "itemListElement"
                )
            ]
        )
