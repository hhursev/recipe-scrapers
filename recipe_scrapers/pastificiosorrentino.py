from ._abstract import AbstractScraper
from ._utils import normalize_string


class PastificioSorrentino(AbstractScraper):
    @classmethod
    def host(cls):
        return "pastificiosorrentino.com"

    def site_name(self):
        return "Pastificio Sorrentino"

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
