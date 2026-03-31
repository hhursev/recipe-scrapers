from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class ThePlantBasedSchool(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "theplantbasedschool.com"

    def instructions(self):
        return "\n".join(
            span.get_text()
            for instruction in self.soup.select(".wprm-recipe-instruction-text")
            for span in instruction.find_all("span", recursive=False)
        )
