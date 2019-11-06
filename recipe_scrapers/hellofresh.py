import re


from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class HelloFresh(AbstractScraper):

    @classmethod
    def host(self, domain='com'):
        return 'hellofresh.%s' % domain

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return get_minutes(self.soup.find(
            'span',
            {'data-translation-id': "recipe-detail.preparation-time"}
        ).parent.parent)

    def yields(self):
        return get_yields(
            self.soup.find(
                'span',
                {'data-translation-id': "recipe-detail.recipe-detail.serving-amount"}
            ).parent.parent.find_all('button')[0]
        )

    def ingredients(self):
        ingredients_container = self.soup.find(
            'div',
            {'data-test-id': 'recipeDetailFragment.ingredients'}
        )

        ingredients = ingredients_container.findAll('p')

        return [
            ' '.join([
                normalize_string(ingredient_first_part.get_text()),
                normalize_string(ingredient_second_part.get_text())
            ])
            for ingredient_first_part, ingredient_second_part
            in zip(ingredients[0::2], ingredients[1::2])
        ]

    def instructions(self):
        instructions_regex = re.compile('recipeDetailFragment.instructions.step-(\d)')

        instructions_container = self.soup.findAll(
            'div',
            {'data-test-id': instructions_regex}
        )

        instructions = [
            subdiv.findAll('p')
            for subdiv in instructions_container
        ]
        instructions = sum(instructions, [])  # flatten

        return '\n'.join([
            ' '.join([
                str(instruction_order) + ')',
                normalize_string(instruction.get_text())
            ])
            for instruction_order, instruction
            in zip(range(1, len(instructions) + 1), instructions)
        ])
