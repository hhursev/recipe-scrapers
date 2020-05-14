import unittest


class ScraperTest(unittest.TestCase):

    def setUp(self):
        options = {'exception_handling': False}
        options.update(getattr(self, 'scraper_options', {}))

        with open('tests/test_data/{}.testhtml'.format(
            self.scraper_class.__name__.lower())
        ) as testfile:
            self.harvester_class = self.scraper_class(testfile, test=True, **options)
