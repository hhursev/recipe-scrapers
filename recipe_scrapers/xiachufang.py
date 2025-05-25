from ._abstract import AbstractScraper
from ._exceptions import FieldNotProvidedByWebsiteException
from ._grouping_utils import group_ingredients


class Xiachufang(AbstractScraper):
    @classmethod
    def host(cls):
        return "xiachufang.com"

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

    def keywords(self):
        keywords = []
        keyword_links = self.soup.select("div.recipe-cats a")
        for link in keyword_links:
            text = link.get_text(strip=True)
            if text and text not in keywords:
                keywords.append(text)
        return keywords

    def description(self):
        desc_div = self.soup.select_one("div.desc")
        if desc_div:
            return desc_div.get_text(separator="", strip=True)

    def total_time(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def yields(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)
