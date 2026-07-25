from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class AdrianasBestRecipes(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "adrianasbestrecipes.com"

    def instructions(self):
        instructions = []
        instruction_groups = self.soup.select("div.wprm-recipe-instruction-group")
        for group in instruction_groups:
            steps = group.select("li.wprm-recipe-instruction")
            for step in steps:
                text = step.get_text(strip=True)
                if text:
                    instructions.append(text)
        return "\n".join(instructions)
