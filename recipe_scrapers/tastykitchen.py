#!/usr/bin/env python
# encoding: utf-8
from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class TastyKitchen(AbstractScraper):

    @classmethod
    def host(self):
        return 'tastykitchen.com'

    def title(self):
        return self.soup.find('h1', {'itemprop': 'name'}).get_text()

    def total_time(self):
        return get_minutes(self.soup.find('time', {'itemprop': 'prepTime'})) +\
               get_minutes(self.soup.find('time', {'itemprop': 'cookTime'}))

    def ingredients(self):
        ingredients_html = self.soup.find('ul', {'class': "ingredients"}).findAll('li')

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
        ]

    def instructions(self):
        directions_html = self.soup.find('span', {'itemprop': 'instructions'}).findAll('p')

        return '\n'.join([
            normalize_string(direction.get_text())
            for direction in directions_html
        ])
