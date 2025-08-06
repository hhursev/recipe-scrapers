from ._abstract import AbstractScraper


class MyJewishLearning(AbstractScraper):
    @classmethod
    def host(cls):
        return "myjewishlearning.com"
