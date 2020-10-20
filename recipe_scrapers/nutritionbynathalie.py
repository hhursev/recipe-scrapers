import re


from ._abstract import AbstractScraper


BULLET_CHARACTER_ORD = 8226


class NutritionByNathalie(AbstractScraper):
    @classmethod
    def host(cls):
        return "nutritionbynathalie.com"

    def title(self):
        return self.soup.find("h1").get_text()

    def total_time(self):
        return 0

    def yields(self):
        return None

    def image(self):
        try:
            return self.soup.find("img", {"id": re.compile(r"^innercomp_")})["src"]
        except Exception:
            return None

    def ingredients(self):
        ingredients = []

        title = self.soup.find(text="Ingredients:").find_parent("p")
        element = title.nextSibling
        while element:
            ingredient = element.get_text()
            if len(ingredient) == 0 or ord(ingredient[0]) != BULLET_CHARACTER_ORD:
                break
            ingredients.append(ingredient[2:])
            element = element.nextSibling

        return ingredients

    def instructions(self):
        title = self.soup.find(text="Directions:").find_parent("p")

        instructions = []
        for child in title.nextSibling.find_all("li"):
            instructions.append(child.get_text())

        return "\n".join(instructions)

    def ratings(self):
        return None
