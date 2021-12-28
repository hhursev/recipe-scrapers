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
        """
        King Arthur updated how they format their instructions to include html (instructions wrapped in <p>) in the
        `recipeInstructions`, parse the instructions assuming each step is wrapped in a <p> first, and fallback to just
        returning the schema instructions in case this is changed, again.
        """
        schema_instructions = self.schema.instructions()
        soup = BeautifulSoup(schema_instructions, "html.parser")
        instruction_elms = soup.findAll("p")
        if instruction_elms:
            return "\n".join(
                [normalize_string(elm.get_text()) for elm in instruction_elms]
            )
        return schema_instructions

    def ratings(self):
        return self.schema.ratings()
