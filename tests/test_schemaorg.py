import unittest

from recipe_scrapers._exceptions import SchemaOrgException
from recipe_scrapers._schemaorg import SchemaOrg


class TestSchemaOrg(unittest.TestCase):
    def setUp(self):
        with open("tests/test_data/schemaorg.testhtml", encoding="utf-8") as pagedata:
            self.schema = SchemaOrg(pagedata.read())

    def test_total_time_with_schema_missing_all_data_should_raise_exception(self):
        keys = ["totalTime", "cookTime", "prepTime"]
        for k in keys:
            if k in self.schema.data:
                del self.schema.data[k]
        with self.assertRaises(SchemaOrgException):
            self.assertEqual(self.schema.total_time(), None)

    def test_total_time_with_schema__all_zeros(self):
        keys = ["totalTime", "cookTime", "prepTime"]
        for k in keys:
            self.schema.data[k] = "PT0M"
        self.assertEqual(self.schema.total_time(), 0)
        del self.schema.data["totalTime"]
        self.assertEqual(self.schema.total_time(), 0)

    def test_graph_schema_without_context(self):
        with open(
            "tests/test_data/schemaorg_graph.testhtml", encoding="utf-8"
        ) as pagedata:
            schema = SchemaOrg(pagedata.read())
        self.assertNotEqual(schema.data, {})
