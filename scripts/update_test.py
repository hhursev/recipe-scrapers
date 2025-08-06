import argparse
import json
import pathlib

import requests
from reorder_json_keys import reorder_json_keys

from recipe_scrapers import SCRAPERS, scrape_html


def update_testcase(json_file: pathlib.Path) -> None:
    """Update testcase by downloading the latest version of the html
    and run the scraper on it to create a new version of the json file.
    Assumes the json file is in the standard file tree.

    Args:
        json_file (pathlib.Path): The original json file.

    """
    json_file = json_file.absolute()
    html_file = json_file.with_suffix(".testhtml")
    orig_data = json.loads(json_file.read_text(encoding="utf-8"))
    url = orig_data["canonical_url"]
    host = html_file.parent.name
    html_data = requests.get(url, timeout=10).content.decode()
    html_file.write_text(html_data)
    supported_only = host in SCRAPERS
    actual = scrape_html(
        html=html_data,
        org_url=host,
        online=False,
        supported_only=supported_only,
    )
    new_data = actual.to_json()

    json_file.write_text(
        json.dumps(new_data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    reorder_json_keys(str(json_file), quiet=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fetch the latest version of a recipe and update the test data",
    )
    parser.add_argument("json_file", help="The json file describing the test")

    args = parser.parse_args()
    update_testcase(pathlib.Path(args.json_file))
