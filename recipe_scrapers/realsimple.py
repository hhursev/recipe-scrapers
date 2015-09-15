from ._abstract import AbstractScraper

from .consts import TIME_REGEX, HTML_SYMBOLS


class RealSimple(AbstractScraper):

    @classmethod
    def host(self):
        return 'realsimple.com'

    def publisher_site(self):
        return 'http://realsimple.com/'

    def title(self):
        return self.soup.find('h1').get_text(strip=True)

    def total_time(self):
        time = self.soup.find('time', {'itemprop': 'totalTime'}).get_text()
        matched = TIME_REGEX.search(time)

        total_minutes = 0
        if matched is not None and matched.group('hours') is not None:
            total_minutes += 60 * int(matched.group('hours'))
        if matched is not None and matched.group('minutes') is not None:
            total_minutes += int(matched.group('minutes'))

        return total_minutes

    def ingredients(self):
        ingredients_html = self.soup.findAll('ol', {'class': "ingredient-list"})[0]

        return [
            ingredient.get_text(strip=True)
            for ingredient in ingredients_html.findAll('span', {'itemprop': 'ingredients'})
        ]

    def instructions(self):
        directions_html = self.soup.find('section', {'itemprop': 'recipeInstructions'})

        return '\n'.join(
            [
                direction.get_text(strip=True)
                for direction in directions_html.findAll('li')
            ])
