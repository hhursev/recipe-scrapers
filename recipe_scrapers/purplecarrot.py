from ._abstract import AbstractScraper


class PurpleCarrot(AbstractScraper):
    @classmethod
    def host(cls):
        return "purplecarrot.com"

    def site_name(self):
        home_link = self.soup.find("a", {"href": "/", "title": True})
        if home_link:
            return home_link["title"]
