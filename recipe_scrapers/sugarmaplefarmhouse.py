from ._abstract import AbstractScraper


class SugarMapleFarmhouse(AbstractScraper):
    @classmethod
    def host(cls):
        return "sugarmaplefarmhouse.com"
