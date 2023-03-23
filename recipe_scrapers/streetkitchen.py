# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import get_yields, normalize_string


class StreetKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "streetkitchen.hu"

    def title(self):
        return self.soup.find("h1", {"class": "entry-title"}).get_text()

    def total_time(self):
        return None

    def image(self):
        return (
            self.soup.find("div", {"class": "article-featured-image-bg"})
            .find("noscript")
            .find("img")["src"]
        )

    def ingredients(self):
        ingredients_raw = self.soup.findAll("dd")
        ingredients = []
        # There are separate sets of ingredients for desktop and mobile view
        for ingredient in ingredients_raw[: int(len(ingredients_raw) / 2)]:
            ingredients.append(normalize_string(ingredient.get_text()).strip())
        return ingredients

    def instructions(self):
        instructions = self.soup.find("div", {"class": "the-content-div"}).findAll("p")

        instructions_arr = []
        for instruction in instructions:
            text = instruction.get_text()
            # From the point we encounter "If you liked..." it's just ads.
            if text.startswith("Ha tetszett a"):
                break
            instructions_arr.append(normalize_string(text))

        return "\n".join(instructions_arr)

    def yields(self):
        return get_yields(
            self.soup.find("span", {"class": "quantity-number"}).get_text()
        )
