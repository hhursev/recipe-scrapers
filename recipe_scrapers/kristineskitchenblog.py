from ._abstract import AbstractScraper


class KristinesKitchenBlog(AbstractScraper):
    @classmethod
    def host(cls):
        return "kristineskitchenblog.com"
