from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class Yummly(AbstractScraper):

    @classmethod
    def host(self):
        return 'yummly.com'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return get_minutes(
            self.soup.find('div', {'class': 'recipe-summary-item unit'})
        )

    def yields(self):
        return get_yields(
            self.soup.find('div', {'class': 'servings'}).find('input').get('value')
        )

    def ingredients(self):
        ingredients = self.soup.findAll(
            'li',
            {'class': "IngredientLine"}
        )

        return [
            ' '.join([
                normalize_string(span.get_text())
                for span in ingredient.select("""
                    span[class^=amount],
                    span[class^=unit],
                    span[class^=ingredient]""")
            ])
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = self.soup.find('div', attrs={'class': 'directions-wrapper'})
        return '\n'.join([
            normalize_string(instr.get_text())
            for instr in instructions.findAll('span', attrs={'class': 'step'})
        ]) if instructions is not None else ''
