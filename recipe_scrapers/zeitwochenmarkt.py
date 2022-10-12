# mypy: disallow_untyped_defs=False

from ._abstract import AbstractScraper
from ._schemaorg import Extractor
from ._utils import normalize_string


class ZeitWochenmarkt(AbstractScraper):
    def __init__(self, url, **kwargs):
        AbstractScraper.__init__(self, url, **kwargs)
        extractor = Extractor(self.page_data)
        for item in extractor.linked_data:
            if item.get("@type") == "ItemList":
                self.schema.data = item["itemListElement"][0]["item"]

    @classmethod
    def host(cls):
        return "zeit.de"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        class_name = "recipe-list-collection__special-ingredient"
        special_ingredients = [
            normalize_string(item.text)
            for item in self.soup.find_all("p", {"class": class_name})
        ]
        return special_ingredients + self.schema.ingredients()

    def instructions(self):
        class_name = "article__subheading article__subheading--recipe article__item"
        subset = self.soup.find("h2", {"class": class_name})
        class_name = "paragraph article__item"
        return "\n".join(
            [
                normalize_string(item.text)
                for item in subset.find_all_next("p", {"class": class_name})
            ]
        )

    def ratings(self):
        return self.schema.ratings()
