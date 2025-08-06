from ._abstract import AbstractScraper


class Vegolosi(AbstractScraper):
    @classmethod
    def host(cls):
        return "vegolosi.it"

    def title(self):
        return self.soup.h1.get_text().strip()
