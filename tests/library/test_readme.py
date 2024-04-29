import re
import unittest
from typing import List, Optional

from recipe_scrapers import SCRAPERS

START_LIST = "-----------------------"
END_LIST = "(*) offline saved files only"


def parse_list_line(line: str) -> Optional[str]:
    match = re.search(r"^- `https?://(?:www\.)?([^/\s]+)", line)

    if not match:
        return None

    return match.group(1)


def get_documented_scrapers() -> List[str]:
    documented_scrapers = []
    with open("README.rst") as f:
        started_list = False
        for line in f:
            if line.strip() == START_LIST:
                started_list = True
                continue

            if not started_list or not line.strip():
                continue

            if line.strip() == END_LIST:
                break

            documented_scraper = parse_list_line(line)
            if documented_scraper:
                documented_scrapers.append(documented_scraper)

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

        self.assertFalse(
            missing_scrapers, f"Missing scrapers in README.rst: {missing_scrapers}"
        )
