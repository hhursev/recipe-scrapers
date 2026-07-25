from ._abstract import AbstractScraper


class LetsCampSmore(AbstractScraper):
    @classmethod
    def host(cls):
        return "letscampsmore.com"
