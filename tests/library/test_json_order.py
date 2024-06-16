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
                    with open(os.path.join(root, filename)) as f:
                        data = json.load(f)

                    filtered_data_keys = [key for key in correct_order if key in data]

                    expected_keys = [
                        key for key in correct_order if key in filtered_data_keys
                    ]
                    actual_keys = list(data.keys())

                    try:
                        self.assertEqual(expected_keys, actual_keys)
                    except AssertionError as e:
                        e.args = (f"File: {os.path.join(root, filename)}\n" + str(e),)
                        raise


if __name__ == "__main__":
    unittest.main()
