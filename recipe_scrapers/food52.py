from recipe_scrapers._abstract import AbstractScraper


class Food52(AbstractScraper):
    @classmethod
    def host(cls):
        return "food52.com"
