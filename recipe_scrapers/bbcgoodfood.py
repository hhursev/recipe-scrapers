from ._abstract import AbstractScraper

# from ._consts import TIME_REGEX


class BBCGoodFood(AbstractScraper):

    @classmethod
    def host(self):
        return 'bbcgoodfood.com'

    def publisher_site(self):
        return 'http://bbcgoodfood.com/'

    def title(self):
        return self.soup.find('h1', {'itemprop': 'name'}).get_text()

    def total_time(self):
        return 0

    def ingredients(self):
        ingredients_html = self.soup.find('section', {'id': "recipe-ingredients"}).findAll('li')
        return [
            ingredient.get_text(strip=True)
            for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions_html = self.soup.find('section', {'id': 'recipe-method'}).findAll('li')
        return '\n'.join(
            [
                instruction.get_text(strip=True)
                for instruction in instructions_html
            ])
