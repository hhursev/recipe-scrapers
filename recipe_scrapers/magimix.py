from ._abstract import AbstractScraper


class Magimix(AbstractScraper):
    @classmethod
    def host(cls):
        return "magimix.com"

    def instructions(self):
        steps = [
            step.get_text(strip=True)
            for step in self.soup.select("div.recipe-steps-content div.recipe-step")
            if step.get_text(strip=True)
        ]
        return "\n".join(steps)
