from ._abstract import AbstractScraper

"""
    Note that innit hosts recipes for several companies.  I found it while looking at centralmarket.com
"""


class Innit(AbstractScraper):
    @classmethod
    def host(self, domain="com"):
        return f"innit.{domain}"
