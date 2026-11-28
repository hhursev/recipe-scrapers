from ._abstract import AbstractScraper
from ._utils import normalize_string


class DagelijkseKost(AbstractScraper):
    @classmethod
    def host(cls):
        return "dagelijksekost.vrt.be"

    def instructions(self):
        container = self.soup.select_one('[data-testid="instructions-web"]')
        return "\n".join(
            normalize_string(step.get_text())
            for step in container.select(
                '[data-testid="recipe-instruction"] p'
            )
        )
