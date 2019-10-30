from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class WhatsGabyCooking(AbstractScraper):

    @classmethod
    def host(self):
        return 'whatsgabycooking.com'

    def title(self):
        return self.soup.find(
            'h1',
            {'class': 'entry-title'}
        ).get_text()

    def total_time(self):
        return get_minutes(self.soup.find(
            'p',
            {'class': 'header-recipe-time'})
        )

    def yields(self):
        return ""

    def ingredients(self):
        ingredients = self.soup.findAll(
            'li',
            {'class': "wprm-recipe-ingredient"}
        )

        retStr = []
        for m in ingredients:
            retStr.append(m.text.strip())

        return retStr

    def image(self):
        return ""

    def instructions(self):
        instructions = self.soup.findAll(
            'div',
            {'class': 'wprm-recipe-instruction-text'}
        )

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])
