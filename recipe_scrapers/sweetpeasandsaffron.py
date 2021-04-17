from ._abstract import AbstractScraper
from ._utils import normalize_string


class SweetPeasAndSaffron(AbstractScraper):
    """
    Web scraper for Sweet Peas & Saffron website
    """

    @classmethod
    def host(cls):
        return "sweetpeasandsaffron.com"

    def title(self):
        return self.soup.find("h2", {"class": "wprm-recipe-name"}).text

    def total_time(self):
        return self.soup.find("span", {"class": "wprm-recipe-total_time"}).text

    def yields(self):
        return self.soup.find("span", {"class": "wprm-recipe-servings"}).text

    def image(self):
        return self.soup.find(
            "div", {"class": "wprm-recipe-image wprm-block-image-normal"}
        ).find("img")["data-src"]

    def _instructions_list(self):
        instructions = [
            e.text
            for e in self.soup.find_all(
                "div", {"class": "wprm-recipe-instruction-text"}
            )
        ]
        return [normalize_string(instruction) for instruction in instructions]

    def instructions(self):
        data = self._instructions_list()
        return "\n".join(data) if data else None

    def ingredients(self):
        ingredient_amount = self.soup.find_all(
            "span", {"class": "wprm-recipe-ingredient-amount"}
        )
        ingredient_unit = self.soup.find_all(
            "span", {"class": "wprm-recipe-ingredient-unit"}
        )
        ingredient_name = self.soup.find_all(
            "span", {"class": "wprm-recipe-ingredient-name"}
        )
        ingredients = [
            " ".join([n.text, a.text, u.text])
            for a, u, n in zip(ingredient_amount, ingredient_unit, ingredient_name)
        ]
        return ingredients

    def ratings(self):
        return self.soup.find("span", {"class": "wprm-recipe-rating-average"}).text

    def author(self):
        return self.soup.find("span", {"class": "wprm-recipe-author"}).text
