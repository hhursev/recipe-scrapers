from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_minutes, get_yields, normalize_string


class QuakerOats(AbstractScraper):
    @classmethod
    def host(cls):
        return "quakeroats.com"

    def author(self):
        return "The Quaker Oats Company"

    def title(self):
        title_tag = self.soup.find("title")
        if title_tag:
            # Remove 'Recipe | Quaker Oats' from the title
            title_text = (
                title_tag.get_text().replace("Recipe | Quaker Oats", "").strip()
            )
            return normalize_string(title_text)
        return ""

    def _get_metadata_from_span(self, partial_id):
        el = self.soup.find("span", id=lambda x: x and partial_id in x)
        return el.get_text(strip=True) if el else ""

    def prep_time(self):
        times = self.soup.find_all("span", id=lambda x: x and "lblCooktime" in x)
        if len(times) == 2:
            return get_minutes(times[0].get_text())
        return 0

    def cook_time(self):
        times = self.soup.find_all("span", id=lambda x: x and "lblCooktime" in x)
        if len(times) == 2:
            return get_minutes(times[1].get_text())
        return 0

    def yields(self):
        return get_yields(self._get_metadata_from_span("lblServings"))

    def total_time(self):
        prep = self.prep_time()
        cook = self.cook_time()
        return prep + cook

    def ingredients(self):
        ingredients = []
        ingredients_container = self.soup.find(
            "div", id=lambda x: x and "lblIngredients" in x
        )
        if ingredients_container:
            ul_tag = ingredients_container.find("ul")
            if ul_tag:
                for item in ul_tag.find_all("li"):
                    # Extract quantity if present
                    quantity_tag = item.find("span", class_="quantity")
                    if quantity_tag:
                        quantity = normalize_string(quantity_tag.get_text())
                        # Remove the quantity from the item text
                        quantity_tag.extract()
                    else:
                        quantity = ""
                    # The remaining text is the ingredient name
                    ingredient_name = normalize_string(item.get_text())
                    ingredient = f"{quantity} {ingredient_name}".strip()
                    ingredients.append(ingredient)
        return ingredients

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingrd-txts li p strong",
            ".ingrd-txts li",
        )

    def instructions(self):
        instructions_section = self.soup.find("div", class_="CookingContent")
        if not instructions_section:
            return None
        ul_tag = instructions_section.find("ul", class_="cook-desc")
        if not ul_tag:
            return None
        steps = ul_tag.find_all("li")
        instructions = [normalize_string(step.get_text()) for step in steps]
        return "\n".join(instructions)

    def description(self):
        description_tag = self.soup.find("meta", attrs={"name": "description"})
        if description_tag and description_tag.get("content"):
            return normalize_string(description_tag["content"])

    def language(self):
        return "en-US"
