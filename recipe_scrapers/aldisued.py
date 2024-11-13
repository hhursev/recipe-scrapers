from ._abstract import AbstractScraper


class AldiSued(AbstractScraper):
    @classmethod
    def host(cls, domain="aldi-sued.de"):
        return domain

    def instructions(self):
        instruction_elements = self.schema.data.get("recipeInstructions", [])
        return "\n".join(
            [
                element.get("text").replace("\xad", "")
                for element in instruction_elements
                if element.get("text")
            ]
        )
