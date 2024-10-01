from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class BarefootInThePines(AbstractScraper):
    @classmethod
    def host(cls):
        return "barefootinthepines.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".mv-create-ingredients h4",
            ".mv-create-ingredients ul li",
        )

    def nutrients(self):
        nutrition_container = self.soup.select_one(".mv-create-nutrition-box")
        if not nutrition_container:
            return None

        nutrition_data = {}
        for item in nutrition_container.select(".mv-create-nutrition-item"):
            label = item.select_one(".mv-create-nutrition-label")
            if label:
                label_text = label.get_text(strip=True)
                quantity = item.get_text(strip=True).replace(label_text, "").strip()
                nutrition_data[label_text] = quantity

        return nutrition_data
