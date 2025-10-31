from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup


class AlisoneRoman(AbstractScraper):
    @classmethod
    def host(cls):
        return "alisoneroman.com"

    def _clean_ingredient(self, text):
        text = " ".join(text.split())
        for punct in [",", ".", "!", "?", ":"]:
            text = text.replace(f" {punct}", punct)
        return text.strip()

    def ingredients(self):
        section = self.soup.select_one("section.gh-content")
        if not section:
            return []

        seen = set()
        ingredients = []
        for li in section.select("ul > li"):
            item = self._clean_ingredient(li.get_text())
            if item not in seen:
                ingredients.append(item)
                seen.add(item)

        return ingredients

    def ingredient_groups(self):
        section = self.soup.select_one("section.gh-content")
        if not section:
            return [IngredientGroup(ingredients=self.ingredients())]

        flat_ingredients = self.ingredients()
        lookup = {i.lower(): i for i in flat_ingredients}
        used = set()

        groups = []
        elements = section.find_all(["p", "ul"], recursive=False)

        i = 0
        while i < len(elements):
            tag = elements[i]
            if tag.name == "p":
                purpose = tag.get_text(strip=True).strip()

                if i + 1 < len(elements) and elements[i + 1].name == "ul":
                    ul = elements[i + 1]
                    group_ingredients = []
                    for li in ul.find_all("li", recursive=False):
                        raw = self._clean_ingredient(li.get_text())
                        key = raw.lower()
                        if key in lookup and key not in used:
                            group_ingredients.append(lookup[key])
                            used.add(key)

                    if group_ingredients:
                        groups.append(
                            IngredientGroup(
                                ingredients=group_ingredients, purpose=purpose
                            )
                        )

                    i += 1
            i += 1

        if not groups:
            return [IngredientGroup(ingredients=self.ingredients())]

        return groups
