from recipe_scrapers._abstract import AbstractScraper


class SchemaScraperFactory:
    class SchemaScraper(AbstractScraper):
        @classmethod
        def host(cls):
            return None

        def title(self):
            return self.schema.title()

        def total_time(self):
            return self.schema.total_time()

        def yields(self):
            return self.schema.yields()

        def image(self):
            return self.schema.image()

        def ingredients(self):
            return self.schema.ingredients()

        def instructions(self):
            self.schema.instructions()

        def ratings(self):
            return self.schema.ratings()

        def author(self):
            return self.schema.author()

        def cuisine(self):
            return self.schema.cuisine()

    @classmethod
    def generate(cls, url):
        return cls.SchemaScraper(url)
