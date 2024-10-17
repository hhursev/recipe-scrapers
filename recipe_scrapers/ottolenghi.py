from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class Ottolenghi(AbstractScraper):
    @classmethod
    def host(cls):
        return "ottolenghi.co.uk"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def image(self):
        return self.soup.find("div", class_="c-recipe-header__gallery").find("img")[
            "src"
        ]

    def ingredients(self):
        return self.schema.ingredients()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".c-recipe-ingredients__heading",
            ".c-recipe-ingredients tr:not(:has(.c-recipe-ingredients__heading))",
        )

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.title()

    def yields(self):
        return (
            self.soup.find("div", class_="c-recipe-header__timings")
            .find("span")
            .get_text(strip=True)
        )

    def prep_time(self):
        return (
            self.soup.find("div", class_="c-recipe-header__timings")
            .find_all("span")[1]
            .get_text(strip=True)
        )

    def cook_time(self):
        return (
            self.soup.find("div", class_="c-recipe-header__timings")
            .find_all("span")[2]
            .get_text(strip=True)
        )
