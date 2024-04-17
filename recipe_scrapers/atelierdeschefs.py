# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class AtelierDesChefs(AbstractScraper):
    @classmethod
    def host(cls):
        return "atelierdeschefs.fr"

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        yields = self.soup.find("option", {"class": "yield"})
        return f"{yields.get('value')} Servings"

    def ratings(self):
        return self.schema.ratings()
