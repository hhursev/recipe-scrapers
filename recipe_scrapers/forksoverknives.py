import re

from ._abstract import AbstractScraper
from ._schemaorg import SchemaOrg
from ._utils import normalize_string


class FOKSchema(SchemaOrg):
    def category(self):
        cat = super().category()
        r = re.compile('.*<a href=".+">(.+)</a>')
        m = r.match(cat)
        if m:
            return normalize_string(m[1])
        return cat


class ForksOverKnives(AbstractScraper):
    @classmethod
    def host(cls):
        return "forksoverknives.com"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = FOKSchema(self.page_data)

    def author(self):
        author = self.soup.find("div", attrs={"class": "post-info"}).find("a")
        return normalize_string(author.get_text())

    def yields(self):
        yields = normalize_string(
            self.soup.find("i", attrs={"class": "icon-serving"}).next_sibling.get_text()
        )
        # Get the first string after "Makes".
        return yields.split(" ", 1)[1]

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
