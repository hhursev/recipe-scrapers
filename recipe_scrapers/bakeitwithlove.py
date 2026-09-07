from ._abstract import AbstractScraper


class BakeItWithLove(AbstractScraper):
    @classmethod
    def host(cls):
        return "bakeitwithlove.com"

    def instructions(self):
        instruction_elements = self.soup.select(".wprm-recipe-instruction-text")
        instructions = [
            element.get_text(" ", strip=True) for element in instruction_elements
        ]
        return "\n".join(instructions)
