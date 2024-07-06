import json
import os
import unittest


class TestJsonOrder(unittest.TestCase):

    def test_json_key_order(self):
        correct_order = [
            "author",
            "canonical_url",
            "site_name",
            "host",
            "language",
            "title",
            "ingredients",
            "ingredient_groups",
            "instructions",
            "instructions_list",
            "category",
            "yields",
            "description",
            "total_time",
            "cook_time",
            "prep_time",
            "cuisine",
            "cooking_method",
            "ratings",
            "ratings_count",
            "equipment",
            "reviews",
            "nutrients",
            "image",
            "keywords",
        ]
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
                        raise AssertionError(
                            f"File: {os.path.join(root, filename)}\n" + str(e)
                        ) from e
