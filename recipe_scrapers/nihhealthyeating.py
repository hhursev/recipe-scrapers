from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml, StaticValueException
from ._grouping_utils import IngredientGroup
from ._utils import get_minutes, get_yields, normalize_string


class NIHHealthyEating(AbstractScraper):
    @classmethod
    def host(cls):
        return "healthyeating.nhlbi.nih.gov"

    def title(self):
        # This content must be present for all recipes on this website.
        return normalize_string(self.soup.h1.get_text())

    def site_name(self):
        raise StaticValueException(
            return_value="National Heart, Lung and Blood Institute"
        )

    def total_time(self):
        # This content must be present for all recipes on this website.
        time_table = self.soup.find("table", {"class": "recipe_time_table"})

        if time_table is None:
            raise ElementNotFoundInHtml("Table with times was not found.")

        return sum(
            get_minutes(td) for td in time_table.find_all("td") if get_minutes(td)
        )

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

    def ingredient_groups(self) -> list[IngredientGroup]:
        # This content must be present for recipes on this website.
        ingredients_div = self.soup.find("div", {"id": "ingredients"})
        section = []

        if ingredients_div is None:
            raise ElementNotFoundInHtml("Ingredients not found.")

        # Find more than one lists of ingredients
        ingredients_h4_sections = ingredients_div.find_all("h4")

        # Ingredients are broken down into sections
        # https://healthyeating.nhlbi.nih.gov/recipedetail.aspx?linkId=11&cId=1&rId=5

        if len(ingredients_h4_sections) >= 2:
            ingredients_sections = ingredients_div.find_all("tr")
            for ingredients_section in ingredients_sections:
                items = ingredients_section.find("p").get_text().strip().split("\n")
                # create ingredient group for each section
                res = IngredientGroup(
                    ingredients=items,
                    purpose=normalize_string(ingredients_section.find("h4").get_text()),
                )
                section.append(res)
            return section

        # Default case
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
                .get_text()
                .strip()
                .split("\n")
            )
            group = IngredientGroup(
                purpose=normalize_string(ingredients_h4_sections[0].get_text()),
                ingredients=items,
            )
            section.append(group)
            section.append(IngredientGroup(ingredients=ingredients_list[:-1]))
            return section

        return [IngredientGroup(ingredients_list)]

    def ingredients(self) -> list[str]:
        results = []
        for ingredient_group in self.ingredient_groups():
            results.extend(ingredient_group.ingredients)
        return results

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
                if element.get_text().strip() != "":
                    elements.append(normalize_string(element.get_text()))

        for i in range(0, len(elements), 2):
            if len(elements) > i + 1:
                k, v = elements[i], elements[i + 1]
                nutrition[k] = v

        return nutrition

    def description(self):
        return normalize_string(
            self.soup.find("p", {"class": "recipe_detail_subtext"}).get_text()
        )

    def prep_time(self):
        return get_minutes(
            self.soup.find("table", {"class": "recipe_time_table"})
            .find_all("td")[0]
            .get_text()
        )

    def cook_time(self):
        return get_minutes(
            self.soup.find("table", {"class": "recipe_time_table"})
            .find_all("td")[1]
            .get_text()
        )

    def serving_size(self):
        return normalize_string(
            self.soup.find("table", {"class": "recipe_time_table"})
            .find_all("td")[3]
            .get_text()
        )

    def recipe_source(self):
        return normalize_string(
            self.soup.find("div", {"id": "Recipe_Source"}).get_text().split(": ")[1]
        )

    def recipe_cards(self):
        recipe_cards_maker = self.soup.find("strong", string="Recipe Cards:")

        if recipe_cards_maker is None:
            return None

        recipe_cards = []
        recipe_cards_maker_siblings = recipe_cards_maker.next_siblings
        for recipe_cards_maker_sibling in recipe_cards_maker_siblings:
            link = recipe_cards_maker_sibling.find("a")
            if recipe_cards_maker_sibling.name == "li":
                recipe_cards.append(
                    {
                        "size": normalize_string(recipe_cards_maker_sibling.get_text()),
                        "url": link.get("href"),
                    }
                )
        return recipe_cards
