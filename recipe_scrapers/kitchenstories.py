from ._abstract import AbstractScraper


class KitchenStories(AbstractScraper):
    @classmethod
    def host(cls):
        return "kitchenstories.com"
