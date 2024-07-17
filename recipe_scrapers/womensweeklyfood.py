import re

from ._abstract import AbstractScraper


class WomensWeeklyFood(AbstractScraper):
    @classmethod
    def host(cls):
        return "womensweeklyfood.com.au"

    def instructions(self):
        return re.sub(r"\d+\.\n", "", self.schema.instructions())
