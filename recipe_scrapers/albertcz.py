from ._abstract import AbstractScraper


class AlbertCz(AbstractScraper):
    @classmethod
    def host(cls):
        return "albert.cz"

    def author(self):
        return "Albert"

    def site_name(self):
        return "Albert"

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
        instructions = self.schema.instructions()

        filtered = [
            line
            for line in instructions.split("\n")
            if not line.strip().endswith(".") or not line.strip()[:-1].isdigit()
        ]

        return "\n".join(filtered)

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        meta = self.soup.find("meta", {"name": "description"})
        if meta:
            return meta.get("content")
        return self.schema.description()
