# mypy: allow-untyped-defs

import requests

from ._abstract import AbstractScraper


class QuiToque(AbstractScraper):
    def __init__(self, url, proxies=None, timeout=None, *args, **kwargs):
        super().__init__(url=url, proxies=proxies, timeout=timeout, *args, **kwargs)
        recipe_id = url.split("/")[4]
        data_url = "https://mgs.quitoque.fr/graphql"
        data_body = {
            "operationName": "getRecipe",
            "variables": {"id": recipe_id},
            "query": "query getRecipe($id:ID!){\nrecipe(id:$id){\nname\nshortDescription\nfacets{\nname\n}\nimage\nnutritionalInformations{\nkiloCalorie\nfat\nsaturatedFat\ncarbohydrate\nsugarCarbohydrate\nfiber\nprotein\nsalt\n}\nfacets{\nname\n}\npools{\nnbPerson\ncookingModes{\ncookingTime\nsteps{\ndescription\n}\nstacks{\ntools{\nname\n}\ncupboardIngredients{\nquantity\nliteralQuantity\nproduct{\nname\n}\n}\ningredients{\nliteralQuantity\nquantity\nproduct{\nname\n}\n}\n}\nwaitingTime\n}\n}\n}\n}",
        }
        self.data = requests.post(
            data_url,
            json=data_body,
            proxies=proxies,
            timeout=timeout,
        ).json()["data"]

    @classmethod
    def host(cls):
        return "quitoque.fr"

    def title(self):
        return self.data["recipe"]["name"]

    def category(self):
        categories = ""
        for category in self.data["recipe"]["facets"]:
            categories += f'{category["name"]}, '
        return categories[:-2]

    def total_time(self):
        return self.data["recipe"]["pools"][0]["cookingModes"][0]["waitingTime"]

    def yields(self):
        return f'{self.data["recipe"]["pools"][0]["nbPerson"]} portions'

    def image(self):
        return self.data["recipe"]["image"]

    def ingredients(self):
        ingredients = []
        stacks = self.data["recipe"]["pools"][0]["cookingModes"][0]["stacks"]
        for ingredient in stacks["ingredients"]:
            if ingredient["quantity"] > 0:
                ingredients.append(
                    f'{ingredient["literalQuantity"]} {ingredient["product"]["name"]}'
                )
            else:
                ingredients.append(ingredient["product"]["name"])
        for cupboard_ingredients in stacks["cupboardIngredients"]:
            if cupboard_ingredients["quantity"] > 0:
                ingredients.append(
                    f'{cupboard_ingredients["literalQuantity"]} {cupboard_ingredients["product"]["name"]}'
                )
            else:
                ingredients.append(cupboard_ingredients["product"]["name"])
        return ingredients

    def instructions(self):
        instruction = ""
        steps = self.data["recipe"]["pools"][0]["cookingModes"][0]["steps"]
        for step in steps:
            instruction += step["description"].replace("\r", "").replace("\xa0", " ")
        return instruction

    def nutrients(self):
        nutritional_informations = self.data["recipe"]["nutritionalInformations"][0]
        nutrients = {
            "calories": f'{nutritional_informations["kiloCalorie"]} calories',
            "fatContent": f'{nutritional_informations["fat"]} grammes',
            "saturatedFatContent": f'{nutritional_informations["saturatedFat"]} grammes',
            "carbohydrateContent": f'{nutritional_informations["carbohydrate"]} grammes',
            "sugarContent": f'{nutritional_informations["sugarCarbohydrate"]} grammes',
            "fiberContent": f'{nutritional_informations["fiber"]} grammes',
            "proteinContent": f'{nutritional_informations["protein"]} grammes',
            "sodiumContent": f'{nutritional_informations["salt"]} grammes',
        }
        return nutrients

    def equipment(self):
        equipments = []
        tools = self.data["recipe"]["pools"][0]["cookingModes"][0]["stacks"]["tools"]
        for tool in tools:
            equipments.append(tool["name"])
        return equipments

    def description(self):
        return self.data["recipe"]["shortDescription"]
