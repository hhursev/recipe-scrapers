from ._abstract import AbstractScraper

# from ._consts import TIME_REGEX


class TheVintageMixer(AbstractScraper):

    @classmethod
    def host(self):
        return 'thevintagemixer.com'

    def publisher_site(self):
        return 'http://thevintagemixer.com/'

    def title(self):
        return self.soup.find('div', {'id': 'zlrecipe-title'}).get_text()

    def total_time(self):
        return 0

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'itemprop': "ingredients"})
        return [
            ingredient.get_text().replace('\n', '')
            for ingredient in ingredients_html
            if len(ingredient.get_text().replace('\n', '')) > 0
        ]

    def instructions(self):
        instructions_html = self.soup.findAll('li', {'itemprop': 'recipeInstructions'})
        return '\n'.join(
            [
                instruction.get_text(strip=True).replace('\n', '')
                for instruction in instructions_html
            ])
