# mypy: disallow_untyped_defs=False
from dataclasses import dataclass
from typing import Dict, List, Optional

from bs4 import BeautifulSoup

from ._utils import normalize_string


@dataclass
class IngredientGroup:
    ingredients: List[str]
    purpose: Optional[
        str
    ] = None  # this group of ingredients is {purpose} (e.g. "For the dressing")


def score_sentence_similarity(first: str, second: str) -> float:
    """Calculate Dice coefficient for two strings.

    The dice coefficient is a measure of similarity determined by calculating
    the proportion of shared bigrams.

    Parameters
    ----------
    first : str
        First string
    second : str
        Second string

    Returns
    -------
    float
        Similarity score between 0 and 1.
        0 means the two strings do not share any bigrams.
        1 means the two strings are identical.
    """

    if first == second:
        # Indentical sentences have maximum score of 1
        return 1

    if len(first) < 2 or len(second) < 2:
        # If either sentence has 0 or 1 character we can't generate bigrams,
        # so the score is 0
        return 0

    first_bigrams = set([first[i : i + 2] for i in range(len(first) - 1)])
    second_bigrams = set([second[i : i + 2] for i in range(len(second) - 1)])

    intersection = first_bigrams & second_bigrams

    return 2.0 * len(intersection) / (len(first_bigrams) + len(second_bigrams))


def best_match(test_string: str, target_strings: List[str]) -> str:
    """Find the best match for test_string in target_strings

    Parameters
    ----------
    test_string : str
        Test string to find the best match for.
    target_strings : List[str]
        List of target strings to search for best match in

    Returns
    -------
    str
        The closest matching string in target_strings to test_string

    """
    scores = [
        score_sentence_similarity(test_string, target) for target in target_strings
    ]
    # Get the index of the maximum score
    index, _ = max(enumerate(scores), key=lambda x: x[1])

    return target_strings[index]


def group_ingredients(
    ingredients_list: List[str],
    soup: BeautifulSoup,
    group_heading: str,
    group_element: str,
) -> List[IngredientGroup]:
    """
    Group ingredients into sublists according the heading in the recipe.

    The group headings are determined by html element matching the group_heading CSSselector.
    The group items are determined by extracting the text the html elements that are
    below the group heading, then matching the text to one of the ingredients in ingredients_list.
    This is done to ensure this function returns the same ingredients as are returned from
    the .ingredients() method of a scraper.

    If the recipe doesn't group ingredients, this returns a single IngredientGroup object
    with the purpose set to None and the ingredients list populated with all ingredients.

    Parameters
    ----------
    ingredients_list : List[str]
        List of ingredients extracted by recipe scraper
    soup : BeautifulSoup
        Parsed page HTML markup as BeautifulSoup object
    group_heading : str
        CSS selector for ingredient group heading
    group_element : str
        CSS selector for ingredient elements

    Returns
    -------
    List[IngredientGroup]
        List of IngredientGroup objects.
        Each object represents a group of ingredients and their purpose.

    Raises
    -------
    ValueError
        Raise ValueError is the number of ingredients found by the CSS selector does
        not match the number of ingredients in ingredients_list.
    """

    # Check the number of ingredients found in the HTML markup matches the
    # number in ingredients_list
    found_ingredients = soup.select(group_element)
    if len(found_ingredients) != len(ingredients_list):
        raise ValueError(
            f"Found {len(found_ingredients)} grouped ingredients but was expecting to find {len(ingredients_list)}."
        )

    groupings: Dict[Optional[str], List[str]] = {None: []}
    current_heading = None

    # Find all elemement matching the heading and ingredient selectors, in the order they appear
    # in the HTML markup
    elements = soup.select(",".join([group_heading, group_element]))
    for el in elements:
        if el in el.parent.select(group_heading):
            # This is the heading
            current_heading = normalize_string(el.get_text())
            groupings[current_heading] = []

        else:
            # This an ingredient string
            # Extract the text and find the best match in ingredients_list
            text = normalize_string(el.get_text())
            ingredient = best_match(text, ingredients_list)
            groupings[current_heading].append(ingredient)

    return [
        IngredientGroup(purpose=heading, ingredients=items)
        for heading, items in groupings.items()
        if items != []
    ]
