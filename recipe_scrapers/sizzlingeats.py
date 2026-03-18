from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class SizzlingEats(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "sizzlingeats.com"

    def instructions(self):
        instructions = self.soup.find_all(
            "div", {"class": "wprm-recipe-instruction-text"}
        )
        return "\n".join([instruction.get_text() for instruction in instructions])
