from ._abstract import AbstractScraper


class FineDiningLovers(AbstractScraper):
    @classmethod
    def host(cls):
        return "finedininglovers.com"

    def site_name(self):
        home_link = self.soup.find("a", {"rel": "home", "href": "/", "title": True})
        if home_link:
            return home_link["title"]
