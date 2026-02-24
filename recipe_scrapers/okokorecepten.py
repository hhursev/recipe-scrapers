from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup


class OkokoRecepten(AbstractScraper):
    @classmethod
    def host(cls):
        return "okokorecepten.nl"

    def instructions(self):
        instructions = []

        voorbereiden_section = self.soup.find(
            "h2", string=lambda text: "Voorbereiden" in text if text else False
        )
        if voorbereiden_section:
            for sibling in voorbereiden_section.find_next_siblings(name=True):
                if sibling.name == "h2":
                    break
                if sibling.name == "p":
                    instructions.append(sibling.get_text(strip=True))

        bereiden_section = self.soup.find(
            "h2", string=lambda text: "Bereiden" in text if text else False
        )
        if bereiden_section:
            for sibling in bereiden_section.find_next_siblings(name=True):
                if sibling.name == "h2":
                    break
                if sibling.name == "p":
                    instructions.append(sibling.get_text(strip=True))

        return "\n".join(instructions)

    def ingredient_groups(self):
        ingredient_groups = []
        ingredients_section = self.soup.find(
            "h2", string=lambda text: "Ingrediënten" in text if text else False
        )
        if not ingredients_section:
            return None

        current_group = {"purpose": None, "ingredients": []}

        for sibling in ingredients_section.find_next_siblings(name=True):
            if sibling.name == "h2":
                break
            if sibling.name == "ul":
                for li in sibling.find_all("li"):
                    if "tussenkop" in li.get("class", []):
                        if current_group["ingredients"]:
                            ingredient_groups.append(current_group)
                            current_group = {
                                "purpose": li.get_text(strip=True),
                                "ingredients": [],
                            }
                    else:
                        current_group["ingredients"].append(li.get_text(strip=True))

        if current_group["ingredients"]:
            ingredient_groups.append(current_group)

        return [
            IngredientGroup(ingredients=group["ingredients"], purpose=group["purpose"])
            for group in ingredient_groups
        ]
