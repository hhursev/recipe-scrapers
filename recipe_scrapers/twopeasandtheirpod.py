from ._abstract import AbstractScraper

from .consts import TIME_REGEX


class TwoPeasAndTheirPod(AbstractScraper):

    @classmethod
    def host(self):
        return 'twopeasandtheirpod.com'

    def publisher_site(self):
        return 'http://twopeasandtheirpod.com/'

    def title(self):
        return self.soup.find('h2').get_text()

    def total_time(self):
        time = self.soup.find('span', {'class': 'duration'})
        total_minutes = 0
        if time is not None:
            matched = TIME_REGEX.search(time.get_text())
            if matched is not None and matched.group('hours'):
                total_minutes += 60 * int(matched.group('hours'))
            if matched is not None and matched.group('minutes'):
                total_minutes += int(matched.group('minutes'))

        return total_minutes

    def ingredients(self):
        ingredients_html = self.soup.find('div', {'class': 'ingredient'}).findAll('p')
        ingredients_flatten = []
        for ingredient in ingredients_html:
            ingredients_flatten.extend(ingredient.get_text().split('\n'))

        return [
            ingredient for ingredient in ingredients_flatten
            if ingredient[0].isdigit()
        ]

    def instructions(self):
        return self.soup.find('div', {'class': 'instructions'}).get_text()

    def social_rating(self):
        # always 100 for twopeasandtheirpod
        return 100
