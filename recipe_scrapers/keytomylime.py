from ._abstract import AbstractScraper


class KeyToMyLime(AbstractScraper):
    @classmethod
    def host(cls):
        return "keytomylime.com"
