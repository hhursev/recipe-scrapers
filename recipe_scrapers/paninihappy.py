from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._utils import get_minutes, get_yields, normalize_string


class PaniniHappy(AbstractScraper):
    @classmethod
    def host(cls):
        return "paninihappy.com"

    def site_name(self):
        raise StaticValueException(return_value="Panini Happy®")

    def title(self):
        return self.soup.find("h1", {"class": "entry-title"}).get_text()

    def total_time(self):
        return get_minutes(self.soup.find("span", {"class": "duration"}))

    def yields(self):
        return get_yields(self.soup.find("span", {"class": "yield"}))

    def image(self):
        div_hrecipe = self.soup.find("div", {"class": "hrecipe"})
        if div_hrecipe:
            img_tag = div_hrecipe.find("img", {"loading": "lazy"})
            if img_tag and "src" in img_tag.attrs:
                return img_tag["src"]

    def ingredients(self):
        ingredients = self.soup.findAll("li", {"class": "ingredient"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.findAll("li", {"class": "instruction"})

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
