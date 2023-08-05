from ._abstract import AbstractScraper


class SaltPepperSkillet(AbstractScraper):
    @classmethod
    def host(cls):
        return "saltpepperskillet.com"

    def title(self):
        return self.schema.title()

    def author(self):
        author = self._extract_author()
        return author if author else self.schema.title()

    def _extract_author(self):
        author_tag = self.soup.find("div", {"class": "sps-publish-date-wrap"})

        if author_tag:
            author_link = author_tag.find("a", href=lambda x: x and "author" in x)
            if author_link:
                author_name = author_link.get_text()
                return author_name

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
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
