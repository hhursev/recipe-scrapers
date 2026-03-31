from ._abstract import AbstractScraper
from ._exceptions import FieldNotProvidedByWebsiteException


class Drinkoteket(AbstractScraper):
    @classmethod
    def host(cls):
        return "drinkoteket.se"

    def ingredients(self):
        items = []
        for li in self.soup.select("ul.ingredients > li"):
            if "separator" in li.get("class", []):
                break
            text = li.get_text()
            if text:
                items.append(text.strip())
        return items

    def yields(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def equipment(self):
        return [e.get_text(strip=True) for e in self.soup.select("div.rbs-img-content")]
