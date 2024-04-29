import re
import unittest
from typing import List

from recipe_scrapers import SCRAPERS

SEPARATOR = "Scrapers available for:"


def get_documented_scrapers() -> List[str]:
    documented_scrapers = []
    with open("README.rst") as f:
        found = False
        for line in f:
            if line.strip() == SEPARATOR:
                found = True
                next(f)  # Skip the underline
                continue
            if not found or not line.strip():
                continue

            match = re.search(r"^- `https?://(?:www\.)?([^/\s]+)", line)
            if match:
                documented_scrapers.append(match.group(1))
            else:
                # Stops reading if no longer within the scraper list section
                if found and line.startswith('(*) offline saved files only'):

    return documented_scrapers


class TestReadme(unittest.TestCase):

    def test_includes(self):
        documented_scrapers = get_documented_scrapers()
        missing_scrapers = []

        for scraper in SCRAPERS:
            match = re.search(r"(?:www.)?(.*)", scraper)
            domain = match.group(1)
            if domain not in documented_scrapers:
                missing_scrapers.append(domain)

        self.assertFalse(missing_scrapers, f"Missing scrapers in README.rst: {missing_scrapers}")
