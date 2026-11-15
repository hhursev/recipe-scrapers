from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class TudoReceitas(AbstractScraper):
    @classmethod
    def host(cls):
        return "tudoreceitas.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredientes .ingrediente.titulo",
            ".ingredientes .ingrediente:not(.titulo)",
        )
