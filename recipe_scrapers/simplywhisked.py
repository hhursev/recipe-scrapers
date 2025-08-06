from ._abstract import AbstractScraper


class SimplyWhisked(AbstractScraper):
    @classmethod
    def host(cls):
        return "simplywhisked.com"
