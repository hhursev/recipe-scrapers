from html import unescape

from ._abstract import AbstractScraper
from ._schemaorg import SchemaOrg


class KitchenStories(AbstractScraper):
    @classmethod
    def host(cls):
        return "kitchenstories.com"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Workaround: kitchenstories has some unusual HTML escaping going on
        # within their on-page schema.org metadata.  Retrieve it and unescape
        # the content so that we can retrieve values from it.
        # Ref: https://github.com/hhursev/recipe-scrapers/issues/562
        schema_data = self.soup.find("script", {"type": "application/ld+json"})
        schema_data = unescape(str(schema_data))
        self.schema = SchemaOrg(schema_data)

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def cook_time(self):
        return self.schema.cook_time()

    def prep_time(self):
        return self.schema.prep_time()

    def image(self):
        return self.schema.image()

    def nutrients(self):
        return self.schema.nutrients()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def author(self):
        return self.schema.author()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
