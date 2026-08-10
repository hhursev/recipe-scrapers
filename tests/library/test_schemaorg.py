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
PROPERTY_VALUE_INGREDIENTS_SCHEMA = """
{
  "@context": "https://schema.org",
  "@type": "Recipe",
  "name": "PropertyValue Recipe",
  "recipeIngredient": [
    "3 or 4 ripe bananas, smashed",
    { "@type": "PropertyValue", "value": 1, "name": "egg" },
    { "@type": "PropertyValue", "value": "3/4", "name": "sugar", "unitCode": "G21" },
    { "@type": "PropertyValue", "value": "1/2", "name": "flour", "unitText": "cup" }
  ],
  "recipeInstructions": "Mix and bake."
}
"""

HOWTO_SECTION_DICT_ITEM_LIST_ELEMENT_SCHEMA = """
{
  "@context": "https://schema.org",
  "@type": "Recipe",
  "name": "Section Dict Recipe",
  "recipeIngredient": [],
  "recipeInstructions": [
    {"@type": "HowToStep", "text": "First step."},
    {
      "@type": "HowToSection",
      "itemListElement": {"@type": "HowToStep", "text": "Wrapped step."}
    }
  ]
}
"""

HOWTO_SECTION_EMPTY_SCHEMA = """
{
  "@context": "https://schema.org",
  "@type": "Recipe",
  "name": "Empty Section Recipe",
  "recipeIngredient": [],
  "recipeInstructions": [
    {"@type": "HowToStep", "text": "First step."},
    {"@type": "HowToSection"}
  ]
}
"""

HOWTO_SECTION_MIXED_ITEM_LIST_ELEMENT_SCHEMA = """
{
  "@context": "https://schema.org",
  "@type": "Recipe",
  "name": "Mixed Section Recipe",
  "recipeIngredient": [],
  "recipeInstructions": [
    {"@type": "HowToStep", "text": "Prep."},
    {
      "@type": "HowToSection",
      "name": "Standard section",
      "itemListElement": [
        {"@type": "HowToStep", "text": "List step one."},
        {"@type": "HowToStep", "text": "List step two."}
      ]
    },
    {
      "@type": "HowToSection",
      "name": "Wrapped section",
      "itemListElement": {"@type": "HowToStep", "text": "Dict step."}
    }
  ]
}
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

    def test_property_value_ingredients(self):
        page_data = JSONLD_PAGE_TEMPLATE.format(
            jsonld=PROPERTY_VALUE_INGREDIENTS_SCHEMA
        )
        parser = SchemaOrg(page_data)
        ingredients = parser.ingredients()
        self.assertIn("3 or 4 ripe bananas, smashed", ingredients)
        self.assertIn("1 egg", ingredients)
        self.assertIn("3/4 G21 sugar", ingredients)
        self.assertIn("1/2 cup flour", ingredients)

    def test_howto_section_with_dict_item_list_element(self):
        page_data = JSONLD_PAGE_TEMPLATE.format(
            jsonld=HOWTO_SECTION_DICT_ITEM_LIST_ELEMENT_SCHEMA
        )
        parser = SchemaOrg(page_data)
        self.assertEqual("First step.\nWrapped step.", parser.instructions())

    def test_howto_section_with_missing_item_list_element(self):
        page_data = JSONLD_PAGE_TEMPLATE.format(jsonld=HOWTO_SECTION_EMPTY_SCHEMA)
        parser = SchemaOrg(page_data)
        self.assertEqual("First step.", parser.instructions())

    def test_howto_section_with_mixed_item_list_element_shapes(self):
        page_data = JSONLD_PAGE_TEMPLATE.format(
            jsonld=HOWTO_SECTION_MIXED_ITEM_LIST_ELEMENT_SCHEMA
        )
        parser = SchemaOrg(page_data)
        self.assertEqual(
            "Prep.\n"
            "Standard section\n"
            "List step one.\n"
            "List step two.\n"
            "Wrapped section\n"
            "Dict step.",
            parser.instructions(),
        )

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

    def test_nextjs_ssr_jsonld(self):
        """JSON-LD injected via Next.js __next_s.push() must be detected."""
        import json as _json

        ld = {
            "@context": "https://schema.org",
            "@type": "Recipe",
            "name": "Test Next.js Recipe",
            "recipeIngredient": ["500g fish"],
            "recipeInstructions": ["Cook the fish."],
        }
        outer = _json.dumps(
            {"type": "application/ld+json", "async": True, "children": _json.dumps(ld)}
        )
        page_data = (
            "<html><head><title>Test</title>"
            f"<script>(self.__next_s=self.__next_s||[]).push([0,{outer}])</script>"
            "</head><body></body></html>"
        )
        parser = SchemaOrg(page_data)
        self.assertEqual("Test Next.js Recipe", parser.title())
        self.assertIn("500g fish", parser.ingredients())
        self.assertEqual("Cook the fish.", parser.instructions())
