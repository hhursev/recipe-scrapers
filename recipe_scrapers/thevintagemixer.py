from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class TheVintageMixer(AbstractScraper):

    @classmethod
    def host(self):
        return 'thevintagemixer.com'

    def title(self):
        return self.soup.find('div', {'class': 'wprm-recipe-name'}).get_text()

    def total_time(self):
        return get_minutes(self.soup.find('meta', {'itemprop':
            'totalTime'}).parent)

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'itemprop':
            "recipeIngredient"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
            if len(normalize_string(ingredient.get_text())) > 0
        ]

    def instructions(self):
        instructions_html = self.soup.findAll('div', {'itemprop': 'recipeInstructions'})

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ])
