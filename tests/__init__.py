import unittest

from tldextract import TLDExtract


class ScraperTest(unittest.TestCase):

    def setUp(self):
        tldextract = TLDExtract(suffix_list_urls=None)
        url_info = tldextract(self.scraper_class.host())
        options = getattr(self, 'scraper_options', {})

        with open('tests/test_data/{}.testhtml'.format(url_info.domain)) as f:
            self.harvester_class = self.scraper_class(f, test=True, **options)
