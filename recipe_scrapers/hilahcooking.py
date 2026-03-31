from ._abstract import AbstractScraper


class HilahCooking(AbstractScraper):
    @classmethod
    def host(cls):
        return "hilahcooking.com"

    def description(self):
        return self.soup.find("meta", {"itemprop": "description"}).get("content")
