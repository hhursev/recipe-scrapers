from ._abstract import AbstractScraper
from ._utils import normalize_string


class ComidinhasDoChef(AbstractScraper):
    @classmethod
    def host(cls):
        return "comidinhasdochef.com"

    def author(self):
        return self.soup.find("span", {"class": "theauthor"}).get_text(strip=True)

    def title(self):
        return self.soup.find("h1", {"class": "title"}).get_text()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        yields = self.soup.find("span", {"itemprop": "recipeYield"})
        return yields.get_text() if yields else None

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return [
            normalize_string(ingredient.get_text())
            for ingredient in self.soup.find_all("li", {"itemprop": "recipeIngredient"})
        ]

    def instructions(self):
        instructions = [
            normalize_string(instruction.get_text(strip=True))
            for instruction in self.soup.find_all(
                "li", {"itemprop": "recipeInstructions"}
            )
        ]
        return "\n".join(instructions)

    def ratings(self):
        rating = self.soup.find("span", {"itemprop": "ratingValue"}).get_text()
        return round(float(rating), 2)
