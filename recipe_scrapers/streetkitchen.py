from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup, group_ingredients
from ._utils import get_minutes, get_yields, normalize_string


class StreetKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "streetkitchen.hu"

    def title(self):
        return self.soup.find("h1", {"class": "entry-title"}).text

    def total_time(self):
        items = self.soup.select(".the-content-div li")
        total_time = 0
        for item in items:
            total_time += get_minutes(item.text) or 0
        return total_time or None

    def image(self):
        return (
            self.soup.find("div", {"class": "article-featured-image-bg"})
            .find("noscript")
            .find("img")["src"]
        )

    def ingredients(self):
        ingredients_raw = self.soup.find("div", class_="ingredients-main").findAll("dd")
        ingredients = []
        for ingredient in ingredients_raw:
            ingredients.append(normalize_string(ingredient.text))
        return ingredients

    def instructions(self):
        instructions = self.soup.find("div", {"class": "the-content-div"}).findAll("p")

        instructions_arr = []
        for instruction in instructions:
            text = instruction.text
            # From the point we encounter "If you liked..." it's just ads.
            if text.startswith("Ha tetszett a"):
                break
            instructions_arr.append(normalize_string(text))

        return "\n".join(instructions_arr)

    def yields(self):
        return get_yields(self.soup.find("span", {"class": "quantity-number"}).text)

    def category(self):
        return self.soup.find("div", {"class": "entry-category"}).find("a").text

    def description(self):
        return normalize_string(self.soup.find("div", {"class": "entry-lead"}).text)

    def author(self):
        return normalize_string(
            self.soup.find("a", {"rel": "author"}).find("img")["alt"]
        )

    def ingredient_groups(self) -> list[IngredientGroup]:
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredients-main div.ingredient-group h3",
            ".ingredients-main div.ingredient-group dd",
        )

    def prep_time(self):
        items = self.soup.find("div", {"class": "the-content-div"}).find_all("li")

        for item in items:
            text = normalize_string(item.get_text())
            if "Elkészítési idő" in text:
                return get_minutes(text)

    def cook_time(self):
        items = self.soup.find("div", {"class": "the-content-div"}).find_all("li")

        for item in items:
            text = normalize_string(item.get_text())
            if "Sütési idő" in text:
                return get_minutes(text)

    def keywords(self):
        items = self.soup.find("ul", {"class": "tags-list"}).find_all("li")
        return [item.text for item in items]
