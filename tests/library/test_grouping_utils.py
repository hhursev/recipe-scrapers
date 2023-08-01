import unittest

from recipe_scrapers._grouping_utils import best_match, score_sentence_similarity


class TestUtils(unittest.TestCase):
    def test_score_exact_match(self):
        first = "¼ cup maple syrup"
        second = "¼ cup maple syrup"
        self.assertEqual(1.0, score_sentence_similarity(first, second))

    def test_score_short_first_sentence(self):
        first = "a"
        second = "4 sprig fresh thyme"
        self.assertEqual(0.0, score_sentence_similarity(first, second))

    def test_score_short_second_sentence(self):
        first = "4 sprig fresh thyme"
        second = ""
        self.assertEqual(0.0, score_sentence_similarity(first, second))

    def test_score_similar_sentences(self):
        first = "16oz firm tofu"
        second = "16 oz firm tofu"
        self.assertEqual(0.8888888888888888, score_sentence_similarity(first, second))

    def test_best_match(self):
        target_strings = [
            "¼ cup vegan mayonnaise",
            "apple cider vinegar",
            "¼ tsp salt",
            "1 cup shredded red cabbage",
            "1 cup shredded green cabbage",
            "1 carrot",
            "5 large soft tortilla",
            "½ head butter lettuce",
            "2 medium tomato",
        ]
        test_string = "1/4 cup vegan mayonnaise"

        self.assertEqual(
            "¼ cup vegan mayonnaise", best_match(test_string, target_strings)
        )
