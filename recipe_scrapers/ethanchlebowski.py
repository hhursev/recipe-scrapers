from ._abstract import AbstractScraper


class EthanChlebowski(AbstractScraper):
    @classmethod
    def host(cls):
        return "ethanchlebowski.com"

    def ratings(self):
        return None

    def cuisine(self):
        return None

    def description(self):
        return self.soup.head.find("meta", {"property": "og:description"})["content"]
