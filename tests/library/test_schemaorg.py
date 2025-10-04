import unittest

from recipe_scrapers._factory import SchemaScraperFactory
from recipe_scrapers._schemaorg import SchemaOrg
from recipe_scrapers.settings import settings

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
BEST_IMAGE_SCHEMA = """
{
  "@context": "https://schema.org",
  "@type": "Recipe",
  "name": "Image Comparison",
  "image": [
    "https://images.example.com/recipe-320x240.jpg",
    {
      "@type": "ImageObject",
      "url": "https://images.example.com/recipe-1280x720.jpg",
      "width": 1280,
      "height": 720
    },
    "https://images.example.com/recipe-640x480.jpg"
  ],
  "recipeIngredient": [],
  "recipeInstructions": []
}
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

    def test_best_image_selection(self):
        page_data = JSONLD_PAGE_TEMPLATE.format(jsonld=BEST_IMAGE_SCHEMA)

        default_scraper = SchemaScraperFactory.generate(
            html=page_data,
            url="http://recipe.test/template",
        )
        self.assertEqual(
            "https://images.example.com/recipe-1280x720.jpg",
            default_scraper.image(),
        )

        best_image_scraper = SchemaScraperFactory.generate(
            html=page_data,
            url="http://recipe.test/template",
            best_image=False,
        )
        self.assertEqual(
            "https://images.example.com/recipe-320x240.jpg",
            best_image_scraper.image(),
        )

    def test_best_image_setting_toggle(self):
        page_data = JSONLD_PAGE_TEMPLATE.format(jsonld=BEST_IMAGE_SCHEMA)

        original = settings.BEST_IMAGE_SELECTION
        try:
            settings.BEST_IMAGE_SELECTION = True
            configured_scraper = SchemaScraperFactory.generate(
                html=page_data,
                url="http://recipe.test/template",
            )
            self.assertEqual(
                "https://images.example.com/recipe-1280x720.jpg",
                configured_scraper.image(),
            )
        finally:
            settings.BEST_IMAGE_SELECTION = original
