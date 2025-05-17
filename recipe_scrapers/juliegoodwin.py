import re

from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml
from ._utils import get_minutes, normalize_string


class JulieGoodwin(AbstractScraper):
    @classmethod
    def host(cls):
        return "juliegoodwin.com.au"

    def author(self):
        return "Julie Goodwin"

    def title(self):
        return normalize_string(self.soup.find("h1").get_text())

    def extract_time(self, keyword):
        minutes = 0
        time_elements = self.soup.find_all(["h4", "h3"])
        for element in time_elements:
            text = element.get_text(strip=True)
            match = re.search(
                rf"{keyword}\s*[\|=]?\s*(\d+)\s*(min|mins|minutes)", text, re.IGNORECASE
            )
            if match:
                minutes += int(match.group(1))
        return get_minutes(minutes)

    def prep_time(self):
        return self.extract_time("Prep time") or 0

    def cook_time(self):
        return self.extract_time("Cooking time") or 0

    def total_time(self):
        prep_time = self.prep_time()
        cook_time = self.cook_time()
        total_mins = prep_time + cook_time
        return total_mins

    def yields(self):
        container = self.soup.find("i", attrs={"class", "fa-cutlery"})
        if container:
            return normalize_string(container.next_sibling.get_text())

        return normalize_string(self.soup.find("h4").get_text())

    def image(self):
        container = self.soup.find("div", {"class": "inner-wrap"})
        if container:
            image = container.findNext("img", {"src": True})
            return image["src"] if image else None

    def ingredients(self):
        ingredients = self.soup.find("ul", {"class", "ingredients"})
        if ingredients:
            return [
                normalize_string(ingredient.get_text())
                for ingredient in ingredients.findAll("li")
            ]

        ingredients_heading = self.soup.find(string="Ingredients")
        if ingredients_heading:
            ingredients = ingredients_heading.findNext("h5")
            return [
                normalize_string(ingredient.split("•", 1)[1])
                for ingredient in ingredients.get_text().split("\n")
            ]

        raise ElementNotFoundInHtml("Could not find ingredients.")

    def instructions(self):
        instructions = self.soup.findAll(string=re.compile("STEP "))
        if instructions:
            return "\n".join(
                [
                    normalize_string(inst.next_element.get_text().split("|", 1)[1])
                    for inst in instructions
                ]
            )

        instruction_header = self.soup.find(string=re.compile("Method"))
        if instruction_header:
            instructions = instruction_header.parent.find_next_siblings(name="p")
            return "\n".join(
                [
                    normalize_string(inst.get_text().split(".", 1)[1])
                    for inst in instructions
                ]
            )

        raise ElementNotFoundInHtml("Could not find instructions.")
