from __future__ import annotations

from typing import Any

from ._abstract import AbstractScraper
from ._exceptions import FieldNotProvidedByWebsiteException
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class SiteRecipeFallbackScraper(AbstractScraper):
    """Schema-first scraper with common recipe-card HTML fallbacks."""

    _site_name: str | None = None

    _ingredient_selectors = (
        ".wprm-recipe-ingredient",
        ".tasty-recipes-ingredients li",
        "[itemprop='recipeIngredient']",
        ".recipe-ingredients li",
        ".recipe__ingredients li",
        ".ingredients li",
        ".ingredient-list li",
        ".ingredient-list__item",
        ".ingredients-section li",
        ".mntl-structured-ingredients__list-item",
    )

    _instruction_selectors = (
        ".wprm-recipe-instruction",
        ".tasty-recipes-instructions li",
        "[itemprop='recipeInstructions'] li",
        ".recipe-instructions li",
        ".recipe__instructions li",
        ".instructions li",
        ".method li",
        ".directions li",
        ".preparation-step",
        ".instruction",
        ".step",
    )

    def _schema_or_none(self, method_name: str) -> Any:
        try:
            value = getattr(self.schema, method_name)()
            if value not in (None, "", []):
                return value
        except Exception:
            return None
        return None

    def _first_meta(self, *selectors: tuple[str, dict[str, str]]) -> str | None:
        for name, attrs in selectors:
            tag = self.soup.find(name, attrs)
            if tag and tag.get("content"):
                return normalize_string(tag["content"])
        return None

    def _select_texts(self, selectors: tuple[str, ...]) -> list[str]:
        seen: set[str] = set()
        values: list[str] = []
        for selector in selectors:
            for element in self.soup.select(selector):
                text = normalize_string(element.get_text(" ", strip=True))
                if len(text) < 2 or text.lower() in seen:
                    continue
                seen.add(text.lower())
                values.append(text)
            if values:
                return values
        return values

    def site_name(self):
        if self._site_name:
            return self._site_name
        return self._schema_or_none("site_name") or self.host()

    def title(self):
        h1 = self.soup.find("h1")
        return (
            self._schema_or_none("title")
            or self._first_meta(
                ("meta", {"property": "og:title"}),
                ("meta", {"name": "twitter:title"}),
            )
            or (normalize_string(h1.get_text(" ", strip=True)) if h1 else None)
        )

    def ingredients(self):
        return self._schema_or_none("ingredients") or self._select_texts(
            self._ingredient_selectors
        )

    def ingredient_groups(self):
        return group_ingredients(self.ingredients(), self.soup)

    def instructions(self):
        instructions = self._schema_or_none("instructions")
        if instructions:
            return instructions
        return "\n".join(self._select_texts(self._instruction_selectors))

    def yields(self):
        return self._schema_or_none("yields") or self._first_serving_text()

    def image(self):
        return self._schema_or_none("image") or self._first_meta(
            ("meta", {"property": "og:image"}),
            ("meta", {"name": "twitter:image"}),
        )

    def author(self):
        author = self._schema_or_none("author")
        if author:
            return author
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def category(self):
        return self._schema_or_none("category")

    def total_time(self):
        return self._schema_or_none("total_time")

    def cook_time(self):
        return self._schema_or_none("cook_time")

    def prep_time(self):
        return self._schema_or_none("prep_time")

    def cuisine(self):
        return self._schema_or_none("cuisine")

    def description(self):
        return self._schema_or_none("description") or self._first_meta(
            ("meta", {"property": "og:description"}),
            ("meta", {"name": "description"}),
        )

    def _first_serving_text(self) -> str | None:
        selectors = (
            ".wprm-recipe-servings",
            ".tasty-recipes-yield",
            "[class*='serving']",
            "[class*='yield']",
        )
        values = self._select_texts(selectors)
        return values[0] if values else None
