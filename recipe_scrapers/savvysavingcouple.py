from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class SavvySavingCouple(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "savvysavingcouple.net"

    def instructions(self):
        instructions = self.soup.find_all(
            "div", {"class": "wprm-recipe-instruction-text"}
        )
        return "\n".join([instruction.get_text() for instruction in instructions])
