from recipe_scrapers._exceptions import SchemaOrgException
from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_yields, normalize_string


class Festligare(AbstractScraper):
    @classmethod
    def host(cls):
        return "festligare.se"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        try:
            category = self.schema.category()
            if category:
                return category
        except SchemaOrgException:
            pass

        breadcrumb_tags = self.soup.find(
            itemtype="https://schema.org/BreadcrumbList"
        ).find_all(itemtype="https://schema.org/ListItem")
        if len(breadcrumb_tags) > 1:
            # The last breadcrumb is the recipe, the second to last the category
            return normalize_string(breadcrumb_tags[-2].get_text())

    def keywords(self):
        try:
            keywords = self.schema.keywords()
            if keywords:
                return keywords
        except SchemaOrgException:
            pass

        keyword_tags = self.soup.find(class_="ArticleContent-categories").find_all(
            class_="ArticleContent-categoryItem"
        )
        return [normalize_string(tag.get_text()) for tag in keyword_tags]

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        try:
            return self.schema.yields()
        except SchemaOrgException:
            pass

        details_item_tags = self.soup.find_all(class_="Hero-detailsItem")
        yields_tags = [
            tag
            for tag in details_item_tags
            if tag.find(class_="Hero-detailsItemTitle").get_text() == "Antal"
        ]
        if yields_tags:
            return get_yields(
                yields_tags[0].find(class_="Hero-detailsItemValue").get_text()
            )

        return None

    def image(self):
        return self.schema.image()

    def ingredients(self):
        try:
            ingredients = self.schema.ingredients()
            if ingredients:
                return ingredients
        except SchemaOrgException:
            pass

        ingredient_tags = self.soup.find(class_="Recipe-ingredientsContent").find_all(
            itemprop="recipeIngredient"
        )
        return [normalize_string(tag.get_text()) for tag in ingredient_tags]

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ArticleContent .Recipe-ingredientsContent h4",
            '.ArticleContent li[itemprop="recipeIngredient"]',
        )

    def instructions(self):
        try:
            instructions = self.schema.instructions()
            if instructions:
                return instructions
        except SchemaOrgException:
            pass

        instruction_tags = self.soup.find(itemprop="recipeInstructions").find_all(
            itemtype="http://schema.org/HowToStep"
        )
        return "\n".join([normalize_string(tag.get_text()) for tag in instruction_tags])

    def ratings(self):
        try:
            return self.schema.ratings()
        except SchemaOrgException:
            pass
        rating_tag = self.soup.find(itemprop="ratingValue")
        if rating_tag:
            return round(float(rating_tag.get("content")), 2)
        return None

    def ratings_count(self):
        try:
            return self.schema.ratings_count()
        except SchemaOrgException:
            pass
        rating_count_tag = self.soup.find(itemprop="reviewCount")
        if rating_count_tag:
            return float(rating_count_tag.get("content"))
        return None

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
