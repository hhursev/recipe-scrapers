import json
import os

from recipe_scrapers._utils import get_abstract_methods

KEYS = get_abstract_methods()


def reorder_json_keys(file_path):
    with open(file_path, encoding="utf-8") as file:
        data = json.load(file)

    reordered_data = {key: data[key] for key in KEYS if key in data}

    # Serialize both original and reordered data for comparison
    original_content = json.dumps(data, indent=2, ensure_ascii=False)
    reordered_content = json.dumps(reordered_data, indent=2, ensure_ascii=False)

    if original_content != reordered_content:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(reordered_content + "\n")


def process_directory(directory, start_letter):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json") and (
                file.startswith(start_letter) or start_letter == "*"
            ):
                file_path = os.path.join(root, file)
                reorder_json_keys(file_path)


if __name__ == "__main__":
    process_directory("tests/test_data", "*")
