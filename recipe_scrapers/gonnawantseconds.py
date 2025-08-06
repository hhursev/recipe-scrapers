from ._abstract import AbstractScraper


class GonnaWantSeconds(AbstractScraper):
    @classmethod
    def host(cls):
        return "gonnawantseconds.com"
