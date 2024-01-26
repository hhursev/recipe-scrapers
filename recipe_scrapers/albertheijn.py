# mypy: disallow_untyped_defs=False
import re

from ._abstract import AbstractScraper
from ._utils import normalize_string
from ._schemaorg import SchemaOrg

import requests
from bs4 import BeautifulSoup

HEADERS = {
    'Accept-Language': 'nl',  # ah.nl seems to block any requests not having both these headers.
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0'
}


class AlbertHeijn(AbstractScraper):
    def __init__(self, url, proxies=None, timeout=None, *args, **kwargs):
        assert url is not None, "url required for fetching recipe data"
        resp = requests.get(
            url,
            headers=HEADERS,
            proxies=proxies,
            timeout=timeout,
        )
        self.page_data = resp.content
        self.url = resp.url
        self.soup = BeautifulSoup(self.page_data, "html.parser")
        self.schema = SchemaOrg(self.page_data)

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
