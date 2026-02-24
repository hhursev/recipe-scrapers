from ._abstract import AbstractScraper
from ._utils import normalize_string


class PastificioSorrentino(AbstractScraper):
    @classmethod
    def host(cls):
        return "pastificiosorrentino.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def site_name(self):
        return "Pastificio Sorrentino"

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
        # The schema parser might miss 'HowtoStep' due to case sensitivity.
        # Fallback to scraping the instruction list from the HTML directly.
        instructions = self.schema.instructions()
        if not instructions:
            instruction_items = self.soup.select(".come-preparare li")
            instructions = "\n".join(
                [normalize_string(item.get_text()) for item in instruction_items]
            )
        return instructions

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
