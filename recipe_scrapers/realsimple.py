from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class RealSimple(AbstractScraper):

    @classmethod
    def host(self):
        return 'realsimple.com'

    def title(self):
        return self.soup.find('h1').get_text(strip=True)

    def total_time(self):
        return get_minutes(self.soup.find('time', {'itemprop': 'totalTime'}))

    def ingredients(self):
        ingredients_html = self.soup.findAll('ol', {'class': "ingredient-list"})[0]

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html.findAll('span', {'itemprop': 'ingredients'})
        ]

    def instructions(self):
        instructions_html = self.soup.find('section', {'itemprop': 'recipeInstructions'})

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html.findAll('li')
        ])
