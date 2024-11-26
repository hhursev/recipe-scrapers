import re

from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml
from ._grouping_utils import IngredientGroup
from ._utils import get_minutes, normalize_string


class SamsungFood(AbstractScraper):
    @classmethod
    def host(cls):
        return "app.samsungfood.com"

    def author(self):
        return normalize_string(
            self.soup.h1.previous_sibling.find("span").get_text().replace("By ", "")
        )

    def title(self):
        return normalize_string(self.soup.h1.get_text())

    def image(self):
        img = self.soup.find(id="recipe-wrapper").next_element.next_element.find(
            "img", src=re.compile("user-recipes")
        )["src"]
        if not img or img == "":
            raise ElementNotFoundInHtml
        return img

    def description(self):
        try:
            return normalize_string(
                self.soup.find(
                    attrs={"data-testid": "saved-recipe-description"}
                ).get_text()
            )
        except AttributeError:
            return None

    def yields(self):
        return self.soup.find(attrs={"data-testid": "servings-block"}).get_text()

    # Helper method:
    def _ingredient_list_elements(self):
        ing_header = self.soup.find("div", string="Ingredients")
        return ing_header.parent.parent.find_next_siblings()

    def ingredients(self):
        ingredients = []
        element = self._ingredient_list_elements()[1]
        tags = element.find_all(attrs={"data-testid": "recipe-ingredient"})
        for tag in tags:
            if tag.div:
                tag.div.replace_with(", " + tag.div.string)
            ingredients.append(normalize_string(tag.get_text()))
        return ingredients

    def ingredient_groups(self):
        ingredient_groups = []
        element = self._ingredient_list_elements()[1]
        for group in element.children:
            ingredients = []
            purpose = None
            tags = group.find_all(attrs={"data-testid": "recipe-ingredient"})
            for item in group.children:
                if item.div:
                    # has div descendants => is ingredient
                    for tag in tags:
                        if tag.div:
                            tag.div.replace_with(", " + tag.div.string)
                        ingredients.append(normalize_string(tag.get_text()))
                else:
                    # is group
                    purpose = normalize_string(item.get_text())
            group = IngredientGroup(ingredients=ingredients, purpose=purpose)
            ingredient_groups.append(group)
        return ingredient_groups

    # Helper method:
    def _steps(self):
        instructions = self.soup.find(attrs={"data-scroll": "instructions"})
        try:
            return instructions.find_all("div", string=re.compile(r"^Step \d+$"))
        except AttributeError:
            return None

    def instructions(self):
        instructions = []
        if not self._steps():
            raise ElementNotFoundInHtml
        for step in self._steps():
            instructions.append(normalize_string(step.next_sibling.get_text()))
        return "\n".join(instructions)

    def equipment(self):
        equipment = []
        seen = set()
        if not self._steps():
            return None
        for step in self._steps():
            try:
                equ_list = step.next_sibling.next_sibling
                for equ in equ_list.find_all(
                    "div", recursive=False
                ):  # only direct children
                    if not equ.div.span.contents[0] in seen:
                        seen.add(equ.div.span.contents[0])
                        equipment.append(
                            normalize_string(str(equ.div.span.contents[0]))
                        )
            except AttributeError:
                continue
        return equipment

    def keywords(self):
        try:
            key_list = self.soup.find(attrs={"data-testid": "tags"}).children
        except AttributeError:
            return None
        return [normalize_string(key.get_text()) for key in key_list]

    def cook_time(self):
        try:
            return get_minutes(
                self.soup.find(string=re.compile(r"^Cook: $")).next_element.string
            )
        except AttributeError:
            return None

    def prep_time(self):
        try:
            return get_minutes(
                self.soup.find(string=re.compile(r"^Prep: $")).next_element.string
            )
        except AttributeError:
            return None

    def total_time(self):
        prep = self.prep_time()
        cook = self.cook_time()
        if prep and cook:
            return prep + cook
        elif prep:
            return prep
        elif cook:
            return cook
        else:
            raise ElementNotFoundInHtml

    # Helper method:
    def _likes(self):
        try:
            return int(
                self.soup.find(string=re.compile(r"^\d+ liked$")).replace(" liked", "")
            )
        except AttributeError:
            return 0

    # Helper method:
    def _dislikes(self):
        try:
            return int(
                self.soup.find(string=re.compile(r"^\d+ disliked$")).replace(
                    " disliked", ""
                )
            )
        except AttributeError:
            return 0

    def ratings(self):
        # portion of positive ratings on a scale of 0-5
        if not self._likes() + self._dislikes() == 0:
            return self._likes() / (self._likes() + self._dislikes()) * 5
        else:
            return None

    def ratings_count(self):
        return self._likes() + self._dislikes()

    def nutrients(self):
        nutrients = {}
        parameters = {
            "Calories": {"unit": "calories", "key": "calories"},
            "Total Fat": {"unit": "grams fat", "key": "fatContent"},
            "Carbs": {"unit": "grams carbohydrates", "key": "carbohydrateContent"},
            "Sugars": {"unit": "grams sugar", "key": "sugarContent"},
            "Protein": {"unit": "grams protein", "key": "proteinContent"},
        }

        try:
            data = self.soup.find(
                "h3", string="Nutrition per serving"
            ).next_element.next_element.next_element.children
        except AttributeError:
            return None

        for nutrient in data:
            try:
                key = normalize_string(nutrient.strong.get_text())
                value = normalize_string(nutrient.span.get_text().split()[0])
            except AttributeError:
                continue
            try:
                nutrients[parameters[key]["key"]] = (
                    value + " " + parameters[key]["unit"]
                )
            except KeyError:
                continue
        return nutrients
