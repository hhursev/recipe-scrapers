from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class FoodNetwork(AbstractScraper):

    @classmethod
    def host(self):
        return 'foodnetwork.com'

    def title(self):
        return self.soup.find('h1').get_text().strip()

    def total_time(self):
        return get_minutes(self.soup.find(
            'span',
            {'class': 'm-RecipeInfo__a-Description--Total'})
        )

    def yields(self):
        return get_yields(self.soup.find(
            'ul',
            {'class': 'o-RecipeInfo__m-Yield'}
        ).find(
            'span',
            {'class': 'o-RecipeInfo__a-Description'}
        ))

    def ingredients(self):
        ingredients = self.soup.findAll(
            'p',
            {'class': 'o-Ingredients__a-Ingredient'}
        )

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = self.soup.findAll(
            'li',
            {'class': 'o-Method__m-Step'}
        )

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
            if instruction.get_text(strip=True) not in ('Watch how to make this recipe.', )
        ])
