# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class BestRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "bestrecipes.com.au"

    def language(self):
        return "en-AU"
