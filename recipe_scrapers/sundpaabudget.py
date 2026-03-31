from ._abstract import AbstractScraper


class SundPaaBudget(AbstractScraper):
    @classmethod
    def host(cls):
        return "sundpaabudget.dk"

    def description(self):
        # Schema returns empty string
        return self.soup.head.find("meta", {"property": "og:description"})["content"]

    def nutrients(self):
        # Some schema.org nutrition info exists in this site's recipe webpages,
        # but the content seems unreliable
        # Ref: https://github.com/hhursev/recipe-scrapers/issues/1346
        return None
