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

    - A non-list element (``<span>``, ``<p>``, ...): its whole text becomes
      one note.
    - A ``<ul>``/``<ol>``: each *leaf* ``<li>`` becomes one note.
    - A wrapper ``<li>`` (one that nests another ``<li>`` or ``<p>``, as block
      editors do for a sub-list): its own leading text (e.g. a label
      introducing the sub-list) becomes a separate note; the nested items are
      collected as their own leaves rather than duplicating them via the
      wrapper's full ``get_text()``.
    """
    if element.name in ("ul", "ol"):
        for item in element.find_all("li"):
            if item.find(["li", "p"]):
                own_text = normalize_string(
                    "".join(item.find_all(string=True, recursive=False))
                )
                if own_text:
                    notes.append(own_text)
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

    WPRM's markup varies by site, so each child of the container is handled
    according to what it is:

    - ``<span>``, ``<p>``, ``<ul>``, ``<ol>`` or ``<li>``: collected directly
      as a note (see ``_collect``).
    - A plain ``<div>`` (block editors like Gutenberg often wrap notes in
      one): unwrapped, and its own children are handled by these same rules.
    - A ``<div>`` with no block-level note structure inside it (just text, or
      only inline formatting like ``<em>``/``<strong>``/``<a>``): treated as
      a single leaf note, collecting all of its text.
    - A ``<div>`` identified as the nutrition label widget or a section
      header (by class name), which WPRM sometimes renders inside the same
      container: skipped entirely so its contents aren't picked up as notes.
    """
    notes: list[str] = []
    _collect_wprm_notes(container, notes)
    return notes


def _collect_wprm_notes(container: Tag, notes: list[str]) -> None:
    for child in container.children:
        if not isinstance(child, Tag):
            continue
        if child.name in NOTE_ELEMENTS:
            _collect(child, notes)
        elif child.name == "div" and not _is_non_note_widget(child):
            if child.find(NOTE_ELEMENTS + ("div",)):
                _collect_wprm_notes(child, notes)
            else:
                _collect_text(child, notes)


def _is_non_note_widget(element: Tag) -> bool:
    classes = element.get("class", [])
    return any("nutrition" in cls or "header" in cls for cls in classes)


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
