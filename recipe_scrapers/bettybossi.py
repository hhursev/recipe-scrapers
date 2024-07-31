from typing import Dict, Optional, Tuple, Union

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
        proxies: Optional[
            Dict[str, str]
        ] = None,  # allows us to specify optional proxy server
        timeout: Optional[
            Union[float, Tuple[float, float], Tuple[float, None]]
        ] = None,  # allows us to specify optional timeout for request
        wild_mode: Optional[bool] = False,
        html: Union[str, bytes, None] = None,
    ) -> None:
        if html is None:
            with Session() as session:
                session.proxies.update(proxies or {})
                session.headers.update(HEADERS)

                session.get(url, timeout=timeout)
                html = session.get(url, timeout=timeout).content  # reload the page

        # As the html content is provided, the parent will not query the page
        super().__init__(url, proxies, timeout, wild_mode, html)
