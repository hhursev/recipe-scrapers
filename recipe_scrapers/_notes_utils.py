from __future__ import annotations

from bs4 import BeautifulSoup, Tag

from ._utils import normalize_string


def extract_notes(soup: BeautifulSoup) -> list[str]:
    """Extract recipe notes from common WordPress recipe plugin HTML formats.

    Supports:
    - WP Recipe Maker (WPRM): ``div.wprm-recipe-notes``
    - Tasty Recipes: ``div.tasty-recipes-notes``

    Returns an empty list when no recognised notes section is present.
    """
    wprm = soup.select_one(".wprm-recipe-notes")
    if wprm:
        return _extract_wprm_notes(wprm)

    tasty = soup.select_one(".tasty-recipes-notes")
    if tasty:
        return _extract_tasty_notes(tasty)

    return []


def _extract_wprm_notes(container: Tag) -> list[str]:
    """Extract notes from a WP Recipe Maker notes container.

    WPRM renders each note as a ``<span>`` that is a *direct* child of the
    container.  Using direct children (rather than ``find_all("span")``)
    avoids picking up spans from the nutrition label widget, which WPRM
    sometimes renders adjacent to the notes in the same recipe block.
    """
    notes = []
    for child in container.children:
        if getattr(child, "name", None) == "span":
            text = normalize_string(child.get_text())
            if text:
                notes.append(text)
    return notes


def _extract_tasty_notes(container: Tag) -> list[str]:
    """Extract notes from a Tasty Recipes notes container.

    Tasty Recipes renders notes as ``<p>`` paragraphs or ``<li>`` list items.
    """
    notes = []
    for element in container.find_all(["p", "li"]):
        text = normalize_string(element.get_text())
        if text:
            notes.append(text)
    return notes
