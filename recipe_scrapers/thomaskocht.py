import re

from ._abstract import AbstractScraper
from ._utils import normalize_string


class ThomasKocht(AbstractScraper):
    @classmethod
    def host(cls):
        return "thomas-kocht.de"

    def author(self):
        return "Thomas Kocht"

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        info = self._info_paragraph()
        if not info:
            return self.schema.total_time()
        prep = re.search(r"Vorbereitungszeit:\s*(\d+)\s*Minuten", info)
        cook = re.search(r"Kochzeit:\s*(\d+)\s*Minuten", info)
        total = 0
        if prep:
            total += int(prep.group(1))
        if cook:
            total += int(cook.group(1))
        return total or None

    def yields(self):
        info = self._info_paragraph()
        if not info:
            return self.schema.yields()
        match = re.search(r"Ergibt\s+(.+?)(?:\||$)", info)
        if match:
            return normalize_string(match.group(1))
        return None

    def image(self):
        return self.schema.image()

    def ingredients(self):
        heading = self.soup.find(
            "h3", string=lambda t: t and t.strip().startswith("Zutaten")
        )
        if not heading:
            return self.schema.ingredients()
        ul = heading.find_next_sibling("ul")
        if not ul:
            return self.schema.ingredients()
        return [
            normalize_string(li.get_text())
            for li in ul.find_all("li")
            if li.get_text(strip=True)
        ]

    def instructions(self):
        steps = []
        for title_div in self.soup.find_all("div", class_="fusion-title"):
            h2 = title_div.find("h2")
            if not h2:
                continue
            if not re.match(r"Schritt\s+\d+", h2.get_text(strip=True)):
                continue
            for sibling in title_div.next_siblings:
                if not hasattr(sibling, "name") or not sibling.name:
                    continue
                classes = sibling.get("class", [])
                if any("fusion-text" in c for c in classes):
                    step_parts = []
                    h4 = sibling.find("h4")
                    if h4:
                        step_parts.append(normalize_string(h4.get_text()))
                    for p in sibling.find_all("p"):
                        text = normalize_string(p.get_text())
                        if text:
                            step_parts.append(text)
                    if step_parts:
                        steps.append(" ".join(step_parts))
                    break
                if sibling.name == "div" and any("fusion-title" in c for c in classes):
                    break
        return "\n".join(steps)

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()

    def site_name(self):
        return self.schema.site_name()

    def _info_paragraph(self):
        for p in self.soup.find_all("p"):
            text = p.get_text(strip=True)
            if "Vorbereitungszeit" in text or "Kochzeit" in text:
                return text
        return None
