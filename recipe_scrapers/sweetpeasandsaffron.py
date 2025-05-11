from ._abstract import AbstractScraper


class SweetPeasAndSaffron(AbstractScraper):
    """
    Web scraper for Sweet Peas & Saffron website
    """

    @classmethod
    def host(cls):
        return "sweetpeasandsaffron.com"
