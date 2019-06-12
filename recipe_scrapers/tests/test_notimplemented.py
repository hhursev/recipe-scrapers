import os
import unittest

from recipe_scrapers._abstract import AbstractScraper


class TestNotImplemented(unittest.TestCase):
    def setUp(self):
        # impelement class that inherits from AbstractScraper and does not
        # define the mandatory methods. Make sure NotImplementedError is raised
        class TestRaises(AbstractScraper):
            pass

        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            'paninihappy.testhtml'
        )) as file_opened:
            self.harvester_class = TestRaises(file_opened, test=True)

    def test_host(self):
        with self.assertRaises(NotImplementedError):
            self.harvester_class.host()

    def test_title(self):
        with self.assertRaises(NotImplementedError):
            self.harvester_class.title()

    def test_total_time(self):
        with self.assertRaises(NotImplementedError):
            self.harvester_class.total_time()

    def test_ingredients(self):
        with self.assertRaises(NotImplementedError):
            self.harvester_class.ingredients()

    def test_instructions(self):
        with self.assertRaises(NotImplementedError):
            self.harvester_class.instructions()
