from ._abstract import AbstractScraper


class SipAndFeast(AbstractScraper):
    @classmethod
    def host(cls):
        return "sipandfeast.com"
