from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup
from ._utils import normalize_string


class Dishnz(AbstractScraper):
    @classmethod
    def host(cls):
        return "dish.co.nz"

    def author(self):
        return normalize_string(
            self.soup.find("span", itemprop="author").find("i").text.strip()
        )

    def title(self):
        return normalize_string(self.soup.find("h1").text)

    def category(self):
        return None

    def total_time(self):
        return None

    def yields(self):
        return normalize_string(
            self.soup.find("div", {"class": "sub-description-block"}).find("h2").text
        )

    def image(self):
        return "https://{}{}".format(
            self.host(), self.soup.find("img", itemprop="image").attrs["src"]
        )

    def ingredients(self):
        ingredients = []
        for ingredient in self.soup.find("div", itemprop="ingredients").find("p"):
            txt = normalize_string(ingredient.text)
            if txt and ingredient.name != "strong":
                ingredients.append(txt)
        return ingredients

    def ingredient_groups(self):
        group = self.soup.find("div", itemprop="ingredients").find("p")
        output = []
        index = -1
        for element in group.contents:
            if element.name == "strong":  # new section
                output.append(
                    IngredientGroup(
                        ingredients=[], purpose=normalize_string(element.text)
                    )
                )
                index += 1
            else:
                txt = normalize_string(element.text)
                if txt:
                    output[index].ingredients.append(txt)

        return output

    def instructions(self):
        instruction_list = []
        instructions = self.soup.find("div", {"class": "recipe"}).find_all("p")
        for instruction in instructions:
            instruction_list.append(normalize_string(instruction.text))
        return "\n".join(instruction_list)

    def ratings(self):
        return None

    def cuisine(self):
        return None

    def description(self):

        return normalize_string(
            self.soup.find("div", {"class": "article-header__group2"})
            .find("div")
            .find("p")
            .text.strip()
        )
