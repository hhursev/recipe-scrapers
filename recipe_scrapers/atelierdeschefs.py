# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._decorators import opengraph_fallback, schemaorg_fallback


class AtelierDesChefs(AbstractScraper):
    @classmethod
    def host(cls):
        return "atelierdeschefs.fr"

    @schemaorg_fallback
    def author(self):
        pass

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        yields = self.soup.find("option", {"class": "yield"})
        return f"{yields.get('value')} Servings"

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    @opengraph_fallback
    @schemaorg_fallback
    def image(self):
        pass

    def ratings(self):
        return self.schema.ratings()
