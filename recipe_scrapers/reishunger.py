from ._abstract import AbstractScraper
from ._utils import normalize_string


class Reishunger(AbstractScraper):
    @classmethod
    def host(cls):
        return "reishunger.de"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        result = self.soup.find("section", {"class": "recipe-preparation"})
        if result:
            result = "\n".join(
                normalize_string(i.get_text()) for i in result.findAll("p")
            )
        return result

    def ratings(self):
        block = self.soup.find("div", {"id": "recipe-header"}).find(
            "div", {"class": "nrating"}
        )
        if block:
            cnt = len(block.findAll("span", {"class": "fa-star"}))
            return cnt
        return block
