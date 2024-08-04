import json
import os
import unittest


class TestNutritionKeyOrder(unittest.TestCase):

    def test_nutrition_key_order(self):
        correct_order = [
            "servingSize",
            "calories",
            "fatContent",
            "saturatedFatContent",
            "unsaturatedFatContent",
            "transFatContent",
            "carbohydrateContent",
            "sugarContent",
            "proteinContent",
            "sodiumContent",
            "fiberContent",
            "cholesterolContent",
        ]
        json_directory = "tests/test_data/"

        for root, dirs, files in os.walk(json_directory):
            for filename in files:
                if filename.endswith(".json"):
                    with open(os.path.join(root, filename), encoding="utf-8") as f:
                        data = json.load(f)

                    if "nutrients" in data and data["nutrients"] is not None:
                        nutrients = data["nutrients"]
                        actual_keys = list(nutrients.keys())

                        ordered_keys = [
                            key for key in correct_order if key in actual_keys
                        ]
                        other_keys = [
                            key for key in actual_keys if key not in correct_order
                        ]

                        expected_keys = ordered_keys + other_keys

                        try:
                            self.assertEqual(expected_keys, actual_keys)
                        except AssertionError as e:
                            recommend_reorder_helper = (
                                "\n\nTo automatically reorder the nutrition keys, run the following command:\n"
                                "python scripts/reorder_nutrition_keys.py\n"
                            )
                            raise AssertionError(
                                f"File: {os.path.join(root, filename)}\n"
                                f"{str(e)}"
                                f"{recommend_reorder_helper}"
                            ) from e
