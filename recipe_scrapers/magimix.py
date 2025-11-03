from ._abstract import AbstractScraper


class Magimix(AbstractScraper):
    @classmethod
    def host(cls):
        return "magimix.com"

    def instructions(self):
        instructions = []
        for step in self.soup.select("div.recipe-steps-content div.recipe-step"):
            title = step.select_one("div.recipe-step-title")
            if title:
                step_number = title.select_one("span.step-number")
                if step_number:
                    step_number.extract()
                text = title.get_text(strip=True)
                if text:
                    instructions.append(text)
        return "\n".join(instructions)
