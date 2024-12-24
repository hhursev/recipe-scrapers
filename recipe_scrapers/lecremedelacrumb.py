from ._abstract import AbstractScraper


class LeCremeDeLaCrumb(AbstractScraper):
    @classmethod
    def host(cls):
        return "lecremedelacrumb.com"
