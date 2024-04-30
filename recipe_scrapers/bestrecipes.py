# mypy: allow-untyped-defs

import warnings

from ._abstract import AbstractScraper


class BestRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "bestrecipes.com.au"

    def language(self):
        msg = (
            f"{self.host()} doesn't seem to provide language metadata in their HTML. "
            "Please let us know if it becomes available in a standard location, "
            "and then we can try to retrieve it dynamically."
        )
        warnings.warn(msg)
        return "en-AU"
