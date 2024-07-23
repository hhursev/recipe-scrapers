import json
import os

from recipe_scrapers._utils import get_abstract_methods

KEYS = get_abstract_methods()


def reorder_json_keys(file_path):
    with open(file_path, encoding="utf-8") as file:
        data = json.load(file)

    reordered_data = {key: data[key] for key in KEYS if key in data}

    if list(data.keys()) != KEYS:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(reordered_data, file, indent=2, ensure_ascii=False)
            file.write("\n")


def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                reorder_json_keys(file_path)


if __name__ == "__main__":
    process_directory("tests/test_data")
