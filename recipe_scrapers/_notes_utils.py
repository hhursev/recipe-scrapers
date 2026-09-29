from __future__ import annotations

from bs4 import BeautifulSoup, Tag

from ._utils import normalize_string

NOTE_ELEMENTS = ("span", "p", "ul", "ol", "li")


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


def _collect(element: Tag, notes: list[str]) -> None:
    """Append the note text of ``element`` to ``notes``.

    Lists contribute one note per *leaf* list item.  Block editors nest lists
    inside a wrapper ``<li>``, and the wrapper's text already contains the text
    of the items below it, so only leaves are collected to avoid duplicates.
    """
    if element.name in ("ul", "ol"):
        for item in element.find_all("li"):
            if item.find(["li", "p"]):
                continue
            _collect_text(item, notes)
    else:
        _collect_text(element, notes)


def _collect_text(element: Tag, notes: list[str]) -> None:
    text = normalize_string(element.get_text())
    if text:
        notes.append(text)


def _extract_wprm_notes(container: Tag) -> list[str]:
    """Extract notes from a WP Recipe Maker notes container.

    WPRM renders notes as ``<span>`` elements or as a list, in both cases as
    *direct* children of the container.  Restricting to direct children (rather
    than searching the whole subtree) avoids picking up the nutrition label
    widget, which WPRM sometimes renders as a ``<div>`` in the same container.
    """
    notes: list[str] = []
    for child in container.children:
        if isinstance(child, Tag) and child.name in NOTE_ELEMENTS:
            _collect(child, notes)
    return notes


def _extract_tasty_notes(container: Tag) -> list[str]:
    """Extract notes from a Tasty Recipes notes container.

    Tasty Recipes renders notes as ``<p>`` paragraphs or ``<li>`` list items.
    """
    notes: list[str] = []
    for element in container.find_all(["p", "li"]):
        if element.find(["p", "li"]):
            continue
        _collect_text(element, notes)
    return notes
