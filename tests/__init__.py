import os
import unittest

from tldextract import TLDExtract


class ScraperTest(unittest.TestCase):

    def setUp(self):
        tldextract = TLDExtract(suffix_list_urls=None)
        url_info = tldextract(self.scraper_class.host())
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            '{}.testhtml'.format(url_info.domain)
        )) as file_opened:
            self.harvester_class = self.scraper_class(file_opened, test=True)
