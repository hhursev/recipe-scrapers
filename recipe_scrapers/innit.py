# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper

"""
    Note that innit hosts recipes for several companies.  I found it while looking at centralmarket.com
"""


class Innit(AbstractScraper):
    @classmethod
    def host(cls, domain="com"):
        return f"innit.{domain}"

    def nutrients(self):
        return self.schema.nutrients()
