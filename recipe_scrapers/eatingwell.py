from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class EatingWell(AbstractScraper):
    @classmethod
    def host(cls):
        return "eatingwell.com"

    def title(self):
        return self.schema.title()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def total_time(self):
        div = self.soup.findAll("div", {"class": "recipe-meta-item"})
        d = {
            normalize_string(key): normalize_string(value)
            for key, value in [i.text.split(":") for i in div]
            if value is not None
        }
        return get_minutes(d.get("total"))

    def yields(self):
        div = self.soup.findAll("div", {"class": "recipe-meta-item"})
        d = {
            normalize_string(key): normalize_string(value)
            for key, value in (i.text.split(":") for i in div)
            if value is not None
        }
        return get_yields(d.get("Servings"))
