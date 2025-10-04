from ._abstract import AbstractScraper


class SimpleHomeEdit(AbstractScraper):
    @classmethod
    def host(cls):
        return "simplehomeedit.com"

    def instructions(self):
        instructions = []
        instruction_lists = self.soup.select("div.tasty-recipes-instructions ol")
        for ol in instruction_lists:
            steps = ol.select("li")
            for step in steps:
                text = step.get_text(strip=True)
                if text:
                    instructions.append(text)
        return "\n".join(instructions)
