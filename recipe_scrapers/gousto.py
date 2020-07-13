from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class Gousto(AbstractScraper):
    @classmethod
    def host(cls):
        return "gousto.co.uk"

    def title(self):
        return self.soup.find("h1", {"class": "indivrecipe-title"}).get_text()

    def total_time(self):
        return get_minutes(
            self.soup.find("p", {"class": "recipehighlight-box-value"}).parent
        )

    def yields(self):
        yields = (
            self.soup.find("div", {"id": "ingredients"})
            .find("div", {"class": "panel-subheading"})
            .get_text()
        )

        return get_yields("{} servings".format(yields))

    def ingredients(self):
        # TODO: Fix append
        container = self.soup.find("div", {"id": "ingredients"})

        ingredients = container.find_all(
            "figcaption", {"class": "indivrecipe-ingredients-text"}
        )

        extras = (
            container.find("div", {"class": "panel indivrecipe-panel"})
            .find("div", {"class": "panel-subheading"})
            .get_text()
        )

        extras = extras.strip().split(", ")

        ingredients = [
            normalize_string(ingredient.get_text()) for ingredient in ingredients
        ]

        for extra in extras:
            ingredients.append(extra)

        return ingredients

    def instructions(self):
        instructions = self.soup.find("div", {"id": "instructions"}).find_all(
            "div", {"class": "indivrecipe-cooking-text-wrapper"}
        )

        instr_container = [
            p.get_text() for subdiv in instructions for p in subdiv.findAll("p")
        ]

        return "\n".join(
            normalize_string(instruction) for instruction in instr_container
        )

    def ratings(self):
        ratings = self.soup.find("div", {"class": "star-overflow"}).find(
            "img", alt=True
        )

        rating = int(ratings["alt"][0])

        return rating
