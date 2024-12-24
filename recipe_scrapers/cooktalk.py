from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._grouping_utils import group_ingredients


class CookTalk(AbstractScraper):
    @classmethod
    def host(cls):
        return "cook-talk.com"

    def site_name(self):
        raise StaticValueException(return_value="Cook-Talk")

    def author(self):
        author_element = self.soup.find("div", {"class": "article-content"}).find(
            "a", {"href": lambda x: x and "recipe_author" in x}
        )
        return author_element.get_text()

    def category(self):
        article_meta = self.soup.find("div", {"class": "article-meta"})
        category_element = article_meta.find("small", {"class": "meta-category"})
        return category_element.find("a").get_text()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "div.ingredient-label",
            "ul#zlrecipe-ingredients-list li.ingredient",
        )
