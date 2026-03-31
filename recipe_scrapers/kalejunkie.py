from ._abstract import AbstractScraper


class KaleJunkie(AbstractScraper):
    @classmethod
    def host(cls):
        return "kalejunkie.com"

    def instructions(self):
        instructions = self.soup.find_all(
            "div", {"class": "wprm-recipe-instruction-text"}
        )

        return "\n".join([instruction.get_text() for instruction in instructions])
