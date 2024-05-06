# mypy: allow-untyped-defs
import json

import requests

from ._abstract import HEADERS, AbstractScraper
from ._utils import get_minutes, get_url_slug, get_yields


class Youfoodz(AbstractScraper):

    def __init__(self, url, proxies=None, timeout=None, *args, **kwargs):
        super().__init__(url=url, *args, **kwargs)

        # Access token is returned in the original HTML
        access_token = self._get_access_token()
        # Access token needed for the API call
        self.data = self._get_recipe_data(
            access_token, proxies=proxies, timeout=timeout
        )

    @classmethod
    def host(cls):
        return "youfoodz.com"

    def author(self):
        author_meta = self.soup.find("meta", {"name": "author"})
        if not author_meta:
            return "Youfoodz"
        return author_meta.get("content")

    def title(self):
        name = self.data["name"]
        headline = self.data.get("headline")
        if not headline:
            return name
        return name + " " + headline

    def category(self):
        return self.data["category"]["name"]

    def prep_time(self):
        time = self.data.get("prepTime")
        return get_minutes(time)

    def total_time(self):
        time = self.data.get("totalTime")
        return get_minutes(time)

    def yields(self):
        yields = self.data["yields"][0]["yields"]
        return get_yields(str(yields))

    def image(self):
        return self.data["imageLink"]

    def ingredients(self):
        ingredients = self.data.get("ingredients", [])
        return [ingredient["name"] for ingredient in ingredients]

    def instructions(self):
        steps = self.data.get("steps", [])
        return "\n".join([step["instructions"].strip() for step in steps])

    def cuisine(self):
        cuisines = self.data.get("cuisines", [])
        return ", ".join([cuisine["name"] for cuisine in cuisines])

    def description(self):
        return self.data["description"]

    def ratings(self):
        return self.data.get("averageRating", 0)

    def ratings_count(self):
        return self.data.get("ratingsCount", 0)

    def nutrients(self):
        calories = self._find_nutrient("Calories")
        fat_content = self._find_nutrient("Fat")
        saturated_content = self._find_nutrient("of which saturates")
        carbohydrate_content = self._find_nutrient("Carbohydrate")
        sugar_content = self._find_nutrient("of which sugars")
        fiber_content = self._find_nutrient("Dietary Fibre")
        protein_content = self._find_nutrient("Protein")
        sodium_content = self._find_nutrient("Sodium")

        return {
            "calories": calories,
            "fatContent": fat_content,
            "saturatedContent": saturated_content,
            "carbohydrateContent": carbohydrate_content,
            "sugarContent": sugar_content,
            "fiberContent": fiber_content,
            "proteinContent": protein_content,
            "sodiumContent": sodium_content,
        }

    def language(self):
        return super().language()

    def _get_access_token(self):
        json_script = self.soup.find("script", {"id": "__NEXT_DATA__"})
        json_data = json.loads(json_script.text)
        return json_data["props"]["pageProps"]["ssrPayload"]["serverAuth"][
            "access_token"
        ]

    def _get_recipe_data(self, access_token, proxies=None, timeout=None):
        recipe_slug = get_url_slug(self.url)
        recipe_id = recipe_slug.split("-")[-1]

        response = requests.get(
            f"https://www.youfoodz.com/gw/recipes/recipes/{recipe_id}",
            headers={**HEADERS, "Authorization": f"Bearer {access_token}"},
            proxies=proxies,
            timeout=timeout,
        )

        return response.json()

    def _find_nutrient(self, target_name):
        nutrition = self.data.get("nutrition")

        for entry in nutrition:
            name = entry.get("name")
            if name == target_name:
                amount = entry["amount"]
                unit = entry["unit"]
                return f"{amount}{unit}"

        return None
