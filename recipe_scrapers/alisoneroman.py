from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup


class AlisoneRoman(AbstractScraper):
    @classmethod
    def host(cls):
        return "alisoneroman.com"

    def ingredient_groups(self):
        section = self.soup.select_one("section.gh-content")
        elements = section.find_all(["p", "ul"], recursive=False) if section else []
        groups = [
            IngredientGroup(
                ingredients=[
                    li.get_text(" ", strip=True)
                    for li in elements[i + 1].find_all("li")
                ],
                purpose=elements[i].get_text(strip=True),
            )
            for i in range(len(elements) - 1)
            if elements[i].name == "p" and elements[i + 1].name == "ul"
        ]
        return groups or [IngredientGroup(ingredients=self.ingredients())]
