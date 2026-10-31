import unittest
from pathlib import Path

from recipe_scrapers import scrape_html
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

DIETARY_RESTRICTIONS_SCHEMA = """
{
  "@context": "https://schema.org",
  "@type": "Recipe",
  "name": "Avocado panzanella",
  "recipeIngredient": [],
  "recipeInstructions": [],
  "suitableForDiet": [
    "https://schema.org/VegetarianDiet",
    {
      "@type": "Diet",
      "name": "Vegan"
    },
    {
      "@type": "Diet",
      "name": "Mediterranean"
    }
  ]
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
        self.assertEqual(
            [{"name": None, "steps": ["First step."]}],
            parser.instruction_groups(),
        )

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

    def test_instruction_groups_preserve_sections_and_step_boundaries(self):
        page_data = JSONLD_PAGE_TEMPLATE.format(
            jsonld=HOWTO_SECTION_MIXED_ITEM_LIST_ELEMENT_SCHEMA
        )
        scraper = SchemaScraperFactory.generate(
            page_data, "http://recipe.test/template"
        )

        expected = [
            {"name": None, "steps": ["Prep."]},
            {"name": "Standard section", "steps": ["List step one.", "List step two."]},
            {"name": "Wrapped section", "steps": ["Dict step."]},
        ]
        self.assertEqual(expected, scraper.instruction_groups())
        self.assertEqual(expected, scraper.to_json()["instruction_groups"])

    def test_instruction_groups_keep_newlines_within_one_step(self):
        page_data = JSONLD_PAGE_TEMPLATE.format(
            jsonld="""{"@context":"https://schema.org","@type":"Recipe",
            "recipeInstructions":[{"@type":"HowToStep","text":"Mix.\\nRest."},
            {"@type":"HowToSection","name":"Cook","itemListElement":[
              {"@type":"HowToStep","text":"Heat."}]},
            {"@type":"HowToStep","text":"Bake."}]}"""
        )
        scraper = SchemaScraperFactory.generate(
            page_data, "http://recipe.test/template"
        )
        self.assertEqual(
            [
                {"name": None, "steps": ["Mix.\nRest."]},
                {"name": "Cook", "steps": ["Heat."]},
                {"name": None, "steps": ["Bake."]},
            ],
            scraper.instruction_groups(),
        )

    def test_instruction_groups_accept_wrapper_and_uppercase_section_name(self):
        page_data = JSONLD_PAGE_TEMPLATE.format(
            jsonld="""{"@context":"https://schema.org","@type":"Recipe",
            "recipeInstructions":{"itemListElement":[
              {"@type":"HowToStep","text":"Prep."},
              {"@type":"HowToSection","Name":"Cook","itemListElement":[
                {"@type":"HowToStep","text":"Heat."},
                {"@type":"HowToStep","text":"Serve."}]}]}}"""
        )
        scraper = SchemaScraperFactory.generate(
            page_data, "http://recipe.test/template"
        )
        self.assertEqual(
            [
                {"name": None, "steps": ["Prep."]},
                {"name": "Cook", "steps": ["Heat.", "Serve."]},
            ],
            scraper.instruction_groups(),
        )

    def test_instruction_groups_keep_plain_string_as_one_step(self):
        page_data = JSONLD_PAGE_TEMPLATE.format(
            jsonld=PROPERTY_VALUE_INGREDIENTS_SCHEMA
        )
        scraper = SchemaScraperFactory.generate(
            page_data, "http://recipe.test/template"
        )
        self.assertEqual(
            [{"name": None, "steps": ["Mix and bake."]}],
            scraper.instruction_groups(),
        )

    def test_instruction_groups_preserve_microdata_list_items(self):
        html = """<html><div itemscope itemtype="http://schema.org/Recipe">
          <h1 itemprop="name">Test Recipe</h1>
          <ol itemprop="recipeInstructions">
            <li>Mix.<br>Rest.</li><li><p>Bake.</p><p>Cool.</p></li>
          </ol>
        </div></html>"""
        scraper = scrape_html(html, "https://example.com/recipe", supported_only=False)
        self.assertEqual(
            [{"name": None, "steps": ["Mix.\nRest.", "Bake.\nCool."]}],
            scraper.instruction_groups(),
        )

    def test_instruction_groups_preserve_one_microdata_step(self):
        html = """<html><div itemscope itemtype="http://schema.org/Recipe">
          <h1 itemprop="name">Test Recipe</h1>
          <ol itemprop="recipeInstructions"><li>Mix.<br>Rest.</li></ol>
        </div></html>"""
        scraper = scrape_html(html, "https://example.com/recipe", supported_only=False)
        self.assertEqual(
            [{"name": None, "steps": ["Mix.\nRest."]}],
            scraper.instruction_groups(),
        )

    def test_instruction_groups_on_real_site_fixtures(self):
        cases = [
            (
                "baking-sense.com/bakingsense_1.testhtml",
                [(None, 1), ("Make the batter", 6), ("Make the Glaze", 3)],
            ),
            (
                "howtocook.recipes/howtocook_2.testhtml",
                [(None, 3), ("Chocolate Buttercream Frosting", 2)],
            ),
            ("lazycatkitchen.com/lazycatkitchen_1.testhtml", [(None, 8)]),
            ("thehappyfoodie.co.uk/thehappyfoodie_1.testhtml", [(None, 1)]),
        ]
        for fixture, expected_groups in cases:
            with self.subTest(fixture=fixture):
                html = (Path("tests/test_data") / fixture).read_text(encoding="utf-8")
                host = fixture.split("/")[0]
                scraper = scrape_html(html, f"https://{host}/")
                groups = scraper.instruction_groups()
                self.assertEqual(
                    expected_groups,
                    [(g["name"], len(g["steps"])) for g in groups],
                )
                self.assertTrue(all(g["steps"] for g in groups))

    def test_instruction_groups_fall_back_to_custom_instructions(self):
        html = "<html><section class='directions'><div class='directions__content'><p>Mix.</p><p>Bake.</p></div></section></html>"
        scraper = scrape_html(html, "https://pauladeen.com/recipe")
        self.assertEqual(
            [{"name": None, "steps": ["Mix.", "Bake."]}],
            scraper.instruction_groups(),
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

    def test_dietary_restrictions_with_diet_objects(self):
        page_data = JSONLD_PAGE_TEMPLATE.format(jsonld=DIETARY_RESTRICTIONS_SCHEMA)
        parser = SchemaOrg(page_data)

        self.assertEqual(
            ["Vegetarian Diet", "Vegan", "Mediterranean"],
            parser.dietary_restrictions(),
        )
