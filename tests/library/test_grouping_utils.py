import unittest

from recipe_scrapers._grouping_utils import best_match, score_sentence_similarity


class TestUtils(unittest.TestCase):

    def test_score_exact_match(self):
        self.assertEqual(
            1.0, score_sentence_similarity("¼ cup maple syrup", "¼ cup maple syrup")
        )

    def test_score_no_match(self):
        self.assertEqual(0.0, score_sentence_similarity("a", "4 sprig fresh thyme"))
        self.assertEqual(0.0, score_sentence_similarity("4 sprig fresh thyme", ""))

    def test_score_special_characters(self):
        self.assertEqual(0.0, score_sentence_similarity("!@#$%^", "*&^%$#"))

    def test_score_numerical_strings(self):
        self.assertEqual(0.8, score_sentence_similarity("123", "1234"))

    def test_score_similar_but_not_exact(self):
        self.assertAlmostEqual(
            0.8888888888888888,
            score_sentence_similarity("16oz firm tofu", "16 oz firm tofu"),
            places=2,
        )

    def test_best_match_exact(self):
        target_strings = [
            "¼ cup vegan mayonnaise",
            "apple cider vinegar",
            "¼ tsp salt",
            "1 cup shredded red cabbage",
        ]
        self.assertEqual(
            "¼ cup vegan mayonnaise",
            best_match("¼ cup vegan mayonnaise", target_strings),
        )

    def test_best_match_closest(self):
        target_strings = [
            "apple cider vinegar",
            "¼ tsp salt",
            "1 cup shredded red cabbage",
            "5 large soft tortilla",
        ]
        self.assertEqual(
            "5 large soft tortilla", best_match("large tortilla", target_strings)
        )

    def test_best_match_singular_plural(self):
        target_strings = ["2 medium tomato", "½ head butter lettuce", "1 carrot"]
        self.assertEqual("2 medium tomato", best_match("tomato", target_strings))

    def test_best_match_with_no_exact_match(self):
        target_strings = ["¼ cup vegan mayonnaise", "apple cider vinegar", "¼ tsp salt"]
        self.assertNotEqual(
            "¼ cup maple syrup", best_match("¼ cup maple syrup", target_strings)
        )

    def test_score_with_empty_string(self):
        self.assertEqual(0.0, score_sentence_similarity("", "anything here"))

    def test_best_match_raises_error_with_empty_list(self):
        with self.assertRaises(ValueError):
            best_match("any string", [])
