# mypy: disallow_untyped_defs=False
import re
import inspect
from typing import Dict, Optional, Tuple, Union

from ._abstract import AbstractScraper
from ._utils import normalize_string
from ._schemaorg import SchemaOrg

from recipe_scrapers.settings import settings

import requests
from bs4 import BeautifulSoup

HEADERS = {
    'Accept-Language': 'nl',  # ah.nl seems to block any requests not having both these headers.
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0'
}


class AlbertHeijn(AbstractScraper):
    def __init__(
        self,
        url: Union[str, None],
        proxies: Optional[
            Dict[str, str]
        ] = None,  # allows us to specify optional proxy server
        timeout: Optional[
            Union[float, Tuple[float, float], Tuple[float, None]]
        ] = None,  # allows us to specify optional timeout for request
        wild_mode: Optional[bool] = False,
        html: Union[str, bytes, None] = None,
    ):
        if html:
            self.page_data = html
            self.url = url
        else:
            assert url is not None, "url required for fetching recipe data"
            resp = requests.get(
                url,
                headers=HEADERS,
                proxies=proxies,
                timeout=timeout,
            )
            self.page_data = resp.content
            self.url = resp.url

        self.wild_mode = wild_mode
        self.soup = BeautifulSoup(self.page_data, "html.parser")
        self.schema = SchemaOrg(self.page_data)

        # attach the plugins as instructed in settings.PLUGINS
        if not hasattr(self.__class__, "plugins_initialized"):
            for name, _ in inspect.getmembers(self, inspect.ismethod):
                current_method = getattr(self.__class__, name)
                for plugin in reversed(settings.PLUGINS):
                    if plugin.should_run(self.host(), name):
                        current_method = plugin.run(current_method)
                setattr(self.__class__, name, current_method)
            setattr(self.__class__, "plugins_initialized", True)

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
