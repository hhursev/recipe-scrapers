from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass

from bs4 import BeautifulSoup

from ._utils import normalize_string


def normalize_fractions(text: str) -> str:
    """Normalize Unicode fractions to ASCII fractions for consistent matching.

    This function converts Unicode fraction characters (like ½, ¼, ¾) to their
    ASCII equivalents (like 1/2, 1/4, 3/4) to ensure consistent matching
    in ingredient grouping.

    Parameters
    ----------
    text : str
        The text string that may contain Unicode fractions.

    Returns
    -------
    str
        The text with Unicode fractions converted to ASCII fractions.
    """
    fraction_map = {
        "½": "1/2",
        "⅓": "1/3",
        "⅔": "2/3",
        "¼": "1/4",
        "¾": "3/4",
        "⅕": "1/5",
        "⅖": "2/5",
        "⅗": "3/5",
        "⅘": "4/5",
        "⅙": "1/6",
        "⅚": "5/6",
        "⅛": "1/8",
        "⅜": "3/8",
        "⅝": "5/8",
        "⅞": "7/8",
    }

    for unicode_frac, ascii_frac in fraction_map.items():
        text = text.replace(unicode_frac, ascii_frac)

    return text


DEFAULT_GROUPINGS: list[tuple[str, list[str], list[str]]] = [
    (
        "wprm",
        [
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-group-name",
        ],
        [
            ".wprm-recipe-ingredient",
            ".wprm-recipe-ingredients li",
        ],
    ),
    (
        "tasty",
        [
            ".tasty-recipes-ingredients-body p strong",
            ".tasty-recipes-ingredients h4",
        ],
        [
            ".tasty-recipes-ingredients-body ul li",
            ".tasty-recipes-ingredients ul li",
        ],
    ),
]


@dataclass
class IngredientGroup:
    ingredients: list[str]
    purpose: str | None = (
        None  # this group of ingredients is {purpose} (e.g. "For the dressing")
    )


def score_sentence_similarity(first: str, second: str) -> float:
    """Calculate Dice coefficient for two strings.

    The dice coefficient is a measure of similarity that accounts for
    the length of the strings, determined by the proportion of shared bigrams. This normalization
    ensures the score is less biased towards shorter strings.

    Parameters
    ----------
    first : str
        The first input string.
    second : str
        The second input string.

    Returns
    -------
    float
        The similarity score between 0 and 1, where 0 indicates no shared bigrams and
        1 indicates identical strings.
    """

    if first == second:
        return 1

    if len(first) < 2 or len(second) < 2:
        return 0

    first_bigrams = {first[i : i + 2] for i in range(len(first) - 1)}
    second_bigrams = {second[i : i + 2] for i in range(len(second) - 1)}

    intersection = len(first_bigrams & second_bigrams)

    return 2 * intersection / (len(first_bigrams) + len(second_bigrams))


def best_match(test_string: str, target_strings: list[str]) -> str:
    """Find the best match for a given test string within a list of target strings.

    This function utilizes the score_sentence_similarity function to compare the test string
    against each target string. The target string with the highest similarity score to the
    test string is returned as the best match. Fractions are normalized to ensure consistent
    matching between Unicode and ASCII fraction representations.

    Parameters
    ----------
    test_string : str
        The string to find the best match for.
    target_strings : list[str]
        A list of strings to compare against the test string.

    Returns
    -------
    str
        The string from target_strings that has the highest similarity score with test_string.
    """
    normalized_test = normalize_fractions(test_string)
    normalized_targets = [normalize_fractions(target) for target in target_strings]

    scores = [
        score_sentence_similarity(normalized_test, target)
        for target in normalized_targets
    ]
    best_match_index = max(range(len(scores)), key=scores.__getitem__)

    return target_strings[best_match_index]


def group_ingredients(
    ingredients_list: list[str],
    soup: BeautifulSoup,
    group_heading: str | None = None,
    group_element: str | None = None,
) -> list[IngredientGroup]:
    """
    Group ingredients into sublists according to the heading in the recipe.

    This method groups ingredients by extracting headings and corresponding elements
    based on provided CSS selectors. If no groupings are present, it creates a single
    group with all ingredients. It ensures ingredient groupings match those in
    the .ingredients() method of a scraper by comparing the text against the ingredients list.

    If no selectors are provided, it attempts to auto-detect grouping selectors
    from known defaults.

    Parameters
    ----------
    ingredients_list : list[str]
        Ingredients extracted by the scraper.
    soup : BeautifulSoup
        Parsed HTML of the recipe page.
    group_heading : str | None
        CSS selector for ingredient group headings. If None, auto-detection is attempted.
    group_element : str | None
        CSS selector for ingredient list items. If None, auto-detection is attempted.

    Returns
    -------
    list[IngredientGroup]
        groupings of ingredients categorized by their purpose or heading.

    Raises
    -------
    ValueError
        If the number of elements selected does not match the length of ingredients_list.
    """

    if group_heading is None or group_element is None:
        for _, heading_opts, element_opts in DEFAULT_GROUPINGS:
            for heading_sel in heading_opts:
                for element_sel in element_opts:
                    if soup.select(heading_sel) and soup.select(element_sel):
                        group_heading = heading_sel
                        group_element = element_sel
                        break
                if group_heading and group_element:
                    break
            if group_heading and group_element:
                break

    if not group_heading or not group_element:
        return [IngredientGroup(ingredients=ingredients_list)]

    found_ingredients = soup.select(group_element)
    if len(found_ingredients) != len(ingredients_list):
        raise ValueError(
            f"Found {len(found_ingredients)} grouped ingredients but was expecting to find {len(ingredients_list)}."
        )

    groupings: dict[str | None, list[str]] = defaultdict(list)
    current_heading: str | None = None
    elements = soup.select(f"{group_heading}, {group_element}")
    for element in elements:
        if element in element.parent.select(group_heading):
            current_heading = normalize_string(element.get_text()) or None
            if current_heading not in groupings:
                groupings[current_heading] = []
        else:
            ingredient_text = normalize_string(element.get_text())
            matched_ingredient = best_match(ingredient_text, ingredients_list)
            groupings[current_heading].append(matched_ingredient)

    return [
        IngredientGroup(purpose=heading, ingredients=items)
        for heading, items in groupings.items()
        if items
    ]
