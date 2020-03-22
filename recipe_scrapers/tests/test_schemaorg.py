import os
from unittest import TestCase
from unittest.mock import patch

from recipe_scrapers._schemaorg import SchemaOrg
from recipe_scrapers.tests.test_allrecipes import TestAllRecipesScraper as ars


class TestSchemaOrgScraper(TestCase):

    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            'allrecipes.testhtml'
        )) as file_opened:
            self.harvester_class = SchemaOrg(file_opened, test=True)

        patcher = patch(
            "recipe_scrapers.tests.test_allrecipes.harvester_class",
            create=True,
            return_value=self.harvester_class,
        )
        self.ars = ars()

        self.ars.setUp()
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_host(self):
        self.assertEqual(
            'schema.org',
            self.harvester_class.host()
        )

    def test_title(self):
        self.ars.test_title()

    def test_total_time(self):
        self.ars.test_total_time()

    def test_yields(self):
        self.ars.test_yields()

    def test_image(self):
        self.ars.test_image()

    def test_ingredients(self):
        self.ars.test_ingredients()

    def test_instructions(self):
        self.ars.test_instructions()

    def test_ratings(self):
        self.ars.test_ratings()
