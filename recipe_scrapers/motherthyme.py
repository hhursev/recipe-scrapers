from ._abstract import AbstractScraper


class MotherThyme(AbstractScraper):
    @classmethod
    def host(cls):
        return "motherthyme.com"

    def site_name(self):
        home_link = self.soup.find("a", {"rel": "home", "aria-label": True})
        if home_link:
            return home_link["aria-label"]
