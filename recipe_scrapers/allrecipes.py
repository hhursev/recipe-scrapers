from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class AllRecipes(AbstractScraper):

    @classmethod
    def host(self):
        return 'allrecipes.com'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return get_minutes(self.soup.find('span', {'class': 'ready-in-time'}))

    def prep_time(self):
        return get_minutes(self.soup.find('time', {'itemprop': 'cookTime'}))

    def cook_time(self):
        return get_minutes(self.soup.find('time', {'itemprop': 'prepTime'}))

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'class': "checkList__line"})

        return [
            normalize_string(ingredient.get_text().replace("ADVERTISEMENT", ""))
            for ingredient in ingredients_html
            if ingredient.get_text(strip=True) not in ('Add all ingredients to list', '', 'ADVERTISEMENT')
        ]

    def instructions(self):
        instructions_html = self.soup.findAll('span', {'class': 'recipe-directions__list--item'})

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ])

    def footnotes(self):
        footnotes_html_container = self.soup.find('section', {'class': 'recipe-footnotes'})
        if footnotes_html_container is None:
            return ""
        footnotes_html = footnotes_html_container.findAll('li')

        return '\n'.join([
            normalize_string(footnote.get_text())
            for footnote in footnotes_html
            if footnote.get_text(strip=True) not in ('Tip', 'Editor\'s Note')
        ])

    def photo_url(self):
        return self.soup.find('img', {'class': 'rec-photo'})['src']

    def review_count(self):
        return int(self.soup.find('meta', {'itemprop': 'reviewCount'})['content'])

    def rating_stars(self):
        return float(self.soup.find('meta', {'itemprop': 'ratingValue'})['content'])
