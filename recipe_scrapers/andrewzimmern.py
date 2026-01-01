from ._abstract import AbstractScraper


class AndrewZimmern(AbstractScraper):
    @classmethod
    def host(cls):
        return "andrewzimmern.com"

    def ingredients(self):
        ingredients = []
        ingredient_elements = self.soup.select("div.ingredients_list li")
        for li in ingredient_elements:
            ingredient = li.get_text(strip=True)
            ingredients.append(ingredient)
        return ingredients

    def instructions(self):
        instruction_paragraphs = self.soup.select("div.preparation p")
        instructions = [p.get_text(strip=True) for p in instruction_paragraphs]
        return "\n".join(instructions)
