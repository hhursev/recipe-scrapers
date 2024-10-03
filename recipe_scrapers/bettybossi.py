from __future__ import annotations

from requests import Session

from ._abstract import HEADERS, AbstractScraper


class BettyBossi(AbstractScraper):
    """Scrape BettyBossi.ch recipes."""

    @classmethod
    def host(cls):
        return "bettybossi.ch"

    def site_name(self):
        """Self-titled website"""
        return self.author()

    def __init__(
        self,
        url: str,
        proxies: (
            dict[str, str] | None
        ) = None,  # allows us to specify optional proxy server
        timeout: (
            float | tuple[float, float] | tuple[float, None] | None
        ) = None,  # allows us to specify optional timeout for request
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
