from ._abstract import AbstractScraper

"""
    Note that innit hosts recipes for several companies.  I found it while looking at centralmarket.com
"""


class Innit(AbstractScraper):
    @classmethod
    def host(self, domain="com"):
        return f"innit.{domain}"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def nutrients(self):
        return self.schema.nutrients()
