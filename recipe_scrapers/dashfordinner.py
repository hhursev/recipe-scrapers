from ._abstract import AbstractScraper


class DashForDinner(AbstractScraper):
    @classmethod
    def host(cls):
        return "dashfordinner.com"
