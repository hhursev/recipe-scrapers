from urllib.parse import urljoin

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class Billa(AbstractScraper):
    @classmethod
    def host(cls):
        return "billa.at"

    def site_name(self):
        try:
            return self.schema.site_name()
        except Exception:
            return "BILLA"

    def author(self):
        try:
            author = self.schema.author()
            if author:
                return author
        except Exception:
            pass
        return "BILLA AG"

    def title(self):
        try:
            title = self.schema.title()
            if title:
                return title
        except Exception:
            pass

        h1 = self.soup.find("h1")
        if h1:
            return normalize_string(h1.get_text(" ", strip=True))

        if self.soup.title and self.soup.title.string:
            raw_title = normalize_string(self.soup.title.string)
            return raw_title.split("|")[0].strip()

        return None

    def ingredients(self):
        try:
            ingredients = self.schema.ingredients()
            if ingredients:
                return ingredients
        except Exception:
            pass

        items = []
        for li in self.soup.select(".ws-recipe-ingredients li"):
            text = normalize_string(li.get_text(" ", strip=True))
            if text:
                items.append(text)

        if items:
            return items

        # Generic fallback
        for li in self.soup.select("main ul li"):
            text = normalize_string(li.get_text(" ", strip=True))
            if text:
                items.append(text)

        return items

    def instructions(self):
        try:
            instructions = self.schema.instructions()
            if instructions:
                return instructions
        except Exception:
            pass

        steps = []
        for node in self.soup.select(".ws-recipe-steps__description"):
            text = normalize_string(node.get_text(" ", strip=True))
            if text:
                steps.append(text)

        if steps:
            return "\n".join(steps)

        # Generic ordered-list fallback
        ol = self.soup.select_one("main ol")
        if ol:
            items = [
                normalize_string(li.get_text(" ", strip=True))
                for li in ol.find_all("li")
            ]
            items = [x for x in items if x]
            if items:
                return "\n".join(items)

        return None

    def yields(self):
        try:
            yields_value = self.schema.yields()
            if yields_value:
                return yields_value
        except Exception:
            pass

        quantity_input = self.soup.select_one(
            '.ws-select-quantity__container__input[aria-label="Portionen"]'
        ) or self.soup.select_one(".ws-select-quantity__container__input")

        if quantity_input:
            value = quantity_input.get("value")
            if value:
                return get_yields(value)

        # Last-resort fallback from visible text
        for node in self.soup.select(".ws-recipe-ingredients-serving-calculator__item"):
            text = normalize_string(node.get_text(" ", strip=True))
            if any(ch.isdigit() for ch in text):
                return get_yields(text)

        return None

    def total_time(self):
        try:
            total = self.schema.total_time()
            if total:
                return total
        except Exception:
            pass

        preferred_labels = ("fertig", "gesamt", "total")

        for node in self.soup.select(".ws-recipe-time"):
            text = normalize_string(node.get_text(" ", strip=True)).lower()
            if any(label in text for label in preferred_labels):
                minutes = get_minutes(text)
                if minutes:
                    return minutes

        for node in self.soup.select(".ws-recipe-time"):
            text = normalize_string(node.get_text(" ", strip=True))
            minutes = get_minutes(text)
            if minutes:
                return minutes

        return None

    def image(self):
        try:
            image = self.schema.image()
            if image:
                return urljoin(self.url, image)
        except Exception:
            pass

        try:
            image = self.opengraph.image()
            if image:
                return urljoin(self.url, image)
        except Exception:
            pass

        img = self.soup.select_one(".ws-recipe-slug__image img")
        if img:
            src = (
                img.get("src")
                or img.get("data-src")
                or img.get("data-original")
                or img.get("currentSrc")
            )
            if src:
                return urljoin(self.url, src)

        return None
