from ._abstract import AbstractScraper
from ._exceptions import StaticValueException


class Cybercook(AbstractScraper):
    @classmethod
    def host(cls):
        return "cybercook.com.br"

    def site_name(self):
        raise StaticValueException(return_value="CyberCook")
