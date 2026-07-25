from ._abstract import AbstractScraper


class SundaySupperMovement(AbstractScraper):
    @classmethod
    def host(cls):
        return "sundaysuppermovement.com"

    def instructions(self):
        instructions = []
        container = self.soup.find("div", class_="wprm-recipe-instructions-container")
        if not container:
            return ""

        steps = container.find_all("li", class_="wprm-recipe-instruction")
        for step in steps:
            text_div = step.find("div", class_="wprm-recipe-instruction-text")
            if not text_div:
                continue

            text = text_div.get_text(strip=True)
            if text:
                instructions.append(text)

        return "\n".join(instructions)
