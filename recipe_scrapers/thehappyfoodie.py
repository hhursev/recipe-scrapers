from ._abstract import AbstractScraper
from ._utils import normalize_string


class TheHappyFoodie(AbstractScraper):
    @classmethod
    def host(cls):
        return "thehappyfoodie.co.uk"

    def ingredients(self):
        ingredient_elements = self.soup.find(
            "div", {"class": "hf-ingredients__container"}
        ).findAll("tr")

        amount = 0
        ingredient_name = 1
        ingredients = []
        for e in ingredient_elements:
            # Skip elements that look like section headings (for example, 'For the sauce:')
            if e.get("class"):
                continue
            ingredients.append(
                (
                    e.find_all("td")[amount].get_text(),
                    e.find_all("td")[ingredient_name].get_text(),
                )
            )

        return [normalize_string(f"{amount} {name}") for amount, name in ingredients]
