from ._abstract import AbstractScraper
from ._exceptions import FieldNotProvidedByWebsiteException


class Gourmandize(AbstractScraper):
    @classmethod
    def host(cls):
        return "gourmandize.com"

    def yields(self):
        raise FieldNotProvidedByWebsiteException("Yields not provided by website")

    def title(self):
        return self.soup.find("meta", property="og:title")["content"]
