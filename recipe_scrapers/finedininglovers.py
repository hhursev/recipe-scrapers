# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class FineDiningLovers(AbstractScraper):
    @classmethod
    def host(cls):
        return "finedininglovers.com"

    def _is_article(self):
        """
        helper method to determine how the current page is structured - we handle 'recipe' and 'article' pages differently
        """
        return "finedininglovers.com/article/" in self.canonical_url()

    def title(self):
        if self._is_article():
            return self.soup.find("div", {"class": "title"}).find("h1").get_text()
        return self.soup.find("h1", {"class": "recipe-full-class"}).get_text()

    def total_time(self):
        if self._is_article():
            return None
        return get_minutes(self.soup.find("div", {"class": "timing"}))

    def yields(self):
        if self._is_article():
            return None

        yields = self.soup.find(
            "div", {"class": "field--name-field-recipe-serving-num"}
        )
        return get_yields("{} servings".format(yields))

    def ingredients(self):
        if self._is_article():
            return (
                []
            )  # ingredients in articles are just normal text and cant be extracted
        ingredients_parent = self.soup.find("div", {"class": "ingredients-box"})
        ingredients = ingredients_parent.findAll(
            "div", {"class": "paragraph--type--recipe-ingredient"}
        )

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        if self._is_article():
            return self.soup.find("div", {"class": "field--name-body"}).get_text()

        instructions_parent = self.soup.find(
            "div", {"class": "field--name-field-recipe-para-steps"}
        )

        if instructions_parent is not None:
            instructions = instructions_parent.findAll(
                "div", {"class": "paragraph--type--recipe-step"}
            )
        else:
            instructions_parent = self.soup.find("div", {"class": "ante-body"})
            instructions = instructions_parent.findAll({"li", "p"})

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def image(self):
        image = self.soup.select_one(".image-zone picture img")
        image_url = image["data-src"].split("?")[0]
        image_base_url = "https://www.finedininglovers.com"

        return "{}{}".format(image_base_url, image_url) if image else None
