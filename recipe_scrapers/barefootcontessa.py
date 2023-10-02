# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._utils import normalize_string


class BareFootContessa(AbstractScraper):
    @classmethod
    def host(cls):
        return "barefootcontessa.com"

    def author(self):
        return "barefootcontessa.com"

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients = self.soup.find('div', {'class': 'mb-10'}).find('ul', {'class': 'h29'}).find_all('li')
        ingredient_list = [item.text for item in ingredients]
        return ingredient_list

    def instructions(self):
        instructions_div = self.soup.find('div', {'class': 'bd4 mb-10 EntryPost__text a-bc-blue'})
        instructions_paragraphs = instructions_div.find_all('p')

        instructions = []

        for paragraph in instructions_paragraphs:
            if paragraph is not None:
                paragraph_text = normalize_string(paragraph.text)
                instructions.append(paragraph_text)

        return '\n'.join(instructions)
