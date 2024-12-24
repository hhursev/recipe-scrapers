from ._abstract import AbstractScraper


class ComidinhasDoChef(AbstractScraper):
    @classmethod
    def host(cls):
        return "comidinhasdochef.com"
