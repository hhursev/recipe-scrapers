from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class BBCGoodFood(AbstractScraper):

    @classmethod
    def host(self):
        return 'bbcgoodfood.com'

    def title(self):
        return self.soup.find('h1', {'itemprop': 'name'}).get_text()

    def total_time(self):
        time_full = get_minutes(self.soup.find('span', {'class': 'cooking-time-full'}))
        time_prep = get_minutes(self.soup.find('span', {'class': 'cooking-time-prep'}))
        time_cook = get_minutes(self.soup.find('span', {'class': 'cooking-time-cook'}))

        if time_full == 0:
            return time_prep + time_cook
        return time_full

    def ingredients(self):
        ingredients_html = self.soup.find('section', {'id': "recipe-ingredients"}).findAll('li')

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions_html = self.soup.find('section', {'id': 'recipe-method'}).findAll('li')

        instructions_string = '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ])

        if len(instructions_string) == 0:
            instructions_string = normalize_string(
                self.soup.find('section', {'id': 'recipe-method'}).get_text()
            )

        return instructions_string
