# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import get_yields


class OneHundredOneCookBooks(AbstractScraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.soup = self.soup.find("div", id="recipe")

    @classmethod
    def host(cls):
        return "101cookbooks.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.soup.find("h2").get_text()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        header = self.soup.find("div", class_="cb101-recipe-time-header")
        if header and "Serves" in header.text:
            data = self.soup.find("div", class_="cb101-recipe-time").text.strip()
            total_yields = data.split()[0]
            return get_yields(total_yields)

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients = []

        ingredient_items = self.soup.select(
            ".cb101-recipe-ingredients li.cb101-recipe-ingredient"
        )

        for item in ingredient_items:
            amount_element = item.select_one(".cb101-recipe-ingredient-amount")
            unit_element = item.select_one(".cb101-recipe-ingredient-unit")
            name_element = item.select_one(".cb101-recipe-ingredient-name")

            amount = amount_element.get_text(strip=True) if amount_element else ""
            unit = unit_element.get_text(strip=True) if unit_element else ""
            name = name_element.get_text(strip=True)

            if amount and unit:
                ingredient = f"{amount} {unit} {name}".strip()
            else:
                ingredient = f"{amount}{unit} {name}".strip()

            ingredients.append(ingredient)

        return ingredients

    def instructions(self):
        instructions_div = self.soup.find(
            "div", class_="cb101-recipe-header", string="Instructions"
        )
        instructions = []
        if instructions_div:
            instruction_group = instructions_div.find_next(
                "div", class_="cb101-recipe-instruction-group"
            )
            if instruction_group:
                for instruction in instruction_group.find_all("p"):
                    instructions.append(instruction.get_text(strip=True))
        return "\n".join(instructions)
