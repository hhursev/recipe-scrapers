import os
import unittest

class ScraperTest(unittest.TestCase):

    def setUp(self):
        domain = self.scraper_class.host().split('.')[0]
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            '{}.testhtml'.format(domain)
        )) as file_opened:
            self.harvester_class = self.scraper_class(file_opened, test=True)
