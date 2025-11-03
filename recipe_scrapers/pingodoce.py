import re
import html
from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields


class PingoDoce(AbstractScraper):
    @classmethod
    def host(cls):
        return "pingodoce.pt"

    def site_name(self):
        return "Pingo Doce"

    def language(self):
        return "pt-PT"

    # -------------------------------------------------------------------------
    # Internal text cleaner
    # -------------------------------------------------------------------------
    def _clean_text(self, text):
        if not text:
            return ""
        return html.unescape(text.strip())

    # -------------------------------------------------------------------------
    # Core fields
    # -------------------------------------------------------------------------
    def author(self):
        author_tag = self.soup.find("div", class_="recipe-chef-link")
        if author_tag:
            return self._clean_text(author_tag.get_text())
        return "Equipa Sabe Bem"

    def title(self):
        h1 = self.soup.find("h1", class_="recipe-title")
        if h1:
            return self._clean_text(h1.get_text())
        meta_title = self.soup.find("meta", property="og:title")
        if meta_title:
            return self._clean_text(meta_title.get("content"))
        return None

    def description(self):
        meta = self.soup.find("meta", {"name": "description"})
        if meta and meta.get("content"):
            return self._clean_text(meta["content"])
        intro = self.soup.find("div", class_="recipe-intro-text")
        if intro:
            return self._clean_text(intro.get_text(" ", strip=True))
        title = self.title() or "Receita"
        return f"{title} — uma deliciosa receita do Pingo Doce."

    def category(self):
        breadcrumb = self.soup.find("ul", class_="breadcrumbs-area")
        if breadcrumb:
            links = breadcrumb.find_all("a")
            if len(links) >= 2:
                return self._clean_text(links[-1].get_text())
        return None

    # -------------------------------------------------------------------------
    # Time and Yield
    # -------------------------------------------------------------------------
    def total_time(self):
        time_div = self.soup.find("div", class_="recipe-area-short-info")
        if not time_div:
            return 0
        text = time_div.get_text(" ", strip=True)
        match = re.search(r"(\d+)\s*min", text)
        if match:
            return get_minutes(match.group(0))
        return 0

    def prep_time(self):
        # prep time is the only visible time
        return self.total_time()

    def cook_time(self):
        return 0

    def yields(self):
        info = self.soup.find("div", class_="recipe-area-short-info")
        if not info:
            return None
        match = re.search(r"(\d+)\s*(?:doses|porções?)", info.get_text(" ", strip=True), re.I)
        if match:
            return f"{match.group(1)} doses"
        return None

    # -------------------------------------------------------------------------
    # Ingredients
    # -------------------------------------------------------------------------
    def ingredients(self):
        ingredients = []
        blocks = self.soup.select("div.js-recipe-ingredient")
        for item in blocks:
            qty = item.select_one(".recipe-ingredient-description-content-quantity")
            name = item.select_one(".recipe-ingredient-description-content-name")
            parts = [
                self._clean_text(qty.get_text()) if qty else "",
                self._clean_text(name.get_text()) if name else "",
            ]
            text = " ".join([p for p in parts if p])
            if text:
                ingredients.append(text)
        return ingredients

    # -------------------------------------------------------------------------
    # Instructions
    # -------------------------------------------------------------------------
    def instructions(self):
        steps = []
        step_blocks = self.soup.select("div.recipe-step-content")
        for s in step_blocks:
            text = self._clean_text(s.get_text(" ", strip=True))
            if text:
                steps.append(text)
        return "\n".join(steps)

    def instruction_list(self):
        return [s for s in map(str.strip, self.instructions().split("\n")) if s]

    # -------------------------------------------------------------------------
    # Image
    # -------------------------------------------------------------------------
    def image(self):
        og = self.soup.find("meta", property="og:image")
        if og and og.get("content"):
            return og["content"]
        img = self.soup.find("img", class_="recipe-image")
        if img and img.get("src"):
            return img["src"]
        return None

    # -------------------------------------------------------------------------
    # Nutrients
    # -------------------------------------------------------------------------
    def nutrients(self):
        nutrients = {}
        table = self.soup.find("table", class_="js-recipe-nutritional-table")
        if not table:
            return None
        rows = table.find_all("tr")
        for r in rows:
            cells = r.find_all(["th", "td"])
            if len(cells) >= 2:
                name = self._clean_text(cells[0].get_text())
                value = self._clean_text(cells[1].get_text())
                if name and value:
                    nutrients[name] = value
        return nutrients if nutrients else None

    # -------------------------------------------------------------------------
    # Keywords
    # -------------------------------------------------------------------------
    def keywords(self):
        tags = []
        tag_section = self.soup.find("div", class_="recipe-tags-list")
        if tag_section:
            for a in tag_section.find_all("a", class_="recipe-tag"):
                text = self._clean_text(a.get_text())
                if text:
                    tags.append(text.capitalize())
        return tags

    # -------------------------------------------------------------------------
    # Ratings
    # -------------------------------------------------------------------------
    def ratings(self):
        rating_div = self.soup.find("div", class_="recipe-rating-info")
        if not rating_div:
            return None
        match = re.search(r"([\d.,]+)", rating_div.get_text())
        if match:
            return float(match.group(1).replace(",", "."))
        return None

    def ratings_count(self):
        rating_div = self.soup.find("div", class_="recipe-rating-info")
        if not rating_div:
            return None
        match = re.search(r"\((\d+)\)", rating_div.get_text())
        if match:
            return float(match.group(1))
        return None

    # -------------------------------------------------------------------------
    # Misc Optional
    # -------------------------------------------------------------------------
    def cuisine(self):
        text = self.description().lower()
        if "mediterrânica" in text:
            return "Mediterrânica"
        return None

    def dietary_restrictions(self):
        terms = self.soup.find_all("span", class_="recipe-special-diet-term")
        if not terms:
            return None
        restrictions = [self._clean_text(t.get_text()) for t in terms if t.get_text()]
        return restrictions or None

    def equipment(self):
        return None

    def cooking_method(self):
        text = self.instructions().lower()
        if "forno" in text:
            return "forno"
        if "frigideira" in text:
            return "frigideira"
        if "cozer" in text:
            return "cozer"
        return None
