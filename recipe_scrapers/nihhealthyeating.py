from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml
from ._utils import get_minutes, get_yields, normalize_string


class NIHHealthyEating(AbstractScraper):
    @classmethod
    def host(cls):
        return "healthyeating.nhlbi.nih.gov"

    def title(self):
        # This content must be present for all recipes on this website.
        return self.soup.h1.get_text().strip()

    def total_time(self):
        # This content must be present for all recipes on this website.
        time_table = self.soup.find("table", {"class": "recipe_time_table"})

        if time_table is None:
            raise ElementNotFoundInHtml("Table with times was not found.")

        return sum([get_minutes(td) for td in time_table.find_all("td")])

    def yields(self):
        # This content must be present for all recipes on this website.
        time_table = self.soup.find("table", {"class": "recipe_time_table"})

        if time_table is None:
            raise ElementNotFoundInHtml(
                "Table with the number of servings that the recipe yields was not found."
            )

        i = 0
        for t in time_table.findAll("th"):
            if "Yields" in t:
                break
            i += 1

        if i >= len(time_table.findAll("td")):
            raise ElementNotFoundInHtml(
                "Table cells with servings that the recipe yields were not found."
            )

        return get_yields(time_table.find_all("td")[i])

    def image(self):
        # Optional content recipes on this website.
        img = self.soup.find("img", {"class": "recipe_image", "src": True})

        if img is None:
            raise ElementNotFoundInHtml("Image not found.")

        image_relative_url = img.get("src")

        if image_relative_url is None:
            raise ElementNotFoundInHtml("Image not found.")

        image_relative_url = f"https://{self.host()}{image_relative_url}"

        return image_relative_url

    def ingredients(self):
        # This content must be present for recipes on this website.
        ingredients_div = self.soup.find("div", {"id": "ingredients"})

        if ingredients_div is None:
            raise ElementNotFoundInHtml("Ingredients not found.")

        ingredients_p = ingredients_div.findAll("p")
        ingredients = [normalize_string(para.get_text()) for para in ingredients_p]

        return [
            ing for ing in ingredients if not ing.lower().startswith("recipe cards")
        ]

    def instructions(self):
        # This content must be present for recipes on this website.
        directions_div = self.soup.find("div", {"id": "recipe_directions"})

        if directions_div is None:
            raise ElementNotFoundInHtml("Instructions not found.")

        instructions = directions_div.findAll("div", {"class": "steptext"})

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
