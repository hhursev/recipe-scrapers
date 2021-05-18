from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class TheSpruceEats(AbstractScraper):
    @classmethod
    def host(cls):
        return "thespruceeats.com"

    def title(self):
        return self.soup.find("h1", {"class": "heading__title"}).get_text()

    def total_time(self):
        return get_minutes(
            self.soup.find("span", text="Total: ").find_next_sibling(
                "span", {"class": "meta-text__data"}
            )
        )

    def yields(self):
        return (
            self.soup.find("span", text="Servings: ")
            .find_next_sibling("span", {"class": "meta-text__data"})
            .get_text()
        )

    def image(self):
        image = self.soup.find("img", {"class": "primary-image"})
        return image["src"] if image else None

    def ingredients(self):
        # ingredients = self.soup.findAll("li", {"class": "ingredient"})
        ingredients = self.soup.find(
            "section",
            {"class": "comp section--fixed-width section--ingredients section"},
        ).find_all("li", {"class": "structured-ingredients__list-item"})
        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        nested_instructions = self.soup.find(
            "section", {"class": "section--instructions"}
        ).find_all("ol")

        instructions = []
        for each_instruction in nested_instructions:
            instructions = instructions + (each_instruction.find_all("li"))

        return "\n".join(
            [
                normalize_string(instruction.find("p").get_text())
                for instruction in instructions
            ]
        )
