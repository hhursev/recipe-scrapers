from collections import defaultdict

from ._abstract import AbstractScraper
from ._exceptions import FieldNotProvidedByWebsiteException
from ._grouping_utils import IngredientGroup
from ._utils import normalize_string


class VeroniqueCloutier(AbstractScraper):
    @classmethod
    def host(cls):
        return "veroniquecloutier.com"

    def author(self):
        return self.soup.find("strong").get_text()

    def title(self):
        return self.soup.find("h1", {"class": "title -main -page-title"}).get_text()

    def total_time(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def yields(self):
        potion_line = self.soup.find(
            string=lambda text: text
            and ("portions" in text.lower() or "donne " in text.lower())
        )

        if not potion_line:
            return None

        parent_text = potion_line.parent.get_text() if potion_line.parent else None
        french_numbers = {
            "un": 1,
            "deux": 2,
            "trois": 3,
            "quatre": 4,
            "cinq": 5,
            "six": 6,
            "sept": 7,
            "huit": 8,
            "neuf": 9,
            "dix": 10,
            "onze": 11,
            "douze": 12,
            "treize": 13,
            "quatorze": 14,
            "quinze": 15,
        }
        special_cases = {"dizaine": 10, "douzaine": 12}

        for word in parent_text.split():
            word_lower = word.lower()
            if word.isdigit():
                return f"{word} serving" if int(word) == 1 else f"{word} servings"
            if word_lower in french_numbers:
                number = french_numbers[word_lower]
                return f"{number} serving" if number == 1 else f"{number} servings"
            if word_lower in special_cases:
                number = special_cases[word_lower]
                return f"{number} serving" if number == 1 else f"{number} servings"

        return None

    def ingredients(self):
        start = self.soup.find(
            string=lambda text: text and text.lower() == "ingrédients"
        )

        ingredient_list = []
        for sibling in start.find_all_next():
            if sibling.string and "préparation" in sibling.string.lower():
                break
            if sibling.name == "ul":
                ingredient_list.extend(li.text for li in sibling.find_all("li"))

        return ingredient_list

    def ingredient_groups(self):
        start = self.soup.find(
            string=lambda text: text and text.lower() == "ingrédients"
        )

        found_ingredients = []
        groupings = defaultdict(list)
        current_heading = None
        for sibling in start.find_all_next():
            if sibling.string and "préparation" in sibling.string.lower():
                break

            if sibling.name == "p" and sibling.text.strip():
                current_heading = sibling.text.strip()

            if sibling.name == "ul" and current_heading:
                groupings[current_heading].extend(
                    li.text for li in sibling.find_all("li")
                )
                found_ingredients.extend(li.text for li in sibling.find_all("li"))
            elif sibling.name == "ul":
                found_ingredients.extend(li.text for li in sibling.find_all("li"))

        if not groupings:
            return [IngredientGroup(ingredients=found_ingredients)]

        return [
            IngredientGroup(purpose=heading, ingredients=items)
            for heading, items in groupings.items()
        ]

    def instructions(self):
        start = self.soup.find(
            string=lambda text: text and text.lower() == "préparation"
        )

        instruction_list = []
        for sibling in start.find_all_next():
            if sibling.name == "div":
                break
            if sibling.name == "ol":
                instruction_list.extend(li.text for li in sibling.find_all("li"))
            elif sibling.name == "p" and sibling.text[0].isdigit():
                instruction_list.append(sibling.text[3:])

        return "\n".join(instruction_list)

    def description(self):
        return normalize_string(
            self.soup.find("div", {"class": "post-excerpt"}).get_text()
        )
