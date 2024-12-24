# from pprint import pprint
from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_minutes, get_yields, normalize_string


class JoshuaWeissman(AbstractScraper):
    @classmethod
    def host(cls):
        return "joshuaweissman.com"

    def prep_time(self):
        spans = self.soup.findAll(name="span")
        spans_texts = [tag.get_text().lower() for tag in spans]
        prep = next((tag for tag in spans_texts if "prep time" in tag), None)
        if prep:
            return get_minutes(prep)
        return None

    def cook_time(self):
        spans = self.soup.findAll(name="span")
        spans_texts = [tag.get_text().lower() for tag in spans]
        cook = next((tag for tag in spans_texts if "cook time" in tag), None)
        if cook:
            return get_minutes(cook)
        return None

    def total_time(self):
        total = self.prep_time() or 0
        total += self.cook_time() or 0
        return total if total > 0 else None

    def yields(self):
        spans = self.soup.findAll(name="span")
        return get_yields(
            next(
                (
                    tag.get_text()
                    for tag in spans
                    if "serving size" in tag.get_text().lower()
                ),
                None,
            )
        )

    def ingredients(self):
        ingredients = [
            li.get_text() for ul in self.soup.findAll("ul") for li in ul.findAll("li")
        ]

        ingredients = [
            normalize_string(ingredient) for ingredient in ingredients if ingredient
        ]

        return ingredients

    def ingredient_groups(self):
        # This is the css for it but web site has weird structuring so it doesn't work properly
        return group_ingredients(
            self.ingredients(),
            self.soup,
            'span[style="font-weight:700"]',
            "ul>li",
        )

    def instructions(self):
        instructions = [
            li.get_text() for ol in self.soup.findAll("ol") for li in ol.findAll("li")
        ]

        instructions = [
            normalize_string(instruction) for instruction in instructions if instruction
        ]

        return "\n".join(instructions)

    def description(self):
        return self.soup.find(id="viewer-foo").get_text()
