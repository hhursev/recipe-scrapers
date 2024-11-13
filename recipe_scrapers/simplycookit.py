from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._grouping_utils import IngredientGroup
from ._utils import normalize_string


class SimplyCookit(AbstractScraper):
    @classmethod
    def host(cls):
        return "simply-cookit.com"

    def site_name(self):
        raise StaticValueException(return_value="Simply Cookit")

    def ingredients(self):
        ingredients = []
        for li in self.soup.find("ul", {"class": "recipe_ingredients"}).findAll("li"):
            if li.find("h3"):
                continue
            ingredients.append(normalize_string(li.get_text()))

        return ingredients

    def instructions(self):
        instructions = []
        for li in self.soup.find("ul", {"class": "recipe_steps"}).findAll("li"):
            li.find("span", {"class": "number"}).clear()
            instructions.append(normalize_string(li.get_text()))

        return "\n".join(instructions)

    def ingredient_groups(self):
        ingredient_groups = []
        current_group = None

        for li in self.soup.find("ul", {"class": "recipe_ingredients"}).findAll("li"):
            group_heading = li.find("h3")
            if group_heading:
                if current_group:
                    ingredient_groups.append(current_group)
                current_group = IngredientGroup(
                    ingredients=[], purpose=normalize_string(group_heading.get_text())
                )
            else:
                text = normalize_string(li.get_text())
                if text:
                    if current_group:
                        current_group.ingredients.append(text)
                    else:
                        if not ingredient_groups:
                            ingredient_groups.append(IngredientGroup(ingredients=[]))
                        ingredient_groups[0].ingredients.append(text)

        if current_group:
            ingredient_groups.append(current_group)

        return ingredient_groups or [IngredientGroup(ingredients=self.ingredients())]
