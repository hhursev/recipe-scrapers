from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class FoodNetwork(AbstractScraper):

    @classmethod
    def host(self):
        return 'foodnetwork.com'

    def title(self):
        return self.soup.find('h1').get_text().strip()

    def total_time(self):
        return get_minutes(self.soup.find(
            'dd',
            {'class': 'o-RecipeInfo__a-Description--Total'})
        )

    def ingredients(self):
        ingredients = self.soup.findAll(
            'li',
            {'class': 'o-Ingredients__a-ListItem'}
        )

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = self.soup.find(
            'div',
            {'class': 'o-Method__m-Body'}
        ).findAll('p')

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
            if instruction.get_text(strip=True) not in ('Watch how to make this recipe.', )
        ])
