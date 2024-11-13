from ._abstract import AbstractScraper
from ._exceptions import StaticValueException


class AldiNord(AbstractScraper):
    @classmethod
    def host(cls, domain: str = "aldi-nord.de"):
        return domain

    def author(self):
        if author_from_schema := self.schema.author():
            return author_from_schema

        raise StaticValueException(return_value="ALDI")

    def site_name(self):
        raise StaticValueException(return_value="ALDI")

    def instructions(self):
        return (
            self.schema.data.get("recipeInstructions", "")
            .replace("\xa0", " ")
            .replace("\r\n ", "\n")
        )
