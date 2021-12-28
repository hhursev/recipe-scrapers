from bs4 import BeautifulSoup

from ._abstract import AbstractScraper
from ._utils import normalize_string


class KingArthur(AbstractScraper):
    @classmethod
    def host(cls):
        return "kingarthurbaking.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        schema_instructions = self.schema.instructions()
        soup = BeautifulSoup(schema_instructions, "html.parser")
        instruction_elms = soup.findAll("p")
        return "\n".join([normalize_string(elm.get_text()) for elm in instruction_elms])

    def ratings(self):
        return self.schema.ratings()
