from ._abstract import AbstractScraper
from ._utils import normalize_string


class JamieOliver(AbstractScraper):
    @classmethod
    def host(cls):
        return "jamieoliver.com"

    def instructions(self):
        method_heading = self.soup.find("h2", string="Method")
        instructions_list = method_heading.find_next("ol")
        instructions = instructions_list.find_all("li")
        return "\n".join([normalize_string(inst.get_text()) for inst in instructions])
