import re

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_minutes, get_yields, normalize_string


class NHSHealthierFamilies(AbstractScraper):
    @classmethod
    def host(cls):
        return "nhs.uk"

    def author(self):
        return "NHS Better Health"

    def title(self):
        title = normalize_string(self.soup.find("h1").get_text())
        if title.endswith(" recipe"):
            title = title[:-7]
        return title

    def _get_recipe_metadata(self):
        container = self.soup.find("div", {"class": "bh-recipe__description"})
        descriptions = container.findAll("p")
        content = "".join([description.get_text() for description in descriptions])
        prep_time = re.search(r"Prep: (\d+) mins", content)
        cook_time = re.search(r"Cook: (\d+) mins", content)
        recipe_yields = re.search(r"Serves (\d+)", content)
        return {
            "prep_time": get_minutes(prep_time.group(0)) if prep_time else None,
            "cook_time": get_minutes(cook_time.group(0)) if cook_time else None,
            "yields": get_yields(recipe_yields.group(0)) if recipe_yields else None,
        }

    def total_time(self):
        metadata = self._get_recipe_metadata()
        return metadata["prep_time"] + metadata["cook_time"]

    def yields(self):
        metadata = self._get_recipe_metadata()
        return metadata["yields"]

    def image(self):
        return self.soup.find("img", {"class": "nhsuk-image__img"})["src"]

    def ingredients(self):
        ingredients = []
        instructions_div = self.soup.find("div", {"class": "bh-recipe-instructions"})
        ul = instructions_div.find("ul")

        if ul:
            for li in ul.findAll("li"):
                ingredients.append(normalize_string(li.get_text()))

        # Stop when encountering an 'ol' element which is where instructions are stored.
        for sibling in ul.find_next_siblings():
            if sibling.name == "ol":
                break
            if sibling.name == "ul":
                for li in sibling.findAll("li"):
                    ingredients.append(normalize_string(li.get_text()))

        return ingredients

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".nhsuk-grid-column-one-third h3",
            ".nhsuk-grid-column-one-third li",
        )

    def instructions(self):
        instructions = (
            self.soup.find("div", {"class": "bh-recipe-instructions"})
            .find("ol")
            .findAll("li")
        )
        instructions = [
            instruction.find("p").get_text() for instruction in instructions
        ]
        return "\n".join(
            [normalize_string(instruction) for instruction in instructions]
        )

    def description(self):
        description_meta = self.soup.find("meta", {"name": "description"})
        return normalize_string(description_meta["content"])
