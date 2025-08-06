from ._abstract import AbstractScraper


class MyVegetarianRoots(AbstractScraper):
    @classmethod
    def host(cls):
        return "myvegetarianroots.com"
