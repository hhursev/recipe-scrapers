import json

from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml, FieldNotProvidedByWebsiteException
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class Xiachufang(AbstractScraper):
    @classmethod
    def host(cls):
        return "xiachufang.com"

    def site_name(self):
        return "下厨房"

    def language(self):
        return "zh-CN"

    def title(self):
        title_tag = self.soup.select_one("h1.page-title")
        if title_tag:
            return title_tag.get_text(strip=True)

    def author(self):
        author_tag = self.soup.select_one("div.author a")
        if author_tag:
            return author_tag.get_text(strip=True)

    def ingredients(self):
        ingredients = []
        rows = self.soup.select("div.ings table tr:not(.delimiter)")
        for row in rows:
            name_cell = row.select_one("td.name")
            unit_cell = row.select_one("td.unit")
            if name_cell:
                name = name_cell.get_text(strip=True)
                unit = unit_cell.get_text(strip=True) if unit_cell else ""
                ingredient = f"{unit} {name}".strip()
                ingredients.append(ingredient)
        return ingredients

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "div.ings tr.delimiter td.name",
            "div.ings tr:not(.delimiter)",
        )

    def instructions(self):
        steps = []
        step_items = self.soup.select("div.steps ol li p.text")
        for step in step_items:
            text = step.get_text(strip=True)
            if text:
                steps.append(text)
        return "\n".join(steps)

    def category(self):
        category_tags = self.soup.select("div.recipe-cats > a")
        return ", ".join((normalize_string(t.get_text()) for t in category_tags))

    def description(self):
        desc_div = self.soup.select_one("div.desc")
        if not desc_div:
            raise ElementNotFoundInHtml("Could not find description")
        desc = desc_div.get_text(separator="", strip=True)
        tip_div = self.soup.select_one("div.tip")
        if tip_div:
            desc += f"\n[小贴士]: {normalize_string(tip_div.get_text())}"
        return desc

    def total_time(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def yields(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def keywords(self):
        recipe_json = self.soup.select_one("script[type='application/ld+json']")
        if not recipe_json:
            return None
        recipe = json.loads(recipe_json.get_text())
        keywords = recipe["keywords"]
        return [normalize_string(k) for k in keywords]
