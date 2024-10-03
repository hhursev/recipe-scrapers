import re

from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._grouping_utils import group_ingredients
from ._utils import get_minutes


class Tofoo(AbstractScraper):
    @classmethod
    def host(cls):
        return "tofoo.co.uk"

    def author(self):
        raise StaticValueException(return_value="The Tofoo co.")

    def title(self):
        return self.soup.find("div", {"class": "hero__content"}).find("h1").get_text()

    def _find_hero_stat(self, label):
        hero_stats = self.soup.find("ul", {"class": "hero__stats"})
        if hero_stats:
            for li in hero_stats.find_all("li"):
                if re.search(rf"{label}:", li.get_text()):
                    return li.get_text()
        return None

    def yields(self):
        serves_text = self._find_hero_stat("Serves")
        if serves_text:
            match = re.search(r"Serves:\s*(\d+)", serves_text)
            if match:
                return int(match.group(1))
        return None

    def prep_time(self):
        prep_text = self._find_hero_stat("Prep")
        return get_minutes(prep_text) if prep_text else 0

    def cook_time(self):
        cook_text = self._find_hero_stat("Cooking")
        return get_minutes(cook_text) if cook_text else 0

    def total_time(self):
        return self.prep_time() + self.cook_time()

    def ingredients(self):
        ingredients_div = self.soup.find(
            "div", {"class": "recipe_details__ingredients"}
        )
        return [li.get_text() for li in ingredients_div.find_all("li")]

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".recipe_details__ingredient h5",
            ".recipe_details__ingredient li",
        )

    def instructions(self):
        instructions_div = self.soup.find("div", {"class": "recipe_details__steps"})
        ol = instructions_div.find("div", {"class": "recipe_details__steps__ol"}).find(
            "ol"
        )
        return "\n".join([li.get_text() for li in ol.find_all("li")])

    def keywords(self):
        hero_cats = self.soup.find("ul", {"class": "hero__cats"})
        return [li.get_text() for li in hero_cats.find_all("li")] if hero_cats else []
