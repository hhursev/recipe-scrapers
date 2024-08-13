import json
import os

from recipe_scrapers._utils import get_abstract_methods, get_nutrition_keys

KEYS = get_abstract_methods()
NUTRITION_KEYS = get_nutrition_keys()


def reorder_json_keys(file_path):
    with open(file_path, encoding="utf-8") as file:
        data = json.load(file)

    reordered_data = {key: data[key] for key in KEYS if key in data}
    if list(data.keys()) != list(reordered_data.keys()):
        print(f"Re-ordering JSON keys for: {file_path}")

    if "nutrients" in data and data["nutrients"] is not None:
        nutrients = data["nutrients"]
        reordered_nutrients = {
            key: nutrients[key] for key in NUTRITION_KEYS if key in nutrients
        }
        for key in nutrients:
            if key not in reordered_nutrients:
                reordered_nutrients[key] = nutrients[key]

        if list(nutrients.keys()) != list(reordered_nutrients.keys()):
            reordered_data["nutrients"] = reordered_nutrients
            print(f"Re-ordering nutrition keys for: {file_path}")

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
