from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class FineDiningLovers(AbstractScraper):

    @classmethod
    def host(self):
        return 'finedininglovers.com'

    def title(self):
        return self.soup.find(
            'h3',
            {'itemprop': 'name'}
        ).get_text()

    def total_time(self):
        return get_minutes(self.soup.find(
            'time',
            {'itemprop': 'prepTime'})
        )


    def yields(self):
        return get_yields(self.soup.find(
            'span',
            {'itemprop': 'recipeYield'})
        )

    def ingredients(self):
        ingredients = self.soup.findAll(
            'li',
            {'itemprop': "ingredients"}
        )

        return [
            normalize_string(ingredient.find('a').get_text())
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = self.soup.findAll(
            'div',
            {'itemprop': 'recipeInstructions'}
        )

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])
