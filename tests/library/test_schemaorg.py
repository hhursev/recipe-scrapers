import unittest

from recipe_scrapers._schemaorg import SchemaOrg

JSONLD_PAGE_TEMPLATE = """
<html>
<head>
<link href="http://recipe.test/template" type="canonical" />
<script type="application/ld+json">{jsonld}</script>
</head>
</html>
"""

SIMPLE_SCHEMA = """
{
  "@context": "https://schema.org",
  "@type": "Recipe",
  "name": "Test Recipe",
  "recipeIngredient": ["1 slice of bread", "5g margarine"],
  "recipeInstructions": ["spread the margarine on the bread"]
}
"""

MULTI_ENTITY_SCHEMA = """
[
  {
    "@context": "https://schema.org",
    "@type": "Recipe",
    "@id": "http://recipe.test/template",
    "name": "Test Recipe",
  },
  {
    "@context": "https://schema.org",
    "@type": "Recipe",
    "@id": "http://recipe.test/other",
    "name": "Another great test recipe",
  },
  {
    "@context": "https://schema.org",
    "@type": "WebPage",
    "@id": "http://recipe.test/template",
    "mainEntity": {
      "@context": "https://schema.org",
      "@type": "Recipe",
      "@id": "http://recipe.test/template",
      "recipeIngredient": ["1 slice of bread", "5g margarine"],
      "recipeInstructions": ["spread the margarine on the bread"]
    }
  }
]
"""


class TestSchemaOrg(unittest.TestCase):

    def test_simple(self):
        page_data = JSONLD_PAGE_TEMPLATE.format(jsonld=SIMPLE_SCHEMA)
        parser = SchemaOrg(page_data)

        self.assertEqual("Test Recipe", parser.title())
        self.assertIn("1 slice of bread", parser.ingredients())
        self.assertIn("5g margarine", parser.ingredients())
        self.assertEqual("spread the margarine on the bread", parser.instructions())

    def test_multi_entity_aggregation(self):
        page_data = JSONLD_PAGE_TEMPLATE.format(jsonld=MULTI_ENTITY_SCHEMA)
        parser = SchemaOrg(page_data)

        self.assertEqual("Test Recipe", parser.title())
        self.assertIn("1 slice of bread", parser.ingredients())
        self.assertIn("5g margarine", parser.ingredients())
        self.assertEqual("spread the margarine on the bread", parser.instructions())
