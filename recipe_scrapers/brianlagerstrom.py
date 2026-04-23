from ._abstract import AbstractScraper
from ._utils import normalize_string


class BrianLagerstrom(AbstractScraper):
    @classmethod
    def host(cls):
        return "brianlagerstrom.com"

    def site_name(self):
        return "Brian Lagerstrom"

    def author(self):
        return "Brian Lagerstrom"

    def title(self):
        og_title = self.soup.find("meta", {"property": "og:title"})
        if og_title:
            title = og_title.get("content", "")
            sep = title.rfind(" \u2014 ")
            if sep != -1:
                title = title[:sep]
            return normalize_string(title)
        return None

    def image(self):
        og_image = self.soup.find("meta", {"property": "og:image"})
        if og_image:
            url = og_image.get("content", "")
            if url.startswith("//"):
                url = "https:" + url
            return url
        return None

    def _recipe_content(self):
        for div in self.soup.find_all("div", class_="sqs-html-content"):
            if "\u25aa" in div.get_text():
                return div
        return None

    def ingredients(self):
        html_content = self._recipe_content()
        if not html_content:
            return []
        for p in html_content.find_all("p"):
            text = p.get_text()
            if "\u25aa" in text:
                items = [
                    normalize_string(item)
                    for item in text.split("\u25aa")
                    if normalize_string(item)
                ]
                return items
        return []

    def instructions(self):
        html_content = self._recipe_content()
        if not html_content:
            return ""
        paragraphs = html_content.find_all("p")
        ingredient_idx: int | None = None
        for i, p in enumerate(paragraphs):
            if "\u25aa" in p.get_text():
                ingredient_idx = i
                break
        if ingredient_idx is None:
            return ""
        steps = []
        for p in paragraphs[ingredient_idx + 1 :]:
            text = normalize_string(p.get_text())
            if not text:
                continue
            if text.startswith("**"):
                continue
            steps.append(text)
        return "\n".join(steps)
