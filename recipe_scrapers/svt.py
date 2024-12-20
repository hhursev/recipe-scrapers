import json

from ._abstract import AbstractScraper
from ._utils import normalize_string


class Svt(AbstractScraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        data_string = self.soup.find("script", id="__NEXT_DATA__").string
        data = json.loads(data_string)
        self.apollo = data["props"]["pageProps"]["__APOLLO_STATE__"]
        recipe_id = self._get_recipe_id()
        self.recipe_data = self.apollo[recipe_id]

    @classmethod
    def host(cls):
        return "svt.se"

    def title(self):
        return self.recipe_data.get("title")

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def cook_time(self):
        return self.recipe_data.get("cookingTime")

    def prep_time(self):
        return self.recipe_data.get("preparationTime")

    def yields(self):
        portions_max = self.recipe_data.get("portionsMax")
        if portions_max:
            return f"{portions_max} servings"
        portions_min = self.recipe_data.get("portionsMin")
        if portions_min:
            return f"{portions_min} servings"
        return None

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients = []
        ingredient_groups = self.recipe_data.get("ingredientList")
        for group in ingredient_groups:
            group_ingredients = group.get("ingredients")
            for ingredient in group_ingredients:
                name = ingredient.get("name")
                amount = ingredient.get("amount")
                unit = ingredient.get("unit")
                ingredient_string = self._make_ingredient_string(name, amount, unit)
                ingredients.append(ingredient_string)
        return ingredients

    def instructions_list(self):
        # TODO: Use itemProp=recipeInstructions
        instructions_string = normalize_string(self.recipe_data.get("description"))
        print(instructions_string)
        instructions = instructions_string.split("\n\n")
        instructions = [normalize_string(instruction) for instruction in instructions]
        print(instructions)
        return instructions

    def instructions(self):
        return "\n".join(self.instructions_list())

    def author(self):
        chefs = self.recipe_data.get("chefs")
        if not chefs:
            return "SVT"
        chef_ref = chefs[0]["__ref"]
        chef = self.apollo[chef_ref]
        return chef["title"]

    def description(self):
        return self.recipe_data.get("lead")

    def _get_recipe_data(self):
        data_string = self.soup.find("script", id="__NEXT_DATA__").string
        data = json.loads(data_string)
        apollo = data["props"]["pageProps"]["__APOLLO_STATE__"]
        recipe_id = self._get_recipe_id(apollo)
        return apollo[recipe_id]

    def _get_recipe_id(self):
        root_query = self.apollo["ROOT_QUERY"]
        for key, value in root_query.items():
            if key.startswith("route"):
                return value["__ref"]
        return None

    def _make_ingredient_string(self, name, amount, unit):
        string = ""
        if amount:
            string += str(amount)
        if unit:
            string += unit
        if string:
            string += " "
        string += name
        return normalize_string(string)
