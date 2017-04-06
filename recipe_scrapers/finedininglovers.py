#!/usr/bin/env python
# encoding: utf-8
from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class FineDiningLovers(AbstractScraper):

    @classmethod
    def host(self):
        return 'finedininglovers.com'

    def title(self):
        return self.soup.find('h3', {'itemprop': 'name'}).get_text()

    def total_time(self):
        return get_minutes(self.soup.find('time', {'itemprop': 'prepTime'}))

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'itemprop': "ingredients"})

        return [
            normalize_string(ingredient.find('a').get_text())
            for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions_html = self.soup.findAll('div', {'itemprop': 'recipeInstructions'})

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ])
