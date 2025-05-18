from ._abstract import AbstractScraper


class OrganicallyAddison(AbstractScraper):
    @classmethod
    def host(cls):
        return "organicallyaddison.com"
