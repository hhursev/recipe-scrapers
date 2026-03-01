import logging

from ._abstract import AbstractScraper
from ._utils import get_host_name
from typing import Optional

logging.basicConfig()
logger = logging.getLogger(__name__)

class SchemaScraperFactory:
    class SchemaScraper(AbstractScraper):
        def host(self) -> str:  # type: ignore [override]
            return get_host_name(self.url) if self.url is not None else ""

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

        def description(self):
            return self.schema.description()

    class OpenGraphScraper(AbstractScraper):
        def host(self) -> str:  # type: ignore [override]
            return get_host_name(self.url) if self.url is not None else ""

        def title(self):
            try:
                return self.opengraph.title()
            except:
                return ""

        def description(self):
            try:
                return self.opengraph.description()
            except:
                return ""

        def image(self):
            try:
                return self.opengraph.image()
            except:
                return ""

        def category(self):
            return ""

        def total_time(self):
            return ""

        def cook_time(self):
            return ""

        def prep_time(self):
            return ""

        def yields(self):
            return ""

        def ingredients(self):
            return ""

        def instructions(self):
            return ""

        def ratings(self):
            return ""

        def author(self):
            return ""

        def cuisine(self):
            return ""

    @classmethod
    def generate(cls, html, url,
                 best_image: Optional[bool] = None,
                 simple_opengraph: Optional[bool] = None):
        schema_scraper = cls.SchemaScraper(html=html, url=url, best_image=best_image)
        if schema_scraper.schema.data or not simple_opengraph:
            return schema_scraper

        logger.info(
            "The website seems not to have schema.org metadata. Attempting to return simple info from OpenGraph."
        )
        return cls.OpenGraphScraper(html=html, url=url)

