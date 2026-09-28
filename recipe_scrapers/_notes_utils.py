from __future__ import annotations

from dataclasses import dataclass

from bs4 import BeautifulSoup, Tag

from ._utils import normalize_string


@dataclass
class RecipeNote:
    title: str = ""
    text: str = ""


def _extract_note_from_element(element: Tag) -> RecipeNote | None:
    """Extract a RecipeNote from a single HTML element.

    If the element's first tag child is a <strong>, treat its text as the note
    title and use the remaining text as the body.  Returns None if the element
    has no meaningful content after normalisation.
    """
    # Work on a copy so we can safely decompose children without touching the tree.
    element = BeautifulSoup(str(element), "html.parser").find()

    first_tag_child = next(
        (c for c in element.children if getattr(c, "name", None)), None
    )
    title = ""
    if first_tag_child and first_tag_child.name == "strong":
        title = normalize_string(first_tag_child.get_text())
        first_tag_child.decompose()

    text = normalize_string(element.get_text())
    if not text and not title:
        return None

    return RecipeNote(title=title, text=text)


def extract_notes(soup: BeautifulSoup) -> list[RecipeNote]:
    """Extract recipe notes from common WordPress recipe plugin HTML formats.

    Supports:
    - WP Recipe Maker (WPRM): ``div.wprm-recipe-notes``
    - Tasty Recipes: ``div.tasty-recipes-notes``

    Returns an empty list when no recognised notes section is present.

    Background
    ----------
    Neither plugin reliably publishes notes in its JSON-LD output, so
    this function falls back to HTML extraction.  WPRM renders each note
    as a ``<span style="display: block;">`` direct child of the container,
    separated by ``<div class="wprm-spacer">`` elements.  Tasty Recipes
    uses ``<p>`` or ``<li>`` elements inside its container.
    """
    wprm = soup.select_one(".wprm-recipe-notes")
    if wprm:
        return _extract_wprm_notes(wprm)

    tasty = soup.select_one(".tasty-recipes-notes")
    if tasty:
        return _extract_tasty_notes(tasty)

    return []


def _extract_wprm_notes(container: Tag) -> list[RecipeNote]:
    """Extract notes from a WP Recipe Maker notes container.

    WPRM renders each note as a ``<span>`` that is a *direct* child of the
    container.  Using direct children (rather than ``soup.find_all("span")``)
    avoids picking up spans from the nutrition label widget, which WPRM
    sometimes renders adjacent to the notes in the same recipe block.
    """
    notes = []
    direct_spans = [
        child for child in container.children if getattr(child, "name", None) == "span"
    ]
    for span in direct_spans:
        note = _extract_note_from_element(span)
        if note:
            notes.append(note)
    return notes


def _extract_tasty_notes(container: Tag) -> list[RecipeNote]:
    """Extract notes from a Tasty Recipes notes container.

    Tasty Recipes renders notes as ``<p>`` paragraphs or ``<li>`` list items.
    Each element becomes a separate note.  A leading ``<strong>`` tag is used
    as the title when present, consistent with the WPRM approach.
    """
    notes = []
    for element in container.find_all(["p", "li"]):
        note = _extract_note_from_element(element)
        if note:
            notes.append(note)
    return notes
