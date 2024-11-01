from ._abstract import AbstractScraper


class AldiNord(AbstractScraper):
    @classmethod
    def host(cls, domain: str = "aldi-nord.de"):
        return domain

    def author(self):
        return "ALDI"

    def site_name(self):
        return "ALDI"

    def instructions(self):
        instructions: str | None = self.schema.data.get("recipeInstructions", None)
        if instructions:
            return instructions.replace("\xa0", " ").replace("\r\n ", "\n")
