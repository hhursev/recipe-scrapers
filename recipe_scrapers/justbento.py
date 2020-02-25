from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class JustBento(AbstractScraper):

    @classmethod
    def host(self):
        return 'justbento.com'

    def title(self):
        expected_prefix = 'Recipe: '
        title = self.soup.find(
            'meta',
            {'property': 'og:title', 'content': True}
        )
        return title.get('content').replace(expected_prefix, '')

    def total_time(self):
        time = self.soup.find(
            'div',
            {'class': 'field-name-taxonomy-vocabulary-2'}
        ).find(
            'a',
            {'typeof': 'skos:Concept'}
        )
        return get_minutes(time)

    def yields(self):
        return '1'

    def ingredients(self):
        ingredients = self.soup.find(
            'div',
            {'class': 'field-name-body'}
        ).find('ul').findAll('li')
        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ]

    def instructions(self):
        elements_after_title = self.soup.find(
            'div',
            {'class': 'field-name-body'}
        ).find('h3').find_next_sibling('ul').find_next_siblings()

        instructions = []
        for element in elements_after_title:
            if instructions and element.name != 'p':
                break
            if element.name == 'p':
                instructions.append(element)

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])

    def image(self):
        image = self.soup.find(
            'div',
            {'class': 'field-name-body'}
        ).find(
            'img',
            {'class': 'centerimg', 'src': True}
        )
        return image['src'] if image else None
