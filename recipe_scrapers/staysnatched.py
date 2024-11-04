from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class StaySnatched(AbstractScraper):
    @classmethod
    def host(cls):
        return "staysnatched.com"

    def author(self):
        author_element = self.soup.find(
            "div",
            {
                "class": "wprm-recipe-block-container wprm-recipe-block-container-columns wprm-block-text-normal wprm-recipe-author-container"
            },
        )
        return author_element.find("a").get_text() if author_element else "Unknown"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )
