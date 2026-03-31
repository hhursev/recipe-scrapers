from ._abstract import AbstractScraper


class SoMuchFoodBlog(AbstractScraper):
    @classmethod
    def host(cls):
        return "somuchfoodblog.com"
