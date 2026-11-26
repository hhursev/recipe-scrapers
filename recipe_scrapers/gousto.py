from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from typing import Any
from urllib.parse import urlparse

from ._abstract import AbstractScraper


class _HTMLStripper(HTMLParser):
    """Minimal HTML-to-text converter that preserves paragraph breaks."""

    _BLOCK_TAGS = {"p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "br", "li"}

    def __init__(self) -> None:
        super().__init__()
        self._parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in self._BLOCK_TAGS:
            self._parts.append("\n")

    def handle_data(self, data: str) -> None:
        self._parts.append(data)

    def get_text(self) -> str:
        return "".join(self._parts)


def _strip_html(html: str) -> str:
    """Remove HTML tags and return plain text, preserving paragraph breaks."""
    stripper = _HTMLStripper()
    stripper.feed(html)
    text = stripper.get_text()
    text = re.sub(r"[ \t]+", " ", text)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)


def _pick_largest_image(images: list[dict[str, Any]]) -> str | None:
    """Return the URL of the largest image, or None."""
    if not images:
        return None
    best = max(images, key=lambda img: img.get("width", 0))
    return best.get("image")


def _mg_to_g(milligrams: int) -> float:
    """Convert milligrams to grams."""
    return round(milligrams / 1000, 1)


class Gousto(AbstractScraper):
    """Gousto scraper — fetches recipe data from the Gousto API.

    Gousto is a React/Next.js SPA that renders recipes dynamically.
    The HTML shell contains no recipe data, so we extract the slug from
    the URL and call the Gousto CMS API instead.

    Falls back to JSON-LD in HTML when no valid recipe URL is provided
    (e.g. during offline testing with static HTML).
    """

    @classmethod
    def host(cls) -> str:
        return "gousto.co.uk"

    def __init__(self, html: str, url: str, **kwargs: Any) -> None:
        super().__init__(html, url, **kwargs)

        self._api_data: dict[str, Any] | None = None

        # Derive slug from URL: /cookbook/.../<slug> or /recipes/<slug>
        parsed = urlparse(url)
        path = parsed.path
        slug = path.rstrip("/").split("/")[-1] if path else ""

        # Only call API if we have a real recipe URL with a slug
        if slug and parsed.netloc:
            api_url = (
                f"https://production-api.gousto.co.uk/cmsreadbroker/v1/recipe/{slug}"
            )
            try:
                import urllib.request

                with urllib.request.urlopen(api_url) as response:
                    raw: dict[str, Any] = json.loads(response.read().decode("utf-8"))
                if raw.get("status") == "ok":
                    self._api_data = raw["data"]["entry"]
            except Exception:
                pass

    def _entry(self) -> dict[str, Any]:
        if self._api_data is None:
            raise ValueError("Gousto API returned no data")
        return self._api_data

    def author(self) -> str:
        if self._api_data:
            return "Gousto"
        return self.schema.author()

    def title(self) -> str:
        if self._api_data:
            return self._entry().get("title", "")
        return self.schema.title()

    def description(self) -> str:
        if self._api_data:
            return self._entry().get("description", "")
        return self.schema.description()

    def image(self) -> str:
        if self._api_data:
            entry = self._entry()
            img = _pick_largest_image(entry.get("media", {}).get("images", []))
            if img:
                return img
            return entry.get("seo", {}).get("open_graph_image", "")
        return self.schema.image()

    def canonical_url(self) -> str:
        if self._api_data:
            return self._entry().get("seo", {}).get("canonical", "")
        return super().canonical_url()

    def cuisine(self) -> str:
        if self._api_data:
            return self._entry().get("cuisine", {}).get("title", "")
        return self.schema.cuisine()

    def category(self) -> str:
        if self._api_data:
            categories = self._entry().get("categories", [])
            for cat in reversed(categories):
                title = cat.get("title", "").strip()
                if title and title != "All Gousto Recipes":
                    return title
            return ""
        return self.schema.category()

    def total_time(self) -> int:
        if self._api_data:
            entry = self._entry()
            prep_times: dict[str, int] = entry.get("prep_times", {})
            if not prep_times:
                return 0
            return prep_times.get("for_2", max(prep_times.values(), default=0))
        return self.schema.total_time()

    def yields(self) -> str:
        if self._api_data:
            entry = self._entry()
            portion_sizes: list[dict[str, Any]] = entry.get("portion_sizes", [])
            offered = [p["portions"] for p in portion_sizes if p.get("is_offered")]
            servings = 2 if 2 in offered else (min(offered) if offered else 2)
            return f"{servings} serving{'s' if servings != 1 else ''}"
        return self.schema.yields()

    def ingredients(self) -> list[str]:
        if self._api_data:
            return [ing["label"] for ing in self._entry().get("ingredients", [])]
        return self.schema.ingredients()

    def instructions(self) -> str:
        if self._api_data:
            steps = self._entry().get("cooking_instructions", [])
            steps_sorted = sorted(steps, key=lambda s: s.get("order", 0))
            texts = [_strip_html(s["instruction"]) for s in steps_sorted]
            return "\n".join(texts)
        return self.schema.instructions()

    def ratings(self) -> float:
        if self._api_data:
            rating = self._entry().get("rating", {})
            return rating.get("average", 0.0)
        return self.schema.ratings()

    def nutrients(self) -> dict[str, str]:
        if self._api_data:
            nutrition = (
                self._entry().get("nutritional_information", {}).get("per_portion", {})
            )
            result: dict[str, str] = {}
            if nutrition.get("energy_kcal"):
                result["calories"] = f"{nutrition['energy_kcal']} calories"
            if nutrition.get("fat_mg"):
                result["fatContent"] = f"{_mg_to_g(nutrition['fat_mg'])}g"
            if nutrition.get("carbs_mg"):
                result["carbohydrateContent"] = f"{_mg_to_g(nutrition['carbs_mg'])}g"
            if nutrition.get("carbs_sugars_mg"):
                result["sugarContent"] = f"{_mg_to_g(nutrition['carbs_sugars_mg'])}g"
            if nutrition.get("fibre_mg"):
                result["fiberContent"] = f"{_mg_to_g(nutrition['fibre_mg'])}g"
            if nutrition.get("protein_mg"):
                result["proteinContent"] = f"{_mg_to_g(nutrition['protein_mg'])}g"
            if nutrition.get("salt_mg"):
                result["sodiumContent"] = f"{_mg_to_g(nutrition['salt_mg'])}g"
            return result
        return self.schema.nutrients()
