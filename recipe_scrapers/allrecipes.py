from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class AllRecipes(AbstractScraper):

    @classmethod
    def host(self):
        return 'allrecipes.com'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return get_minutes(self.soup.find(
            'span',
            {'class': 'ready-in-time'})
        )

    def yields(self):
        return get_yields(self.soup.find(
            'meta',
            {
                'id': 'metaRecipeServings',
                'itemprop': 'recipeYield'
            }).get("content"))

    def image(self):
        image = self.soup.find(
            'img',
            {'class': 'rec-photo', 'src': True}
        )
        return image['src'] if image else None

    def ingredients(self):
        ingredients = self.soup.findAll(
            'li',
            {'class': "checkList__line"}
        )

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
            if ingredient.get_text(strip=True) not in (
                'Add all ingredients to list',
                '',
                'ADVERTISEMENT'
            )
        ]

    def instructions(self):
        instructions = self.soup.findAll(
            'span',
            {'class': 'recipe-directions__list--item'}
        )

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])

    def ratings(self):
        rating = self.soup.find("meta", {"property": "og:rating"})
        rating = round(float(rating['content']), 2) if rating and rating['content'] else -1.0
        return rating
