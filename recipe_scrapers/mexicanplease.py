from ._abstract import AbstractScraper


class MexicanPlease(AbstractScraper):
    @classmethod
    def host(cls):
        return "mexicanplease.com"
