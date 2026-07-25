from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class BBCFood(AbstractScraper):
    @classmethod
    def host(cls, domain="com"):
        return f"bbc.{domain}"

    def title(self):
        return normalize_string(self.soup.find("h1").get_text())

    def author(self):
        container = self.soup.find("div", {"class": "chef__name"})
        if not container:
            return None

        author = container.a
        return author.text if author else None

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            '.recipe-ingredients__sub-heading, [data-testid="recipe-ingredients"] > h3',
            '.recipe-ingredients__list-item, [data-testid="recipe-ingredients"] li',
        )
