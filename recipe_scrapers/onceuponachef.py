from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class OnceUponAChef(AbstractScraper):
    @classmethod
    def host(cls):
        return "onceuponachef.com"

    def author(self):
        author_tag = self.soup.find("div", {"class": "postauthor"})
        author_name = normalize_string(author_tag.get_text())
        return author_name

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredients h4",
            "li.ingredient",
        )
