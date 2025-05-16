from ._abstract import AbstractScraper


class VanillaAndBean(AbstractScraper):
    @classmethod
    def host(cls):
        return "vanillaandbean.com"
