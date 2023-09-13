# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class TudoGostoso(AbstractScraper):
    @classmethod
    def host(cls):
        return "tudogostoso.com.br"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()
