from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml


class SimpleHomeEdit(AbstractScraper):
    @classmethod
    def host(cls):
        return "simplehomeedit.com"

    def instructions(self):
        instructions = []
        for li in self.soup.select(
            "div.wprm-recipe-instructions-container li.wprm-recipe-instruction"
        ):
            text = li.get_text(" ", strip=True)
            if text:
                instructions.append(text)

        if not instructions:
            raise ElementNotFoundInHtml("Could not find instructions.")

        return "\n".join(instructions)
