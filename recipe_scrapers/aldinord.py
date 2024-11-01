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
        return (
            self.schema.data.get("recipeInstructions", "")
            .replace("\xa0", " ")
            .replace("\r\n ", "\n")
        )
