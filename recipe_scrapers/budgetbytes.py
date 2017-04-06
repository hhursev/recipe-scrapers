#!/usr/bin/env python
# encoding: utf-8

import unicodedata
from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class BudgetBytes(AbstractScraper):

    @classmethod
    def host(self):
        return 'budgetbytes.com'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return {
            'prep-time': get_minutes(self.soup.find('time', {'itemprop': 'prepTime'})),
            'cook-time': get_minutes(self.soup.find('time', {'itemprop': 'cookTime'}))
        }

    def servings(self):
        return self.soup.find('span', {'itemprop': 'recipeYield'}).get_text()

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'class': 'ingredient'})
        ingredients = []

        for ingredient in ingredients_html:
            ingredient = normalize_string(ingredient.get_text())
            ingredient = ingredient.split(' $', 1)[0]

            try:
                array = ingredient.split(' ', 2)
                ingredient_dict = {
                    'amount': round(unicodedata.numeric(array[0]), 3),
                    'type': array[1],
                    'title': array[2]
                }
            except:
                ingredient_dict = {
                    'title': ingredient
                }

            ingredients.append(ingredient_dict)

        return ingredients

    def instructions(self):
        instructions_html = self.soup.findAll('li', {'class': 'instruction'})

        return [
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ]

    def description(self):
        li = self.soup.find('div', {'class': 'entry-content'}).findAll('p')
        return li[0].get_text()

    def image(self):
        return self.soup.find('img', {'itemprop': 'image'})["src"]
