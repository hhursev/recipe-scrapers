from ._abstract import AbstractScraper
from ._exceptions import StaticValueException, FieldNotProvidedByWebsiteException
from ._utils import get_yields


class RickBayless(AbstractScraper):
    @classmethod
    def host(cls):
        return "rickbayless.com"

    def site_name(self):
        raise StaticValueException(return_value="Rick Bayless")

    def author(self):
        raise StaticValueException(return_value="Rick Bayless")

    def title(self):
        header = self.soup.find("div", {"class": "page-header"})
        return header.find("h1").get_text(strip=True)

    def total_time(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def description(self):
        desc = self.soup.find("div", {"class": "recipe-description"})
        return desc.get_text(strip=True) if desc else None

    def ingredients(self):
        ingredients_div = self.soup.find("div", {"class": "recipe-ingredients"})
        items = ingredients_div.find_all("li", {"itemprop": "ingredients"})
        return [" ".join(li.get_text().split()) for li in items]

    def instructions(self):
        instructions_div = self.soup.find("div", {"class": "recipe-instructions"})
        return "\n".join(
            p.get_text().strip()
            for p in instructions_div.find_all("p")
            if p.get_text(strip=True)
        )

    def yields(self):
        servings = self.soup.find("div", {"class": "recipe-servings"})
        if not servings:
            return None
        text = servings.get_text(strip=True)
        result = text.replace("Servings:", "").strip()
        return get_yields(result)
