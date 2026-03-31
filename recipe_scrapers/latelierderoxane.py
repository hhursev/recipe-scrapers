from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string
from ._grouping_utils import IngredientGroup


class LAtelierDeRoxane(AbstractScraper):
    @classmethod
    def host(cls):
        return "latelierderoxane.com"

    def title(self):
        return self._get_text_from_bloc("bloc_titreh1", "h1")

    def description(self):
        return normalize_string(self._get_text_from_bloc("bloc_chapeau", "p"))

    def total_time(self):
        return get_minutes(self._get_bloc_temps_value_by_index(0))

    def prep_time(self):
        return get_minutes(self._get_bloc_temps_value_by_index(1))

    def cook_time(self):
        return get_minutes(self._get_bloc_temps_value_by_index(2))

    def yields(self):
        return get_yields(self._get_bloc_temps_value_by_index(4))

    def ingredients(self):
        ingredients_divs = self.soup.find_all("div", {"class": "ingredient"})
        ingredients = []
        for ingredient_div in ingredients_divs:
            text = normalize_string(ingredient_div.get_text(strip=True))
            if text and ":" not in text:
                ingredients.append(text)
        return ingredients

    def ingredient_groups(self):
        ingredients_divs = self.soup.find_all("div", {"class": "ingredient"})
        groups = []
        current_group = {"purpose": None, "ingredients": []}

        for ingredient_div in ingredients_divs:
            text = normalize_string(ingredient_div.get_text(strip=True))
            if not text:
                continue
            if ":" in text:
                if current_group["ingredients"]:
                    groups.append(current_group)
                current_group = {"purpose": text.strip(":"), "ingredients": []}
            else:
                current_group["ingredients"].append(text)

        if current_group["ingredients"]:
            groups.append(current_group)

        return [
            IngredientGroup(ingredients=group["ingredients"], purpose=group["purpose"])
            for group in groups
        ]

    def instructions(self):
        instructions_div = self.soup.find(
            "div", {"class": "bloc_texte_simple bloc_blog"}
        )
        instructions_list = instructions_div.find_all("li")
        return "\n".join(
            [
                normalize_string(instruction.get_text(strip=True))
                for instruction in instructions_list
            ]
        )

    def _get_bloc_temps_value_by_index(self, index):
        temps_div = self.soup.find("div", {"class": "bloc_temps bloc_blog"})
        infos_div = temps_div.find("div", {"class": "infos"})
        value_spans = infos_div.find_all("span", {"class": "valeur"})
        return value_spans[index].get_text(strip=True)

    def _get_text_from_bloc(self, bloc_class, tag):
        bloc_div = self.soup.find("div", {"class": f"{bloc_class} bloc_blog"})
        return bloc_div.find(tag).get_text(strip=True)
