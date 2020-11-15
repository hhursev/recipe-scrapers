import unittest

from recipe_scrapers._schemaorg import SchemaOrg


class TestSchemaOrg(unittest.TestCase):
    def setUp(self):
        with open("tests/test_data/schemaorg.testhtml", encoding="utf-8") as pagedata:
            self.schema = SchemaOrg(pagedata.read())

    def test_total_time_with_schema_missing_all_data(self):
        keys = ["totalTime", "cookTime", "prepTime"]
        for k in keys:
            if k in self.schema.data:
                del self.schema.data[k]
        self.assertEqual(self.schema.total_time(), 0)

    def test_graph_schema_without_context(self):
        with open(
            "tests/test_data/schemaorg_graph.testhtml", encoding="utf-8"
        ) as pagedata:
            schema = SchemaOrg(pagedata.read())
        self.assertNotEqual(schema.data, {})
