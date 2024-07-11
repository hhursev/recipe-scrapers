from ._abstract import AbstractScraper


class SundPaaBudget(AbstractScraper):
    @classmethod
    def host(cls):
        return "sundpaabudget.dk"

    def description(self):
        # Schema returns empty string
        return self.soup.head.find("meta", {"property": "og:description"})["content"]
