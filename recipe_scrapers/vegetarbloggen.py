from ._abstract import AbstractScraper
from ._exceptions import StaticValueException


class Vegetarbloggen(AbstractScraper):
    @classmethod
    def host(cls):
        return "vegetarbloggen.no"

    def site_name(self):
        raise StaticValueException(return_value="Vegetarbloggen")

    def instructions(self):
        return self.schema.instructions().strip()
