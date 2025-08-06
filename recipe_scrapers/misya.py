from ._abstract import AbstractScraper
from ._exceptions import StaticValueException


class Misya(AbstractScraper):
    @classmethod
    def host(cls):
        return "misya.info"

    def site_name(self):
        raise StaticValueException(return_value="Ricette di Misya")
