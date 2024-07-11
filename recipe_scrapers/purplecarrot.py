from ._abstract import AbstractScraper


class PurpleCarrot(AbstractScraper):
    @classmethod
    def host(cls):
        return "purplecarrot.com"

    def nutrients(self):
        return self.schema.nutrients()
