from ._abstract import AbstractScraper
from ._exceptions import FieldNotProvidedByWebsiteException


class OwenHan(AbstractScraper):
    @classmethod
    def host(cls):
        return "owen-han.com"

    def author(self):
        return self.soup.find("span", {"class": "author-name"}).get_text()

    def title(self):
        return self.soup.find("h1", {"class": "entry-title"}).text

    def total_time(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def ingredients(self):
        return [x for x in map(lambda x: x.text, self.soup.select("ul > li"))]

    def instructions_list(self):
        return [x for x in map(lambda x: x.text, self.soup.select("ol > li"))]

    def instructions(self):
        return "\n".join(self.instructions_list())
