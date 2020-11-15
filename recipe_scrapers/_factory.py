from ._abstract import AbstractScraper
from ._utils import get_host_name


class SchemaScraperFactory:
    class SchemaScraper(AbstractScraper):
        def host(self):
            return get_host_name(self.url)

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
            return self.schema.instructions()

        def ratings(self):
            return self.schema.ratings()

        def author(self):
            return self.schema.author()

        def cuisine(self):
            return self.schema.cuisine()

    @classmethod
    def generate(cls, url, **options):
        return cls.SchemaScraper(url, **options)
