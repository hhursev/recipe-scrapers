from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class LAtelierDeRoxane(AbstractScraper):
    @classmethod
    def host(cls):
        return "latelierderoxane.com"

    def title(self):
        div = self.soup.find("div", {"class": "bloc_titreh1 bloc_blog"})
        return div.find("h1").get_text()

    def description(self):
        div = self.soup.find("div", {"class": "bloc_chapeau bloc_blog"})
        cleaned_description = div.find("p").get_text()
        return normalize_string(cleaned_description)

    def total_time(self):
        return get_minutes(self.get_bloc_temps_value_by_index(0))

    def prep_time(self):
        return get_minutes(self.get_bloc_temps_value_by_index(1))

    def cook_time(self):
        return get_minutes(self.get_bloc_temps_value_by_index(2))

    def yields(self):
        return get_yields(self.get_bloc_temps_value_by_index(4))

    def ingredients(self):
        raw_ingredients = self.soup.find_all("div", {"class": "ingredient"})
        formatted_ingredients = []
        for ingredient in raw_ingredients:
            formatted_ingredients.append(normalize_string(ingredient.get_text()))
        return formatted_ingredients

    def instructions(self):
        instruction_bloc = self.soup.find(
            "div", {"class": "bloc_texte_simple bloc_blog"}
        )
        instructions = instruction_bloc.find_all("li")
        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def site_name(self):
        return "L'Atelier de Roxane"

    def get_bloc_temps_value_by_index(self, i):
        div_bloc = self.soup.find("div", {"class": "bloc_temps bloc_blog"})
        div_infos = div_bloc.find("div", {"class": "infos"})
        span_value = div_infos.find_all("span", {"class": "valeur"})
        return span_value[i].get_text()
