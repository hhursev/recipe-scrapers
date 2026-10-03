import unittest

from recipe_scrapers import NoSchemaFoundInWildMode, scrape_html

HTML_WITH_OG = """
<html>
<head>
<meta property="og:title" content="Test recipe">
<meta property="og:description" content="This is some test recipe">
<meta property="og:image" content="https://example.org/test-image.png">
</head>
</html>
"""

HTML_WITH_PARTIAL_OG = """
<html>
<head>
<meta property="og:title" content="Title only">
</head>
</html>
"""

HTML_WITH_OG_AND_RECIPE_SCHEMA = """
<html>
<head>
<meta property="og:title" content="From OG">
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Recipe",
  "name": "From schema"
}
</script>
</head>
</html>
"""

TEST_URL = "https://example.org/test-recipe.html"


class TestOpenGraph(unittest.TestCase):

    def test_scrapes_open_graph_metadata(self):
        scraper = scrape_html(
            HTML_WITH_OG,
            TEST_URL,
            supported_only=False,
            simple_opengraph=True,
        )

        self.assertEqual("Test recipe", scraper.title())
        self.assertEqual("This is some test recipe", scraper.description())
        self.assertEqual("https://example.org/test-image.png", scraper.image())

    def test_partial_open_graph_is_enough(self):
        scraper = scrape_html(
            HTML_WITH_PARTIAL_OG,
            TEST_URL,
            supported_only=False,
            simple_opengraph=True,
        )

        self.assertEqual("Title only", scraper.title())
        self.assertEqual("", scraper.description())
        self.assertIsNone(scraper.image())

    def test_raises_when_flag_is_off(self):
        with self.assertRaises(NoSchemaFoundInWildMode):
            scrape_html(
                HTML_WITH_OG,
                TEST_URL,
                supported_only=False,
                simple_opengraph=False,
            )

    def test_raises_when_page_has_no_open_graph(self):
        with self.assertRaises(NoSchemaFoundInWildMode):
            scrape_html(
                "<html></html>",
                TEST_URL,
                supported_only=False,
                simple_opengraph=True,
            )

    def test_recipe_schema_beats_open_graph(self):
        scraper = scrape_html(
            HTML_WITH_OG_AND_RECIPE_SCHEMA,
            TEST_URL,
            supported_only=False,
            simple_opengraph=True,
        )

        self.assertEqual("From schema", scraper.title())
