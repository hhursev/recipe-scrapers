#!/usr/bin/env python
# encoding: utf-8

from fractions import Fraction
from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class AllRecipes(AbstractScraper):

    @classmethod
    def host(self):
        return 'allrecipes.com'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return {
            'prep-time': get_minutes(self.soup.find('time', {'itemprop': 'prepTime'})),
            'cook-time': get_minutes(self.soup.find('time', {'itemprop': 'totalTime'}))
        }

    def servings(self):
        return self.soup.find('span', {'ng-bind': 'adjustedServings'}).get_text()

    def ingredients(self):

        ingredients_html = self.soup.findAll('span', {'class': "recipe-ingred_txt added"})
        ingredients = []

        for ingredient in ingredients_html:
            ingredient = normalize_string(ingredient.get_text())

            try:
                array = ingredient.split(' ', 2)
                ingredient_dict = {
                    'amount': round(float(sum(Fraction(s) for s in array[0].split())), 3),
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
        instructions_html = self.soup.findAll('span', {'class': 'recipe-directions__list--item'})

        return [
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ]

    def description(self):
        return normalize_string(
            self.soup.find('div', {'class': 'submitter__description'}).get_text()
        )

    def image(self):
        return self.soup.find('img', {'class': 'rec-photo'})["src"]
