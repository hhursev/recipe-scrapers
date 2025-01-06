from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_equipment


class CookiesAndCups(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookiesandcups.com"

    def author(self):
        return self.soup.select_one(
            ".post-author-detail.post-author-by .entry-author-name a"
        ).get_text(strip=True)

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".tasty-recipes-ingredients-body p strong",
            ".tasty-recipes-ingredients-body ul li",
        )

    def equipment(self):
        equipment_items = self.soup.select(
            ".tasty-recipes-instructions-body ol li a.tasty-link"
        )
        equipment_links_text = [item.get_text(strip=True) for item in equipment_items]
        return get_equipment(equipment_links_text)
