import re
import unittest
from typing import Any, Dict, List, Optional, Tuple

from recipe_scrapers import SCRAPERS

START_LIST = "-----------------------"
END_LIST = "(*) offline saved files only"


def get_supported_hosts() -> Dict[str, List[str]]:
    supported_scrapers: Dict[str, List[str]] = {}
    for host in SCRAPERS:
        scraper: Any = SCRAPERS[host]
        primary_host = scraper.host()

        if host in supported_scrapers:
            continue

        if host == primary_host:
            supported_scrapers[primary_host] = []
        else:
            supported_scrapers[primary_host].append(host)

    return supported_scrapers


def determine_sub_level_domain(primary_host, secondary_hosts) -> Optional[str]:
    if not secondary_hosts:
        return None

    for i in range(len(primary_host)):
        current_character = primary_host[i]
        for secondary_host in secondary_hosts:
            if secondary_host[i] != current_character:
                return primary_host[: i - 1]

    return primary_host


def get_top_level_domains(primary_host, secondary_hosts) -> List[str]:
    sub_level_domain = determine_sub_level_domain(primary_host, secondary_hosts)

    if not sub_level_domain:
        return []

    return [
        secondary_host[len(sub_level_domain) :] for secondary_host in secondary_hosts
    ]


def get_supported_scrapers() -> Dict[str, List[str]]:
    supported_hosts = get_supported_hosts()
    supported_scrapers = {}
    for primary_host in supported_hosts:
        secondary_hosts = supported_hosts[primary_host]
        secondary_tlds = get_top_level_domains(primary_host, secondary_hosts)
        supported_scrapers[primary_host] = secondary_tlds
    return supported_scrapers


def parse_primary_line(line: str) -> Optional[Tuple[str, str]]:
    match = re.search(
        r"^- `https?://(?:www\.)?([^/\s]+)[^<]*<https?://(?:www\.)?([^/\s]*)[^>]*>`_$",
        line,
    )

    if not match:
        return None

    return match.group(1), match.group(2)


def parse_secondary_line(line: str):
    matches = re.search(r"`(\.[^\s]+)\s<https?://([^/>]+)>`_", line)
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
        supported_scrapers = get_supported_scrapers()
        sorted_supported_hosts = sorted(list(supported_scrapers.keys()))
        lines = get_list_lines()
        current_line_index = 0
        for primary_host in sorted_supported_hosts:
            parse_result = parse_primary_line(lines[current_line_index])
            if not parse_result:
                self.fail(f"Line {current_line_index + 1} is incorrect.")

            name_host, value_host = parse_result
            self.assertEqual(name_host, value_host)
            self.assertEqual(name_host, primary_host)

            current_line_index += 1
