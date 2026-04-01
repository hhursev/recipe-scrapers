import re
import requests
import json

from ._abstract import AbstractScraper


class MonsieurCuisine(AbstractScraper):
    def __init__(self, html: str, url: str, best_image=None):
        super().__init__(html, url, best_image)
        self.recipe_json = self._get_recipe_json()

    @classmethod
    def host(cls):
        return "monsieur-cuisine.com"

    def author(self):
        return self.recipe_json["data"]["recipe"]["author"]["name"]

    def title(self):
        return self.soup.find('h1').get_text()

    def category(self):
        return ""

    def total_time(self):
        minutes = self.recipe_json["data"]["recipe"]["servingSizes"][0]["duration"]
        return minutes

    def yields(self):
        return self.recipe_json["data"]["recipe"]["servingSizes"][0]["amount"]

    def image(self):
        return self.recipe_json["data"]["recipe"]["servingSizes"][0]["detailsImage"]["landscape"]

    def ingredients(self):
        ingredient_objects = self.recipe_json["data"]["recipe"]["servingSizes"][0]["ingredients"]
        ingredients = []
        for ingredient_tmp in ingredient_objects:
            ingredient = ingredient_tmp["amount"] + " " + ingredient_tmp["unit"] + " " + ingredient_tmp["name"]
            ingredients.append(ingredient)
        string = ""
        for ingredient in ingredients:
            string += ingredient + "\n"
        # remove the last \n
        string = string[:-1]
        return string

    def instructions(self):
        step_objects = self.recipe_json["data"]["recipe"]["servingSizes"][0]["steps"]
        instructions = []
        for step_tmp in step_objects:
            step = step_tmp["description"]
            instructions.append(step)
        string = ""
        for instruction in instructions:
            if instruction:
                string += instruction + "\n"
        # remove the last \n
        string = string[:-1]
        return string

    def ratings(self):
        return ""

    def cuisine(self):
        cat = self.recipe_json["data"]["recipe"]["categories"]
        string = ""
        if cat:
            for c in cat:
                string += c["name"] + "\n"
            # remove the last \n
            string = string[:-1]
        return string

    def description(self):
        desc = self.recipe_json["data"]["recipe"]["description"]
        if desc:
            return desc
        return ""
    
    def site_name(self):
        return "monsieurcuisine.com"

    def _recipe_id(self):
        site_config_script = self.soup.find(
            "script",
            string=lambda text: text and "window.siteConfig" in text,
        )
        if not site_config_script:
            return None

        match = re.search(r'"recipeId":\s*(\d+)', site_config_script.get_text())
        if not match:
            return None

        recipe_id = match.group(1)
        return recipe_id

    def _get_recipe_json(self):
        recipe_id = self._recipe_id()
        headers = {
            "Host": "mc-api.tecpal.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:149.0) Gecko/20100101 Firefox/149.0",
            "Accept": "*/*",
            "Accept-Language": "fr-FR",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "X-Request-ID": "7cdcec5f-93d3-48b8-9fdf-8d912af36666",
            "x-bypass-cdn": "cd844315-77c4-46ba-83fe-7702d13b12b2",
            "device-type": "web",
            "Origin": "https://www.monsieur-cuisine.com",
            "DNT": "1",
            "Connection": "keep-alive",
            "Referer": "https://www.monsieur-cuisine.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
        }

        # get the json of the request
        response = requests.get(
            f"https://mc-api.tecpal.com/api/v2/recipes/{recipe_id}",
            headers=headers,
        )

        data = json.loads(response.content)
        return data