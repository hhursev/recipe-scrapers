from ._abstract import AbstractScraper


class Migusto(AbstractScraper):
    @classmethod
    def host(cls):
        return "migusto.migros.ch"

    def image(self):
        return self.soup.find("meta", {"property": "og:image"})["content"]
