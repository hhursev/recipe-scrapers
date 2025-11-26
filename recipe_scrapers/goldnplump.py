from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup


class GoldnPlump(AbstractScraper):
    @classmethod
    def host(cls):
        return "goldnplump.com"

    def is_group_heading(self, text):
        words = [w for w in text.strip().split() if any(c.isalnum() for c in w)]
        if not words:
            return False

        uppercase_words = [w for w in words if w.isupper()]
        return len(uppercase_words) >= len(words) / 2

    def ingredients(self):

        ing = self.soup.select(".recipe-ingredeients .field-item p")
        if not ing:
            return []

        lines = []
        for p in ing:
            for el in p.children:
                if getattr(el, "name", None) == "b":
                    text = el.get_text(strip=True)
                    if not self.is_group_heading(text):
                        lines.append(text)
                elif isinstance(el, str):
                    text = el.strip()
                    if text:
                        lines.append(text)
        return lines

    def ingredient_groups(self):
        container = self.soup.select(".recipe-ingredeients .field-item p")
        if not container:
            return [IngredientGroup(ingredients=self.ingredients())]

        groups = []
        current_group = []
        current_heading = None

        for p in container:
            for element in p.children:
                if element.name == "b":
                    text = element.get_text(strip=True)
                    if self.is_group_heading(text):
                        if current_group:
                            groups.append(
                                IngredientGroup(
                                    ingredients=current_group, purpose=current_heading
                                )
                            )
                            current_group = []
                        current_heading = text.title()
                    else:
                        current_group.append(text)
                elif isinstance(element, str):
                    text = element.strip()
                    if text:
                        current_group.append(text)

        if current_group:
            groups.append(
                IngredientGroup(ingredients=current_group, purpose=current_heading)
            )

        return groups
