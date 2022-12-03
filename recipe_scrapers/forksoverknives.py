# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import normalize_string
from ._schemaorg import SchemaOrg
from typing import Dict, List, Optional, Tuple, Union
import re


class fok_Schema(SchemaOrg):
    def __init__(self, page_data, raw=False):
        super().__init__(page_data)

    def category(self):
        cat = super().category()
        r = re.compile('.*<a href="\S+">(.*)</a>')
        m = r.match(cat)
        if m:
            return normalize_string(m[1])
        return cat


class ForksOverKnives(AbstractScraper):
    @classmethod
    def host(cls):
        return "forksoverknives.com"

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
        super().__init__(
            url=url, proxies=proxies, timeout=timeout, wild_mode=wild_mode, html=html
        )
        self.schema = fok_Schema(self.page_data)

    def author(self):
        author = self.soup.find("div", attrs={"class": "post-info"}).find("a")
        return normalize_string(author.get_text())

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        yields = normalize_string(
            self.soup.find("i", attrs={"class": "icon-serving"}).next_sibling.get_text()
        )
        # Get the first string after "Makes".
        return yields.split(" ", 1)[1]

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        ratings = normalize_string(
            self.soup.find("div", attrs={"class": "headline"})
            .find("span", attrs={"class": "rated-count"})
            .get_text()
        )
        # Unwrap parens
        ratings = ratings[1:]
        # return the first element
        return float(ratings.split()[0])
