from ._abstract import AbstractScraper

from ._consts import TIME_REGEX


class JamieOliver(AbstractScraper):

    @classmethod
    def host(self):
        return 'jamieoliver.com'

    def publisher_site(self):
        return 'http://jamieoliver.com/'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        # jamieoliver has awfully written site (but recipes are good)
        tds = self.soup.findAll('td', {'valign': 'top'})
        tds_text = [td.get_text(strip=True) for td in tds]

        total_minutes = 0
        for text in tds_text:
            matched = TIME_REGEX.search(text)
            if matched is not None:
                total_minutes += 60 * int(matched.groupdict().get('hours') or 0)
                total_minutes += int(matched.groupdict().get('minutes') or 0)

        return total_minutes

    def ingredients(self):
        article = self.soup.find('article', {'class', 'ingredients'})
        ingredients_html = article.findAll('li')
        return [
            ingredient.get_text(strip=True)
            for ingredient in ingredients_html
        ]

    def instructions(self):
        directions_html = self.soup.find('p', {'class': 'instructions'})
        return directions_html.get_text()
