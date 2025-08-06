import json
import os
import unittest

from recipe_scrapers._utils import get_abstract_methods


class TestJsonOrder(unittest.TestCase):

    def test_json_key_order(self):
        correct_order = get_abstract_methods()
        json_directory = "tests/test_data/"

        for root, dirs, files in os.walk(json_directory):
            for filename in files:
                if filename.endswith(".json"):
                    with open(os.path.join(root, filename), encoding="utf-8") as f:
                        data = json.load(f)

                    filtered_data_keys = [key for key in correct_order if key in data]

                    expected_keys = filtered_data_keys
                    actual_keys = list(data.keys())

                    try:
                        self.assertEqual(expected_keys, actual_keys)
                    except AssertionError as e:
                        recommend_reorder_helper = (
                            "\n\nTo automatically reorder the keys, run the following command:\n"
                            "python scripts/reorder_json_keys.py\n"
                        )
                        raise AssertionError(
                            f"File: {os.path.join(root, filename)}\n"
                            f"{str(e)}"
                            f"{recommend_reorder_helper}"
                        ) from e
