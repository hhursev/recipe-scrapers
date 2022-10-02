# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml
from ._utils import get_minutes, get_yields, normalize_string

import re
from bs4 import Tag


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
        section = []

        if ingredients_div is None:
            raise ElementNotFoundInHtml("Ingredients not found.")

        # Find more than one lists of ingredients
        ingredients_h4_sections = ingredients_div.find_all("h4")

        # https://healthyeating.nhlbi.nih.gov/recipedetail.aspx?linkId=11&cId=1&rId=5

        if len(ingredients_h4_sections) >= 2:
            ingredients_sections = ingredients_div.find_all("tr")
            for ingredients_section in ingredients_sections:
                items = ingredients_section.find("p").text.strip().split("\n")
                res = {
                    normalize_string(ingredients_section.find("h4").text.strip()): items
                }
                section.append(res)
            return section

        ingredients_p = ingredients_div.findAll("p")
        ingredients = [normalize_string(para.get_text()) for para in ingredients_p]
        ingredients_list = [
            ing for ing in ingredients if not ing.lower().startswith("recipe cards")
        ]

        # Edge case: ingredents are a mix for single main ingredients and a single sub section
        # https://healthyeating.nhlbi.nih.gov/recipedetail.aspx?linkId=0&cId=10&rId=163

        if len(ingredients_h4_sections) == 1:
            items = (
                ingredients_div.find("h4")
                .find_next_sibling("p")
                .text.strip()
                .split("\n")
            )
            res = {normalize_string(ingredients_h4_sections[0].text.strip()): items}
            section.append(res)
            return ingredients_list[:-1] + section

        return ingredients_list

    def instructions(self):
        # This content must be present for recipes on this website.
        directions_div = self.soup.find("div", {"id": "recipe_directions"})

        if directions_div is None:
            raise ElementNotFoundInHtml("Instructions not found.")

        instructions = directions_div.findAll("div", {"class": "steptext"})

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def nutrients(self):
        elements = []
        nutrition = {}

        for s in (
            self.soup.find("div", {"id": "nutrition_info"}).find("table").find_all("tr")
        ):
            for element in s.find_all("td"):
                if element.text.strip() != "":
                    elements.append(normalize_string(element.get_text()))

        for i in range(0, len(elements), 2):
            if len(elements) > i + 1:
                k, v = elements[i], elements[i + 1]
                nutrition[k] = v

        return nutrition

    def description(self):
        return normalize_string(
            self.soup.find("p", {"class": "recipe_detail_subtext"}).text.strip()
        )

    def prep_time(self):
        return get_minutes(
            self.soup.find("table", {"class": "recipe_time_table"})
            .find_all("td")[0]
            .text.strip()
        )

    def cook_time(self):
        return get_minutes(
            self.soup.find("table", {"class": "recipe_time_table"})
            .find_all("td")[1]
            .text.strip()
        )

    def serving_size(self):
        return normalize_string(
            self.soup.find("table", {"class": "recipe_time_table"})
            .find_all("td")[3]
            .text.strip()
        )

    def recipe_source(self):
        return normalize_string(
            self.soup.find("div", {"id": "Recipe_Source"}).text.split(": ")[1].strip()
        )

    def recipe_cards(self):
        recipe_cards_maker = self.soup.find(
            "strong", string=re.compile(r"Recipe Cards:")
        )
        if recipe_cards_maker is not None:
            recipe_cards = []
            recipe_cards_maker_siblings = recipe_cards_maker.next_siblings
            for recipe_cards_maker_sibling in recipe_cards_maker_siblings:
                link = recipe_cards_maker_sibling.find("a")
                if (
                    isinstance(recipe_cards_maker_sibling, Tag)
                    and recipe_cards_maker_sibling.name == "li"
                ):
                    recipe_cards.append(
                        {
                            "size": normalize_string(
                                recipe_cards_maker_sibling.get_text()
                            ),
                            "url": link.get("href"),
                        }
                    )
        else:
            return None
        return recipe_cards
