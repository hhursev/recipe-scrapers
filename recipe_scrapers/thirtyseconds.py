import json
import re

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class ThirtySeconds(AbstractScraper):
    """Scraper for 30seconds.com (30Seconds Food).

    Most recipe pages expose only an ``Article`` schema, with the recipe itself
    living in the page markup: an ``Ingredients`` list (a ``<ul>`` that follows a
    ``<strong>Ingredients</strong>`` header, or — on pages without that header —
    the ``<ul>`` right after the ``Servings:`` line) and a directions ``<ol>``
    that follows a "Here's how to make it" / "Directions" header. Some pages also
    carry a full ``Recipe`` schema; where that exists the SchemaOrg plugin covers
    it, but these overrides parse the markup so both layouts work.
    """

    @classmethod
    def host(cls):
        return "30seconds.com"

    def _article(self):
        """First JSON-LD node carrying a name/headline (the Article, usually)."""
        if getattr(self, "_article_cache", None) is not None:
            return self._article_cache
        node = {}
        for block in re.findall(
            r"<script[^>]+type=['\"]application/ld\+json['\"][^>]*>(.*?)</script>",
            self.page_data,
            re.S,
        ):
            try:
                obj = json.loads(block)
            except json.JSONDecodeError:
                continue
            for candidate in obj if isinstance(obj, list) else [obj]:
                if isinstance(candidate, dict) and (
                    candidate.get("name") or candidate.get("headline")
                ):
                    node = candidate
                    break
            if node:
                break
        self._article_cache = node
        return node

    def author(self):
        author = self._article().get("author")
        if isinstance(author, list):
            author = author[0] if author else None
        if isinstance(author, dict):
            return author.get("name")
        return author

    def title(self):
        article = self._article()
        return normalize_string(article.get("name") or article.get("headline") or "")

    def site_name(self):
        return self.opengraph.site_name()

    def image(self):
        image = self._article().get("image")
        if isinstance(image, list):
            image = image[0] if image else None
        if isinstance(image, dict):
            image = image.get("url")
        return image or self.opengraph.image()

    def total_time(self):
        match = re.search(r"Total Time:\s*([^<\n]+)", self.page_data, re.I)
        return get_minutes(match.group(1)) if match else 0

    def yields(self):
        match = re.search(r"Servings:\s*([0-9]+)", self.page_data, re.I)
        return get_yields(f"{match.group(1)} servings") if match else None

    def _directions_ol(self):
        return re.search(
            r"(?:Here.{0,4}s how to make it|Directions|Instructions|Method|Steps)\b"
            r".*?<ol>(.*?)</ol>",
            self.page_data,
            re.S | re.I,
        )

    def ingredients(self):
        start = re.search(
            r"<strong>\s*Ingredients\s*</strong>", self.page_data, re.I
        ) or re.search(r"Servings:.*?</p>", self.page_data, re.S | re.I)
        if not start:
            return []
        directions = self._directions_ol()
        end = directions.start() if directions else len(self.page_data)
        ordered = self.page_data.find("<ol", start.end())
        if ordered != -1:
            end = min(end, ordered)
        items = re.findall(r"<li>(.*?)</li>", self.page_data[start.end() : end], re.S)
        return [i for i in (normalize_string(item) for item in items) if i]

    def instructions(self):
        directions = self._directions_ol()
        if not directions:
            return ""
        items = re.findall(r"<li>(.*?)</li>", directions.group(1), re.S)
        return "\n".join(i for i in (normalize_string(item) for item in items) if i)
