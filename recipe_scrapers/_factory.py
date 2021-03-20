from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_host_name


class SchemaScraperFactory:
    class SchemaScraper(AbstractScraper):
        def host(self) -> str:
            return get_host_name(self.url)

        def title(self) -> Optional[str]:
            return self.schema.title()

        def total_time(self) -> Optional[int]:
            return self.schema.total_time()

        def yields(self) -> Optional[str]:
            return self.schema.yields()

        def image(self) -> Optional[str]:
            return self.schema.image()

        def ingredients(self) -> Optional[List[str]]:
            return self.schema.ingredients()

        def instructions(self) -> Optional[str]:
            return self.schema.instructions()

        def ratings(self) -> Optional[float]:
            return self.schema.ratings()

        def author(self) -> Optional[str]:
            return self.schema.author()

        def cuisine(self) -> Optional[str]:
            return self.schema.cuisine()

    @classmethod
    def generate(cls, url, **options):
        return cls.SchemaScraper(url, **options)
