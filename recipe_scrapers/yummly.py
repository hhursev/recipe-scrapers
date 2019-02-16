from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string
import json


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

    def ingredients(self):
        ingredients = self.soup.findAll(
            'li',
            {'class': "IngredientLine"}
        )
        ingredients_data = []
        for ingredient in ingredients:
            # Add if amount found
            amount = ingredient.find('span', {'class': 'amount'})
            amount_str = normalize_string(amount.get_text()) if amount else ''
            # Add if unit found
            unit = ingredient.find('span', {'class': 'unit'})
            unit_str = ' {}'.format(normalize_string(unit.get_text())) if unit else ''
            # Add if ingredient name found
            ingredient_name = ingredient.find('span', {'class': 'ingredient'})
            ingredient_name_str = ' {}'.format(normalize_string(ingredient_name.get_text())) if ingredient_name else ''

            ingredients_data.append(
                '{amount}{unit}{ingredient_name}'.format(
                    amount=amount_str, unit=unit_str, ingredient_name=ingredient_name_str,
                )
            )

        return ingredients_data

    def instructions(self):
        # Yummly does not provide instructions on it's page. It has a link that redirects to original website.
        return ''
