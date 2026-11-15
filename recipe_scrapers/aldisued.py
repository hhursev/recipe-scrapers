from ._abstract import AbstractScraper
from ._utils import normalize_string


class AldiSued(AbstractScraper):
    @classmethod
    def host(cls, domain="aldi-sued.de"):
        return domain

    def _parse_ingredients_vue_nuxt_template(self):
        """Parse ingredients from the new Nuxt/Vue template."""
        for div in self.soup.find_all("div", class_="base-rich-text"):
            if "Zutaten" not in div.get_text():
                continue
            ul = div.find("ul")
            if not ul:
                continue
            ingredients = []
            for li in ul.find_all("li"):
                parts = [
                    p.strip() for p in li.get_text().strip().split("\n") if p.strip()
                ]
                ingredients.append(" ".join(parts))
            if ingredients:
                return ingredients

        for tag in self.soup.find_all(
            ["p", "h1", "h2", "h3", "h4", "h5", "h6", "b", "strong"]
        ):
            if "Zutaten" in tag.get_text():
                ul = tag.find_next_sibling("ul")
                if not ul:
                    sibling = tag.find_next_sibling()
                    if sibling:
                        ul = sibling.find("ul") if sibling.name != "ul" else sibling
                if ul:
                    ingredients = []
                    for li in ul.find_all("li"):
                        parts = [
                            p.strip()
                            for p in li.get_text().strip().split("\n")
                            if p.strip()
                        ]
                        ingredients.append(" ".join(parts))
                    if ingredients:
                        return ingredients
        return None

    def _parse_ingredients_legacy_aem_template(self):
        """Parse ingredients from the old legacy AEM template."""
        ingredient_list = self.soup.find("ul", id="recipeIngredients")
        if not ingredient_list:
            return None
        spans = ingredient_list.find_all("span", class_="receipe-list-item-text")
        if not spans:
            return None
        return [normalize_string(span.get_text()) for span in spans]

    def ingredients(self):
        return (
            self._parse_ingredients_vue_nuxt_template()
            or self._parse_ingredients_legacy_aem_template()
            or self.schema.ingredients()
        )

    def instructions(self):
        instruction_elements = self.schema.data.get("recipeInstructions", [])
        return "\n".join(
            [
                element.get("text").replace("\xad", "")
                for element in instruction_elements
                if element.get("text")
            ]
        )
