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
        list_element = h2.find_next_sibling(name="ul")
        ingredients = []
        for li in list_element.find_all("li"):
            ingredients.append(li.text.strip())
        return ingredients

    def instructions(self):
        list_element = self.soup.find("ol")
        return "\n".join(li.text.strip() for li in list_element.find_all("li"))

    def _get_value(self, label):
        # Find the element containing the label
        if hasattr(label, "search"):  # Is regex pattern
            # Find all b tags first
            all_b_tags = self.soup.find_all("b")
            # Then filter manually for regex match
            label_element = None
            for b in all_b_tags:
                if b.string and label.search(b.string):
                    label_element = b
                    break
        else:
            # Direct string match
            label_element = self.soup.find("b", string=label)

        if not label_element:
            return None

        # Extract value: Get parent of b tag and collect all text after the label
        parent = label_element.parent
        if not parent:
            return None

        # Get all content in the parent after the label_element
        value_text = ""
        capture = False
        for content in parent.contents:
            if content is label_element:
                capture = True
                continue
            if capture and hasattr(content, "text"):
                value_text += content.text
            elif capture and isinstance(content, str):
                value_text += content

        return value_text.strip() if value_text.strip() else None
