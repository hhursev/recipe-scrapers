import re

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields


class Aldi(AbstractScraper):
    @classmethod
    def host(cls):
        return "aldi.com.au"

    def site_name(self):
        return "Aldi"

    def author(self):
        return self.soup.find("meta", {"name": "author"}).get("content")

    def title(self):
        return self.soup.find("h1").text

    def category(self):
        element = self.soup.select_one("a.tab-nav--link.dropdown--list--link.m-active")
        if element:
            title = element.text
            recipe_position = title.find(" Recipe")
            if recipe_position != -1:
                return title[:recipe_position]

    def prep_time(self):
        return get_minutes(self._get_value(re.compile("prep", re.IGNORECASE)))

    def cook_time(self):
        return get_minutes(self._get_value(re.compile("cook", re.IGNORECASE)))

    def total_time(self):
        return (self.prep_time() or 0) + (self.cook_time() or 0)

    def yields(self):
        value = self._get_value(re.compile("(makes)|(serves)", re.IGNORECASE))
        return get_yields(str(value))

    def image(self):
        figure = self.soup.find(
            "figure", {"class": "csc-textpic-image csc-textpic-last"}
        )
        if figure:
            image = figure.find("img")
            if image:
                return image.get("src")
        return None

    def ingredients(self):
        h2 = self.soup.find("h2", string=re.compile("Ingredients"))
        list_element = h2.find_next_sibling("ul")
        ingredients = []
        for li in list_element.find_all("li"):
            ingredients.append(li.text.strip())
        return ingredients

    def instructions(self):
        list_element = self.soup.find("ol")
        return "\n".join(li.text.strip() for li in list_element.find_all("li"))

    def _get_value(self, label):
        label_element = self.soup.find("b", string=label)
        if label_element:
            parts = [
                sibling.strip()
                for sibling in label_element.find_next_siblings(string=True)
                if sibling.strip()
            ]
            return " ".join(parts)
        return None
