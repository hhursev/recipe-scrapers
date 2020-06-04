from ._abstract import AbstractScraper


class NYTimes(AbstractScraper):
    
    @classmethod
    def host(self):
        return 'cooking.nytimes.com'
        