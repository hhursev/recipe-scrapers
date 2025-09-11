from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields
from ._grouping_utils import group_ingredients


class LoveFood(AbstractScraper):
    @classmethod
    def host(cls):
        return "lovefood.com"

    def author(self):
        return self.soup.select_one('meta[name="og:article:author"]')["content"]

    def title(self):
        return self.soup.select_one('meta[name="og:title"]')["content"]

    def description(self):
        return self.soup.select_one('meta[name="og:description"]')["content"]

    def image(self):
        return self.soup.select_one('meta[name="og:image"]')["content"]

    def category(self):
        el = self.soup.select_one("li:-soup-contains('Recipe Type:')")
        return el.get_text(strip=True).split(":", 1)[-1].strip()

    def cuisine(self):
        el = self.soup.select_one("li:-soup-contains('Cuisine:')")
        return el.get_text(strip=True).split(":", 1)[-1].strip()

    def yields(self):
        el = self.soup.select_one("li:-soup-contains('Serves:')")
        return get_yields(el.get_text(strip=True).split(":", 1)[-1].strip())

    def ingredients(self):
        items = self.soup.select('ul[name="ingredients-metric"] li')
        return [li.get_text(strip=True) for li in items]

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".layout__item strong",
            '.layout__item ul[name="ingredients-metric"] li',
        )

    def instructions(self):
        items = self.soup.select("div.content__step-by-step ol li")
        return "\n".join([li.get_text(strip=True) for li in items])

    def _get_time_str(self, label):
        el = self.soup.select_one(f"li:-soup-contains('{label}')")
        if el:
            time_str = el.get_text(strip=True).split(":", 1)[-1].strip()
            return get_minutes(time_str)
        return None

    def prep_time(self):
        return self._get_time_str("Preparation Time")

    def cook_time(self):
        return self._get_time_str("Cooking Time")

    def total_time(self):
        prep = self.prep_time() or 0
        cook = self.cook_time() or 0
        total = prep + cook
        return total if total > 0 else None
