from __future__ import annotations

from requests import Session

from ._abstract import HEADERS, AbstractScraper

# mypy: disallow_untyped_defs=False


class BettyBossi(AbstractScraper):
    """Scrape BettyBossi.ch recipes.

    This scraper is particular as the website implements a refresh after
    loading the page the first time. It is therefore needed to do two get
    requests in a single session, once to initialize the connection, the second
    to load the page content.
    """

    @classmethod
    def host(cls):
        return "bettybossi.ch"

    def __init__(
        self,
        url: str,
        proxies: dict[str, str]
        | None = None,  # allows us to specify optional proxy server
        timeout: float
        | tuple[float, float]
        | tuple[float, None]
        | None = None,  # allows us to specify optional timeout for request
        wild_mode: bool | None = False,
        html: str | bytes | None = None,
    ) -> None:
        if html is None:
            with Session() as session:
                session.proxies.update(proxies or {})
                session.headers.update(HEADERS)

                session.get(url, timeout=timeout)
                html = session.get(url, timeout=timeout).content  # reload the page

        # As the html content is provided, the parent will not query the page
        super().__init__(url, proxies, timeout, wild_mode, html)

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

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

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
