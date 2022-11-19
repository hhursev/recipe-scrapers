from __future__ import annotations

from ._abstract import AbstractScraper
from ._utils import get_host_name


class SchemaScraperFactory:
    class SchemaScraper(AbstractScraper):
        def host(self) -> str:  # type: ignore [override]
            return get_host_name(self.url) if self.url is not None else ""

        def title(self) -> str | None:
            return self.schema.title()

        def category(self) -> str | None:
            return self.schema.category()

        def total_time(self) -> float | None:
            return self.schema.total_time()

        def cook_time(self) -> float | None:
            return self.schema.cook_time()

        def prep_time(self) -> float | None:
            return self.schema.prep_time()

        def yields(self) -> str | None:
            return self.schema.yields()

        def image(self) -> str | None:
            return self.schema.image()

        def ingredients(self) -> list[str]:
            return self.schema.ingredients()

        def instructions(self) -> str:
            return self.schema.instructions()

        def ratings(self) -> float | None:
            return self.schema.ratings()

        def author(self) -> str | None:
            return self.schema.author()

        def cuisine(self) -> str | None:
            return self.schema.cuisine()

        def description(self) -> str | None:
            return self.schema.description()

    @classmethod
    def generate(
        cls,
        url: str | None,
        proxies: dict[str, str] | None = None,
        timeout: float | tuple[float, float] | tuple[float, None] | None = None,
        wild_mode: bool | None = None,
        html: str | bytes | None = None,
    ) -> SchemaScraper:
        return cls.SchemaScraper(
            url,
            proxies,
            timeout,
            wild_mode,
            html,
        )
