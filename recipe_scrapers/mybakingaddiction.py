from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class MyBakingAddiction(AbstractScraper):

    @classmethod
    def host(self):
        return 'mybakingaddiction.com'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return get_minutes(self.soup.find('meta', {'itemprop': 'prepTime'}).parent) +\
            get_minutes(self.soup.find('meta', {'itemprop': 'cookTime'}).parent)

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'itemprop': "ingredients"})
        ingredients_html += self.soup.find('div', {'class': 'ingredients'}).get_text().split('\n')

        return [
            ingredient for ingredient in set([
                normalize_string(ingredient.get_text()) if type(ingredient) != str else ingredient
                for ingredient in ingredients_html
                if ingredient != ''
            ])
        ]

    def instructions(self):
        instructions_html = self.soup.find('span', {'itemprop': 'recipeInstructions'}).findAll(['li', 'p'])

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ])
