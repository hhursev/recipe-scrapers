from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class Foodism(AbstractScraper):
    @classmethod
    def host(cls):
        return "foodism.co.uk"

    def ingredients(self):
        ingredients_div = self.soup.find(
            "div", class_="recipe-tab-body article-ingredients-body clearfix"
        )
        if not ingredients_div:
            return []

        return [li.get_text(strip=True) for li in ingredients_div.find_all("li")]

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".recipe-tab-body .details",
            ".recipe-tab-body ul li",
        )

    def instructions(self):
        lis = [
            li.get_text(strip=True)
            for li in self.soup.select(
                "div.recipe-tab.article-method div.recipe-tab-body ol li"
            )
            if li.get_text(strip=True)
        ]
        return "".join(step + "\n" for step in lis)
