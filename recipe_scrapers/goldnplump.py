from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup
from ._exceptions import SchemaOrgException


class GoldnPlump(AbstractScraper):
    @classmethod
    def host(cls):
        return "goldnplump.com"

    def author(self):
        return "Gold'n Plump"

    def total_time(self):
        try:
            return self.schema.total_time()
        except SchemaOrgException:
            return None

    def is_group_heading(self, text):
        words = [w for w in text.strip().split() if any(c.isalnum() for c in w)]
        if not words:
            return False
        return words[0].isupper()

    def ingredients(self):
        container = self.soup.select(".recipe-ingredeients .field-item p")
        if not container:
            return []

        lines = []
        for p in container:
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
