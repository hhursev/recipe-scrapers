import re
import unittest
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

from recipe_scrapers import SCRAPERS, AbstractScraper

START_LIST = "-----------------------"
END_LIST = "(*) offline saved files only"

ScraperIndex = Dict[str, Tuple[AbstractScraper, List[str]]]


def get_scraper_domains():
    scraper_domains = defaultdict(list)
    for domain, scraper in SCRAPERS.items():
        primary_domain = scraper.host()
        if domain == primary_domain:
            scraper_domains[scraper].insert(0, domain)
        else:
            scraper_domains[scraper].append(domain)
    return scraper_domains


def get_scraper_index() -> ScraperIndex:
    scraper_index = {}
    for scraper, domains in get_scraper_domains().items():
        shared_prefix = get_shared_prefix(domains)

        if not shared_prefix:
            # Treat all as primary domains
            for domain in domains:
                scraper_index[domain] = (scraper, [domain])
            continue

        # Index the primary domain and include their secondary domains minus the shared prefix
        primary_domain = scraper.host()
        scraper_index[primary_domain] = (
            scraper,
            [
                (
                    domain[len(shared_prefix) :]
                    if domain.startswith(shared_prefix)
                    else domain
                )
                for domain in domains
                if domain != shared_prefix
            ],
        )

    # Produce the index sorted by primary domain name
    return scraper_index


def get_shared_prefix(domains):
    """
    Find the longest-common-prefix of the domains
    """
    shared_prefix = ""
    while True:
        if any(len(domain) == len(shared_prefix) for domain in domains):
            break
        next_char = domains[0][len(shared_prefix)]
        if not all(domain.startswith(shared_prefix + next_char) for domain in domains):
            break
        shared_prefix += next_char

    shared_prefix, _ = (
        shared_prefix.rsplit(".", 1) if "." in shared_prefix else (shared_prefix, None)
    )

    return shared_prefix


def get_secondary_domains(
    scraper_index: ScraperIndex, primary_domain: str
) -> List[str]:
    _, suffixes = scraper_index[primary_domain]
    return [suffix for suffix in suffixes if not primary_domain.endswith(suffix)]


def parse_primary_line(line: str) -> Optional[Tuple[str, str]]:
    match = re.search(
        r"^- `https?://(?:www\.)?([^/\s]+)[^<]*<https?://(?:www\.)?([^/\s]*)[^>]*>`_(?: \(\*\))?$",
        line,
    )

    if not match:
        return None

    return match.group(1), match.group(2)


def parse_secondary_line(line: str):
    matches = re.findall(r"`(\.[^\s]+)\s<https?://(?:www\.)?([^/>]+)[^>]*>`_", line)
    return matches


def get_list_lines() -> List[str]:
    list_lines = []
    with open("README.rst") as f:
        started_list = False
        for line in f:
            stripped_line = line.strip()
            if stripped_line == START_LIST:
                started_list = True
                continue

            if not started_list or not stripped_line:
                continue

            if stripped_line == END_LIST:
                break

            list_lines.append(line)
    return list_lines


class TestReadme(unittest.TestCase):

    def test_includes(self):
        scraper_index = get_scraper_index()
        primary_domains = sorted(scraper_index.keys())

        lines = get_list_lines()

        current_line_index = 0
        for primary_host in primary_domains:
            current_line = lines[current_line_index]

            parse_result = parse_primary_line(current_line)
            if not parse_result:
                self.fail(f"Invalid line: {current_line}")

            name_host, value_host = parse_result
            self.assertEqual(
                name_host,
                value_host,
                "The name and value hyperlink portions have different hosts.",
            )
            self.assertEqual(
                name_host,
                primary_host,
                f"The host ({name_host}) doesn't match the expected host ({primary_host})",
            )

            current_line_index += 1

            secondary_hosts = get_secondary_domains(scraper_index, primary_host)
            if secondary_hosts:
                current_line = lines[current_line_index]
                parse_result = parse_secondary_line(lines[current_line_index])
                if not parse_result:
                    self.fail(f"Invalid line: {current_line}")

                sorted_secondary_hosts = sorted(secondary_hosts)
                for i, secondary_host in enumerate(sorted_secondary_hosts):
                    if not parse_result or not parse_result[i]:
                        self.fail(
                            f"Missing top level domain(s) for primary domain {primary_host}"
                        )

                    top_level_domain = parse_result[i][0]

                    self.assertEqual(
                        secondary_host,
                        top_level_domain,
                        f"Expected top level domain {secondary_host}, got {top_level_domain} for primary domain {primary_host}",
                    )
                current_line_index += 1
