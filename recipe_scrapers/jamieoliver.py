# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import normalize_string


class JamieOliver(AbstractScraper):
    @classmethod
    def host(cls):
        return "jamieoliver.com"

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.catimageegory()

    def instructions(self):
        instructions = self.soup.find("ol", {"class": "recipeSteps"}).findAll("li")
        return "\n".join([normalize_string(inst.get_text()) for inst in instructions])
