# mypy: disallow_untyped_defs=False
import re
from typing import Dict, Optional, Tuple, Union
from requests import Session

from ._abstract import AbstractScraper
from ._utils import normalize_string


HEADERS = {
    'Accept-Language': 'nl',  # ah.nl seems to block any requests not having both these headers.
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0'
}


class AlbertHeijn(AbstractScraper):
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

    @classmethod
    def host(cls):
        return "ah.nl"

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

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        instructions = [
            normalize_string(step.get_text())
            # get steps root
            for root in self.soup.findAll(
                "div",
                {"class", re.compile("recipe-preparation-steps_root.*")},
            )
            # get steps
            for step in root.findAll("p")
        ]

        if instructions:
            return "\n".join(instructions)

        # try schema.org
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
