from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class RealMomNutrition(AbstractScraper):
    @classmethod
    def host(cls):
        return "realmomnutrition.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".mv-create-ingredients h4",
            ".mv-create-ingredients ul li",
        )

    def equipment(self):
        return [
            item.get_text(strip=True)
            for item in self.soup.select(
                "ul.mv-create-products-list div.mv-create-products-product-name"
            )
        ]
