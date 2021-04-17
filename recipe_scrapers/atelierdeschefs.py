from ._abstract import AbstractScraper


class AtelierDesChefs(AbstractScraper):
    @classmethod
    def host(cls):
        return "atelierdeschefs.fr"

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

    def ratings(self):
        return self.schema.ratings()
