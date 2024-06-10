# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from ._abstract import AbstractScraper


class DonnaHay(AbstractScraper):
    @classmethod
    def host(cls):
        return "donnahay.com.au"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredient_element = self.soup.find(
            "div", {"class": "ingredients"}
        )

        ingredients = []
        for ingredient in ingredient_element.find_all("li"):
            ingredients.append(ingredient.text.replace(u'\xa0', u' ').strip())

        return ingredients

    def ingredient_groups(self):
        ingredient_element = self.soup.find(
            "div", {"class": "ingredients"}
        )

        ingredient_group_elements = ingredient_element.find_all("ul")
        ingredient_group_names = ingredient_element.find_all("p")
        
        ingredient_groups = []
        for (index, group) in enumerate(ingredient_group_elements):
            
            ingredient_groups.append(
                IngredientGroup(
                    ingredients=[
                        ingredient.text.replace(u'\xa0', u' ').strip() for ingredient in group
                    ],
                    purpose=
                        ingredient_group_names[index - 1].text.replace(u'\xa0', u' ').strip() 
                            if len(ingredient_groups) != 0 
                            else None,
                ),
            )

        return ingredient_groups

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
