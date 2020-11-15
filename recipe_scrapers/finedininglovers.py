from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class FineDiningLovers(AbstractScraper):
    @classmethod
    def host(cls):
        return "finedininglovers.com"

    def title(self):
        return self.soup.find("div", {"class": "recipe-detail"}).find("h3").get_text()

    def total_time(self):
        return get_minutes(self.soup.find("div", {"class": "timing"}))

    def yields(self):
        yields = self.soup.find(
            "div", {"class": "field--name-field-recipe-serving-num"}
        )

        return get_yields("{} servings".format(yields))

    def ingredients(self):
        ingredients_parent = self.soup.find("div", {"class": "ingredients-box"})
        ingredients = ingredients_parent.findAll(
            "div", {"class": "paragraph--type--recipe-ingredient"}
        )

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions_parent = self.soup.find(
            "div", {"class": "field--name-field-recipe-para-steps"}
        )
        instructions = instructions_parent.findAll(
            "div", {"class": "paragraph--type--recipe-step"}
        )

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def image(self):
        image = self.soup.select_one(".image-zone picture img")
        image_url = image["data-src"].split("?")[0]
        image_base_url = "https://www.finedininglovers.com"

        return "{}{}".format(image_base_url, image_url) if image else None
