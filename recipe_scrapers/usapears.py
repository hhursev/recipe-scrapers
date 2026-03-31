import re

from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml
from ._grouping_utils import group_ingredients
from ._utils import get_minutes, normalize_string


class USAPears(AbstractScraper):
    @classmethod
    def host(cls):
        return "usapears.org"

    def author(self):
        author = self.schema.author()
        if author:
            return author

        d1 = self.soup.find("meta", {"name": "twitter:data1", "content": True})
        l1 = self.soup.find("meta", {"name": "twitter:label1", "content": "Written by"})
        if d1 and l1:
            return d1["content"]

    def total_time(self):
        total_time = 0
        recipe_legends = self.soup.find_all("div", {"class": "recipe-legend"})
        for recipe_legend in recipe_legends:
            if recipe_legend.get_text() in ["Prep Time", "Cook Time"]:
                total_time += get_minutes(
                    recipe_legend.parent.find("div", {"class": "recipe-value-data"})
                )
        return total_time

    def ingredients(self):
        ingredient_elements = self.soup.select(
            'li[itemprop="ingredients"]:not(:has(strong))'
        )

        return [
            normalize_string(paragraph.get_text().strip())
            for paragraph in ingredient_elements
        ]

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            'li[itemprop="ingredients"] strong',
            'li[itemprop="ingredients"]:not(:has(strong))',
        )

    def nutrients(self):
        container = self.soup.find("ul", {"itemprop": "nutrition"})
        if not container:
            raise ElementNotFoundInHtml("Could not find nutritional info container")

        results = {}
        redundant_pattern = r"<strong>(.+)[:] </strong>"
        for item in container.find_all("li", {"itemprop": True}):
            nutrient = item["itemprop"]
            content = "".join(str(elem) for elem in item.children)
            if re.match(redundant_pattern, content):
                content = re.sub(redundant_pattern, "", content)
            results[nutrient] = content

        corrections = {
            "carbohydrates": "carbohydrateContent",
            "protein": "proteinContent",
            "fat": "fatContent",
        }
        for mistake, correction in corrections.items():
            if mistake in results:
                results[correction] = results.pop(mistake)

        return results

    def ratings(self):
        rating_elements = self.soup.find_all("p", {"class": "comment-rating"})
        if not rating_elements:
            return None

        total_rating = 0
        for element in rating_elements:
            img = element.find("img", {"src": True})
            if not img:
                continue
            match = re.search(r"(\d+)-star\.svg", img["src"])
            if match:
                total_rating += int(match.group(1))

        if len(rating_elements) > 0:
            return round(total_rating / len(rating_elements), 2)
        return None
