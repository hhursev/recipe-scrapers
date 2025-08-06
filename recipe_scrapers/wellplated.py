from ._abstract import AbstractScraper


class WellPlated(AbstractScraper):
    @classmethod
    def host(cls):
        return "wellplated.com"

    def cuisine(self):
        return self.schema.cuisine().replace(",", ", ")
