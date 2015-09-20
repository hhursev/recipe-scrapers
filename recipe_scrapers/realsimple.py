from ._abstract import AbstractScraper

from ._consts import TIME_REGEX


class RealSimple(AbstractScraper):

    @classmethod
    def host(self):
        return 'realsimple.com'

    def publisher_site(self):
        return 'http://realsimple.com/'

    def title(self):
        return self.soup.find('h1').get_text(strip=True)

    def total_time(self):
        try:
            time = self.soup.find('time', {'itemprop': 'totalTime'}).get_text()
            matched = TIME_REGEX.search(time)
            if matched is None:
                raise AttributeError

            total_minutes = int(matched.groupdict().get('minutes') or 0)
            total_minutes += 60 * int(matched.groupdict().get('hours') or 0)

            return total_minutes

        except AttributeError:  # when there is no span or no time regex match
            return 0

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
