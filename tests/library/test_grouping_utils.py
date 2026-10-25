import itertools
import unittest

from bs4 import BeautifulSoup

from recipe_scrapers._grouping_utils import (
    _optimal_one_to_one_assignment,
    best_match,
    group_ingredients,
    score_sentence_similarity,
)


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


class TestOptimalOneToOneAssignment(unittest.TestCase):
    @staticmethod
    def _brute_force_min_cost(cost):
        n = len(cost)
        return min(
            sum(cost[i][perm[i]] for i in range(n))
            for perm in itertools.permutations(range(n))
        )

    def test_simple_2x2(self):
        # Optimal is the diagonal (cost 1+1=2), not the cross (cost 2+2=4).
        cost = [[1, 2], [2, 1]]
        assignment = _optimal_one_to_one_assignment(cost)
        total = sum(cost[i][assignment[i]] for i in range(2))
        self.assertEqual(2, total)

    def test_prefers_correct_pairing_over_locally_better_but_globally_worse_match(
        self,
    ):
        # Mirrors the real recipetineats.com bug this assignment strategy
        # exists to fix: element 0 ("wine") scores a *worse* match against
        # its own true counterpart (col 0) than against an unrelated
        # candidate (col 1) that happens to share more surface-level
        # structure (punctuation, filler words). Element 1 ("pasta") is a
        # near-exact match for col 1. A naive independent best-match-per-
        # element approach would let element 0 steal col 1, leaving
        # element 1 to fall back to a poor remaining option and col 0
        # (the true "wine" entry) unmatched by anything. The optimal
        # assignment must still prefer the correct pairing (0->0, 1->1)
        # since its total cost is lower once the one-to-one constraint is
        # enforced.
        cost = [
            [0.712, 0.578],  # element 0: worse match to its own entry (0) than to 1
            [0.95, 0.0],  # element 1: near-exact match to entry 1
        ]
        assignment = _optimal_one_to_one_assignment(cost)
        self.assertEqual([0, 1], assignment)

    def test_cross_validated_against_brute_force(self):
        import random

        random.seed(42)
        for _ in range(100):
            n = random.randint(1, 6)
            cost = [[random.uniform(0, 10) for _ in range(n)] for _ in range(n)]
            assignment = _optimal_one_to_one_assignment(cost)
            total = sum(cost[i][assignment[i]] for i in range(n))
            self.assertAlmostEqual(self._brute_force_min_cost(cost), total, places=6)


class TestGroupIngredients(unittest.TestCase):
    def test_duplicate_and_dropped_ingredient_regression(self):
        # Reproduces a real bug found on recipetineats.com
        # (slow-cooked-lamb-ragu-pasta): a wine ingredient's rendered HTML
        # text is long and descriptive, while its entry in the flat
        # ingredients_list (sourced from schema.org JSON-LD) is short.
        # Matching each HTML element independently to its single
        # best-scoring flat entry let the wine element's verbose text
        # outscore its own (short) true entry against an unrelated but
        # similarly verbose pasta entry — silently duplicating the pasta
        # ingredient into the wine group and dropping wine entirely, while
        # item counts still matched so nothing else caught it.
        html = """
        <div class="wprm-recipe-ingredient-group">
          <h4 class="wprm-recipe-ingredient-group-name">Ragu</h4>
          <li class="wprm-recipe-ingredient">1 1/2 cups red wine, full bodied (like merlot, cabernet sauvignon), or any red not too sweet or woody (substitute 0% wine or more chicken stock for non alcoholic)</li>
        </div>
        <div class="wprm-recipe-ingredient-group">
          <h4 class="wprm-recipe-ingredient-group-name">FOR PASTA</h4>
          <li class="wprm-recipe-ingredient">500g / 1 lb pappardelle, mafaldine, rigatoni, capunti paesani ( or other shapes with shredded meat catching abilities! (Note 2))</li>
        </div>
        """
        soup = BeautifulSoup(html, "html.parser")
        ingredients_list = [
            "1 1/2 cups red wine",
            "500g / 1 lb pappardelle, mafaldine, rigatoni, capunti paesani ( or other shapes with shredded meat catching abilities! (Note 2))",
        ]

        groups = group_ingredients(ingredients_list, soup)
        flattened = [ing for g in groups for ing in g.ingredients]

        self.assertEqual(2, len(flattened))
        self.assertEqual(sorted(ingredients_list), sorted(flattened))
        ragu_group = next(g for g in groups if g.purpose == "Ragu")
        self.assertEqual(["1 1/2 cups red wine"], ragu_group.ingredients)
