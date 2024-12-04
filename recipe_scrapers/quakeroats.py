from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml, FieldNotProvidedByWebsiteException
from ._utils import get_minutes, normalize_string


class QuakerOats(AbstractScraper):
    @classmethod
    def host(cls):
        return "quakeroats.com"

    def canonical_url(self):
        raise FieldNotProvidedByWebsiteException("No canonical URL provided")

    def instructions_list(self):
        raise ElementNotFoundInHtml("instructions_list")

    def author(self):
        return "Quaker Oats"

    def title(self):
        title_tag = self.soup.find("title")
        if title_tag:
            # Remove 'Recipe | Quaker Oats' from the title
            title_text = (
                title_tag.get_text().replace("Recipe | Quaker Oats", "").strip()
            )
            return normalize_string(title_text)
        return ""

    def category(self):
        # The website may not have categories.
        return None

    def total_time(self):
        # Extract preparation time
        prep_time_span = self.soup.find("span", id=lambda x: x and "lblPreptime" in x)
        if prep_time_span:
            prep_time = get_minutes(prep_time_span.get_text())
        else:
            prep_time = 0

        # Extract cook time
        cook_time_span = self.soup.find("span", id=lambda x: x and "lblCooktime" in x)
        if cook_time_span:
            cook_time = get_minutes(cook_time_span.get_text())
        else:
            cook_time = 0

        return prep_time + cook_time

    def yields(self):
        recipeyield = self.soup.find(itemprop="recipeYield")
        if recipeyield:
            return normalize_string(recipeyield.get_text())

        return None

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

    def instructions(self):
        instructions_section = self.soup.find("div", class_="CookingContent")
        if instructions_section:
            ul_tag = instructions_section.find("ul", class_="cook-desc")
            if ul_tag:
                steps = ul_tag.find_all("li")
                instructions = []
                for step in steps:
                    instruction_text = normalize_string(step.get_text())
                    instructions.append(instruction_text)
                return "\n".join(instructions)
        return ""

    def ratings(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def cuisine(self):
        # The website does not specify cuisine.
        return None

    def description(self):
        description_tag = self.soup.find("meta", attrs={"name": "description"})
        if description_tag:
            return normalize_string(description_tag.get("content", ""))
        return ""

    def language(self):
        return "en-US"
