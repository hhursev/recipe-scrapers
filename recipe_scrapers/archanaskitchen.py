from ._abstract import AbstractScraper


class ArchanasKitchen(AbstractScraper):

    @classmethod
    def host(self):
        return 'archanaskitchen.com'
