from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup
from ._utils import normalize_string


class Sunset(AbstractScraper):
    @classmethod
    def host(cls):
        return "sunset.com"

    def ingredient_groups(self):
        groups = []
        current_group = []
        current_purpose = None

        for element in self.soup.select(
            ".recipe-ingredients .cooked-single-ingredient"
        ):
            classes = element.get("class", [])
            if "cooked-heading" in classes:
                if current_group:
                    groups.append(
                        IngredientGroup(
                            ingredients=current_group, purpose=current_purpose
                        )
                    )
                current_group = []
                current_purpose = normalize_string(element.get_text())
            elif "cooked-ingredient" in classes:
                ingredient = " ".join(
                    element.get_text(separator=" ", strip=True).split()
                )
                current_group.append(normalize_string(ingredient))

        if current_group:
            groups.append(
                IngredientGroup(ingredients=current_group, purpose=current_purpose)
            )

        return groups
