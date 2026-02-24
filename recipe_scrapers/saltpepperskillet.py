from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class SaltPepperSkillet(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "saltpepperskillet.com"

    def author(self):
        return self.schema.author().title()
