from ._utils import normalize_string
from ._abstract import AbstractScraper


class CuisinezPourBebe(AbstractScraper):
    @classmethod
    def host(cls):
        return "cuisinez-pour-bebe.fr"

    def category(self):
        return self.schema.category()

    def image(self):
        return self.schema.image()

    def description(self):
        tags = self.soup.find(class_="wprm-recipe-summary").find_all("span")
        desc = [normalize_string(tag.get_text()) for tag in tags]
        return "\n".join(desc)
    
    def yields(self):
        return self.schema.data.get("recipeYield", "")[1]

    def instructions(self):
        instructions = self.soup.find_all(
            "div", {"class": "wprm-recipe-instruction-text"}
        )
        instruction_list = []

        for instruction in instructions:
            instruction_list.append(instruction.get_text().strip())

        return "\n".join(instruction_list)


