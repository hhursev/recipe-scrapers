from ._abstract import AbstractScraper


class TasteAndTellBlog(AbstractScraper):
    @classmethod
    def host(cls):
        return "tasteandtellblog.com"
