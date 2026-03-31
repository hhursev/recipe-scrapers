from ._abstract import AbstractScraper
from ._utils import normalize_string


class SimplyRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "simplyrecipes.com"

    def instructions(self):
        steps = self.soup.find(
            "div", {"class": "structured-project__steps"}
        ).ol.find_all("li")

        return "\n".join(
            [
                normalize_string(
                    step.div.text + "".join([p.text for p in step.find_all("p")])
                )
                for step in steps
            ]
        )
