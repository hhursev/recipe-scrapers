# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import get_host_name


class SchemaScraperFactory:
    class SchemaScraper(AbstractScraper):
        def host(self) -> str:  # type: ignore [override]
            return get_host_name(self.url) if self.url is not None else ""

        def cook_time(self):
            return self.schema.cook_time()

        def prep_time(self):
            return self.schema.prep_time()

        def cuisine(self):
            return self.schema.cuisine()

        def description(self):
            return self.schema.description()

    @classmethod
    def generate(cls, url, **options):
        return cls.SchemaScraper(url, **options)
