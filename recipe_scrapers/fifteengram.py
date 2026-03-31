from ._abstract import AbstractScraper


class FifteenGram(AbstractScraper):
    @classmethod
    def host(cls):
        return "15gram.be"

    def canonical_url(self):
        return self.soup.find("meta", {"property": "og:url"}).get("content")

    def author(self):
        return "15gram"
