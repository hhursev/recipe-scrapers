import unittest
from unittest import mock

from recipe_scrapers import scrape_html

HTML_WITH_OG = \
"""
<html>
<head>
<meta property="og:title" content="Test recipe">
<meta property="og:description" content="This is some test recipe">
<meta property="og:image" content="https://example.org/test-image.png">
</head>
</html>
"""

class TestOpenGraph(unittest.TestCase):

    def test_valid_call(self):
        scraper = scrape_html(HTML_WITH_OG, "https://example.org/test-recipe.html",
                              supported_only=False,
                              simple_opengraph=True)

        self.assertEqual("Test recipe", scraper.title())
        self.assertEqual("This is some test recipe", scraper.description())
        self.assertEqual("https://example.org/test-image.png", scraper.image())


