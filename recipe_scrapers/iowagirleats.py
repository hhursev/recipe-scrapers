from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_equipment

class iowagirleats(AbstractScraper):
    @classmethod
    def host(cls):
        return "iowagirleats.com"

    def author(self):
        return self.soup.find("meta", {"name": "author"})["content"]

    def title(self):
        return self.soup.find("h2", {"class": "wprm-recipe-name"}).get_text()

    def category(self):
        return self.soup.find("span", {"class": "wprm-recipe-keyword"}).get_text()

    def total_time(self):
        return self.soup.find("span", {"class": "wprm-recipe-total_time"}).get_text()

    def yields(self):
        return self.soup.find("span", {"class": "wprm-recipe-servings"}).get_text()

    def image(self):
        return self.soup.select_one(".wp-block-image img")["src"]
    
    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )

    def ingredients(self):
        ingredients = self.soup.find_all("li", {"class": "wprm-recipe-ingredient"})
        ingredient_list = []

        for ingredient in ingredients:
            ingredient_list.append(ingredient.get_text().strip())

        return ingredient_list

    def instructions(self):
        instructions = self.soup.find_all(
            "div", {"class": "wprm-recipe-instruction-text"}
        )
        instruction_list = []

        for instruction in instructions:
            instruction_list.append(instruction.get_text().strip())

        return "\n".join(instruction_list)

    def cuisine(self):
        return self.soup.find("span", {"class": "wprm-recipe-cuisine"}).get_text()

    def description(self):
        return self.soup.find("div", {"class": "wprm-recipe-summary"}).get_text()

    def equipment(self):
        equipment_items = [
            link.get_text()
            for link in self.soup.select(
                "div.wprm-recipe-equipment-name a.wprm-recipe-equipment-link"
            )
        ]
        return get_equipment(equipment_items)