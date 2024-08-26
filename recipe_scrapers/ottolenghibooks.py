import re

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_yields, normalize_string


class OttolenghiBooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "books.ottolenghi.co.uk"

    def author(self):
        return "Ottolenghi"

    def title(self):
        return normalize_string(self.soup.h1.string)

    def yields(self):
        recipeyield = self.soup.find(itemprop="recipeYield").get_text().lower()
        replacements = [
            ("one", "1"),
            ("two", "2"),
            ("three", "3"),
            ("four", "4"),
            ("five", "5"),
            ("six", "6"),
            ("seven", "7"),
            ("eight", "8"),
            ("nine", "9"),
            ("ten", "10"),
            ("eleven", "11"),
            ("twelve", "12"),
            ("thirteen", "13"),
            ("fourteen", "14"),
            ("fifteen", "15"),
            ("sixteen", "16"),
            ("seventeen", "17"),
            ("eighteen", "18"),
            ("nineteen", "19"),
            ("twenty", "20"),
        ]
        for word, number in replacements:
            recipeyield = re.sub(r"\b" + word + r"\b", number, recipeyield)
        return get_yields(recipeyield)

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup.find(class_="recipe__aside"),
            "h3",
            "li",
        )

    def ingredients(self):
        ingredients = self.soup.find(class_="recipe__aside").find_all("li")
        return [normalize_string(i.get_text().replace(" - ", " ")) for i in ingredients]

    def instructions(self):
        recipe = self.soup.find(class_="recipe-list")
        tags = recipe.find_all("li")
        instructions = [normalize_string(tag.get_text()) for tag in tags]
        return "\n".join(instructions)

    def description(self):
        tags = self.soup.find(class_="recipe").find_all("p")
        desc = [normalize_string(tag.get_text()) for tag in tags]
        return "\n".join(desc)

    def dietary_restrictions(self):
        # this is consistently used only in the books Simple and Sweet
        diets = self.soup.find(class_="recipe__types").css.select(
            'a[href^="/simple/"], a[href^="/sweet/"]'
        )
        return [normalize_string(diet.get_text().lower()) for diet in diets]

    def keywords(self):
        # for the book Simple:
        simple_keywords = self.soup.find_all(class_="simple-icon")
        keywords = [
            normalize_string(k.get_text().replace("Simple ", ""))
            for k in simple_keywords
        ]
        # except for the books Simple and Sweet (see dietary_restrictions):
        other_keywords = self.soup.find(class_="recipe__types").css.select(
            'a:not([href^="/simple/"]):not([href^="/sweet/"])'
        )
        for k in other_keywords:
            keywords.append(normalize_string(k.get_text()))
        return keywords

    def category(self):
        return normalize_string(self.soup.find(class_="recipe-meta").get_text())
