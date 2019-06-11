import os
import unittest

from recipe_scrapers._abstract import AbstractScraper


class TestingExceptionsHandling(AbstractScraper):
    """
    Custom Harvester Class that will raise exceptions in its methods
    to check if the decorator handling exceptions is working properly
    """
    def title(self):
        raise Exception

    def total_time(self):
        raise Exception

    def yields(self):
        raise Exception

    def ingredients(self):
        raise Exception

    def links(self):
        return []


class TestExceptionsHandlingScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            'allrecipes.testhtml'
        )) as file_opened:
            self.harvester_class = TestingExceptionsHandling(file_opened, test=True)
        setattr(self.harvester_class, 'testing_mode', False)

    def test_host(self):
        with self.assertRaises(NotImplementedError):
            self.harvester_class.host()

    def test_title(self):
        return self.assertEqual('', self.harvester_class.title())

    def test_total_time(self):
        return self.assertEqual(0, self.harvester_class.total_time())

    def test_yields(self):
        return self.assertEqual("", self.harvester_class.yields())

    def test_ingredients(self):
        return self.assertCountEqual([], self.harvester_class.ingredients())

    def test_not_implemented_is_raising(self):
        with self.assertRaises(NotImplementedError):
            return self.assertEqual('', self.harvester_class.instructions())

    def test_on_no_exception_return_default_result(self):
        return self.assertEqual([], self.harvester_class.links())
