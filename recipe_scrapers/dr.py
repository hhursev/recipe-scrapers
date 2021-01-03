from ._abstract import AbstractScraper


class Dr(AbstractScraper):
    @classmethod
    def host(cls):
        return "dr.dk"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def language(self):
        meta_language = self.soup.find(
            "meta",
            attrs={"name": lambda x: x and x.lower() == "language", "content": True},
        )

        return meta_language.get("content")

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()
