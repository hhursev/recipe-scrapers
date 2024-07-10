import extruct

from ._abstract import AbstractScraper
from ._utils import normalize_string


class ZeitWochenmarkt(AbstractScraper):
    def __init__(self, url, **kwargs):
        AbstractScraper.__init__(self, url, **kwargs)
        data = extruct.extract(
            self.soup.prettify(), syntaxes=["json-ld"], errors="log", uniform=True
        )
        for item in data["json-ld"]:
            if item.get("@type") == "ItemList":
                self.schema.data = item["itemListElement"][0]["item"]

    @classmethod
    def host(cls):
        return "zeit.de"

    def author(self):
        return self.soup.find("a", {"rel": "author"}).get_text().strip()

    def ingredients(self):
        ingredients = []
        for div_element in self.soup.select(".recipe-list-collection"):
            special_ingredients = div_element.select(
                ".recipe-list-collection__special-ingredient"
            )
            ingredients.extend(normalize_string(p.text) for p in special_ingredients)

            list_items = div_element.select(".recipe-list-collection__list li")
            ingredients.extend(
                normalize_string(li.get_text(strip=True, separator=" "))
                for li in list_items
            )

        return ingredients

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
