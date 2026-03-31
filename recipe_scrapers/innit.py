from ._abstract import AbstractScraper
from ._exceptions import StaticValueException

"""
    Note that innit hosts recipes for several companies.  I found it while looking at centralmarket.com
"""


class Innit(AbstractScraper):
    @classmethod
    def host(cls, domain="com"):
        return f"innit.{domain}"

    def site_name(self):
        raise StaticValueException(return_value="Innit")
