from ._abstract import AbstractScraper


class FoodFidelity(AbstractScraper):
    @classmethod
    def host(cls):
        return "foodfidelity.com"

    def description(self):
        img_tag = self.soup.find("img", {"data-pin-description": True})
        if img_tag:
            return img_tag["data-pin-description"]
