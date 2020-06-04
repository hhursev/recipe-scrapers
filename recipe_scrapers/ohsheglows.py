from ._abstract import AbstractScraper


class OhSheGlows(AbstractScraper):
    
    @classmethod
    def host(self):
        return 'ohsheglows.com'
        