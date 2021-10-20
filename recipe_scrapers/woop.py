from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class Woop(AbstractScraper):
    @classmethod
    def host(cls):
        return "woop.co.nz"

    def title(self):
        found = self.soup.find("meta", {"property": "og:title"})
        return normalize_string(found["content"])

    def ingredients(self):
        div = self.soup.findAll("div", {"class": "ingredients"})[0]
        li = div.findChildren("li")
        return [normalize_string(i.text) for i in li if i.text]

    def yields(self):
        div = self.soup.findAll("div", {"class": "serving-amount"})[0]
        value = div.findChildren("div", {"class": "value"})[0]
        return get_yields(value.text)

    def total_time(self):
        div = self.soup.findAll("div", {"class": "cook-time"})[0]
        p = div.findChildren("p")[0]
        value = get_minutes(p)
        return value

    def instructions(self):
        div = self.soup.findAll("div", {"class": "cooking-instructions"})[0]
        li = div.findChildren("li")
        normalized = [normalize_string(i.text) for i in li]
        return "\n".join([i for i in normalized if i])

    def nutrients(self):
        div = self.soup.findAll("div", {"class": "nutritional-info"})[0]
        li = div.findChildren("li")
        return {
            normalize_string(nutrient): normalize_string(value)
            for nutrient, value in [i.text.split(":") for i in li]
            if value is not None
        }
