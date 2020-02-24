from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class AllRecipes(AbstractScraper):

    @classmethod
    def host(self):
        return 'allrecipes.com'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        total_time = 0

        total_time = get_minutes(self.soup.find(
            'span',
            {'class': 'ready-in-time'})
        )

        if not total_time:
            total_time_node = [
                node.parent()
                for node in self.soup.findAll(
                    'div',
                    {'class': 'recipe-meta-item-header'}
                )
                if 'total' in node.get_text()
            ][0]

            if total_time_node:
                total_time = get_minutes(total_time_node[1].get_text())

        return total_time

    def yields(self):
        recipe_yield = self.soup.find(
            'meta', {'itemprop': 'recipeYield'}
        )
        if recipe_yield:
            return get_yields(recipe_yield.get("content"))
        else:
            return get_yields(self.soup.find(
                'div',
                {'class': 'recipe-adjust-servings__original-serving'}
            ).get_text())

    def image(self):
        image = self.soup.find(
            'img',
            {'class': 'rec-photo', 'src': True}
        )
        if image is None:
            image = self.soup.find('div', {'class': 'lead-media'})
            return image['data-src'] if image else None

        return image['src'] if image else None

    def ingredients(self):
        ingredients = self.soup.findAll(
            'li',
            {'class': "checkList__line"}
        )

        if not ingredients:
            ingredients = self.soup.findAll(
                'span',
                {'class': 'ingredients-item-name'}
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

        if not instructions:
            instructions = self.soup.findAll(
                'li',
                {'class': 'instructions-section-item'}
            )

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])

    def ratings(self):
        rating = (
            self.soup.find("meta", {"property": "og:rating"}) or
            self.soup.find("meta", {"name": "og:rating"})
        )
        rating = round(float(rating['content']), 2) if rating and rating['content'] else -1.0
        return rating
