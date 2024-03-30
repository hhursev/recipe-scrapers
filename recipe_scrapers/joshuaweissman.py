# mypy: allow-untyped-defs

# from pprint import pprint
from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_minutes, get_yields, normalize_string


class JoshuaWeissman(AbstractScraper):
    @classmethod
    def host(cls):
        return "joshuaweissman.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        # Get all spans and get their text
        spans = self.soup.findAll(name="span")
        spans_texts = [tag.get_text().lower() for tag in spans]
        # Filter out all spans that don't contain time
        time_texts = [tag for tag in spans_texts if "time" in tag]

        # Find first string that contains the text
        def check_text(check_string):
            return next(
                (string for string in time_texts if check_string in string), None
            )

        total = check_text("total time")
        if total:
            total = get_minutes(total)
            if total:
                return total
        prep = check_text("prep time")
        if prep:
            prep = get_minutes(prep)
        cook = check_text("cook time")
        if cook:
            cook = get_minutes(cook)
        if prep + cook:
            return prep + cook

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

    def image(self):
        return self.schema.image()

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

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.soup.find(id="viewer-foo").get_text()
