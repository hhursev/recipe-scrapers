# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import get_yields, normalize_string


class KwestiaSmaku(AbstractScraper):
    @classmethod
    def host(cls):
        return "kwestiasmaku.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def yields(self):
        return get_yields(
            self.soup.find("div", {"class": "field-name-field-ilosc-porcji"})
        )

    def image(self):
        return (
            self.soup.find("div", {"class": "view-zdjecia"})
            .find("li", {"class": "first"})
            .img["src"]
        )

    def ingredients(self):
        ingredients = self.soup.find(
            "div", {"class": "field-name-field-skladniki"}
        ).find_all("li")
        return [normalize_string(i.get_text()) for i in ingredients]

    def instructions(self):
        instructions = self.soup.find(
            "div", {"class": "field-name-field-przygotowanie"}
        ).find_all("li")
        return "\n".join([normalize_string(i.get_text()) for i in instructions])

    def ratings(self):
        return self.schema.ratings()
