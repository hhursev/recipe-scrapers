from ._abstract import AbstractScraper


class AtelierDesChefs(AbstractScraper):
    @classmethod
    def host(cls):
        return "atelierdeschefs.fr"

    def yields(self):
        yields = self.soup.find("option", {"class": "yield"})
        return f"{yields.get('value')} Servings"
