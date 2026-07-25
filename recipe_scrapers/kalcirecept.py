from ._abstract import AbstractScraper
from ._utils import normalize_string


class KalciRecept(AbstractScraper):
    @classmethod
    def host(cls):
        return "kalcirecept.hu"

    def site_name(self):
        og_site_name = self.soup.find("meta", {"property": "og:site_name"})
        if og_site_name:
            return og_site_name.get("content", "")
        return "Kálci receptjei"

    def title(self):
        h1 = self.soup.find("h1", class_="text-white")
        if h1:
            return normalize_string(h1.get_text())
        og_title = self.soup.find("meta", {"property": "og:title"})
        if og_title:
            title = og_title.get("content", "")
            sep = title.rfind(" - ")
            if sep != -1:
                title = title[:sep]
            return normalize_string(title)
        return None

    def image(self):
        og_image = self.soup.find("meta", {"property": "og:image"})
        if og_image:
            return og_image.get("content", "")
        return None

    def _find_heading(self, text):
        for h1 in self.soup.find_all("h1"):
            if h1.get_text(strip=True) == text:
                return h1
        return None

    def ingredients(self):
        heading = self._find_heading("Hozzávalók")
        if not heading:
            return []
        container = heading.find_next_sibling()
        if not container:
            return []
        ingredients = []
        for li in container.find_all("li"):
            spans = li.find_all("span")
            if spans:
                parts = [
                    normalize_string(s.get_text())
                    for s in spans
                    if s.get_text(strip=True)
                ]
                text = " ".join(parts)
                if text:
                    ingredients.append(text)
        return ingredients

    def instructions(self):
        heading = self._find_heading("A recept")
        if not heading:
            return ""
        container = heading.find_next_sibling()
        if not container:
            return ""
        steps = []
        for p in container.find_all("p"):
            text = normalize_string(p.get_text())
            if text:
                steps.append(text)
        return "\n".join(steps)
