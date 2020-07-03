from ._abstract import AbstractScraper


class ArchanasKitchen(AbstractScraper):

    @classmethod
    def host(cls):
        return 'archanaskitchen.com'
