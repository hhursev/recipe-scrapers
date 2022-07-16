from ._abstract import AbstractScraper


class EthanChlebowski(AbstractScraper):
    @classmethod
    def host(cls):
        return "ethanchlebowski.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return None

    def cuisine(self):
        return None

    def description(self):
        return self.soup.head.find("meta", {"property": "og:description"})["content"]
