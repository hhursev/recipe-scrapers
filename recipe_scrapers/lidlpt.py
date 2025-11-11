import re
import html
from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields


class LidlPT(AbstractScraper):
    @classmethod
    def host(cls):
        return "receitaslidl.pt"

    def site_name(self):
        return "Lidl Portugal"

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
    # Core Fields
    # -------------------------------------------------------------------------
    def author(self):
        if hasattr(self, "schema"):
            try:
                author = self.schema.author()
                if author:
                    return self._clean_text(author)
            except Exception:
                pass
        return "Lidl Portugal"

    def title(self):
        title_tag = self.soup.find("h1", {"title": True})
        if title_tag:
            return self._clean_text(title_tag.get_text())
        return None

    def description(self):
        meta = self.soup.find("meta", {"name": "description"})
        if meta and meta.get("content"):
            return self._clean_text(meta["content"])

        title = self.title() or "Receita"
        category = self.category() or "prato"
        servings = self.yields() or ""
        return f"{title} — uma deliciosa receita de {category.lower()} para {servings}."

    def category(self):
        # Schema fallback
        if hasattr(self, "schema") and getattr(self.schema, "data", None):
            try:
                cat = self.schema.category()
                if cat:
                    return self._clean_text(cat)
            except Exception:
                pass

        # Breadcrumb-based fallback
        breadcrumb = self.soup.find("div", {"data-testid": "breadcrumb"})
        if breadcrumb:
            links = breadcrumb.find_all("a", href=True)
            for a in reversed(links):
                text = a.get_text(strip=True)
                if text and "receita" not in text.lower():
                    return self._clean_text(text)

        # Tag fallback
        section = self.soup.find("h2", string=re.compile("Palavras.?chave", re.I))
        if section:
            container = section.find_next("div")
            if container:
                tags = [self._clean_text(tag.get_text()) for tag in container.find_all("span")]
                if tags:
                    return tags[0]

        return None

    # -------------------------------------------------------------------------
    # Time and Yield
    # -------------------------------------------------------------------------
    def prep_time(self):
        tag = self.soup.find("div", {"data-testid": "recipe-info-badge-preparation"})
        if not tag:
            return 0
        time_text = tag.find_all("span")[-1].get_text(strip=True)
        return get_minutes(time_text)

    def cook_time(self):
        tag = self.soup.find("div", {"data-testid": "recipe-info-badge-cooking"})
        if not tag:
            return 0
        time_text = tag.find_all("span")[-1].get_text(strip=True)
        return get_minutes(time_text)

    def total_time(self):
        return (self.prep_time() or 0) + (self.cook_time() or 0)

    def yields(self):
        input_tag = self.soup.find("input", {"data-testid": "servings-group-input"})
        if input_tag and input_tag.get("value"):
            servings = input_tag.get("value").strip()
            return get_yields(servings)
        return None

    # -------------------------------------------------------------------------
    # Ingredients
    # -------------------------------------------------------------------------
    def ingredients(self):
        ingredients = []

        items = self.soup.find_all("li", {"data-name": True})
        for li in items:
            quantity = li.find("span", {"data-testid": "quantity-from"})
            unit = li.find("span", {"data-testid": "unit"})
            name = li.find("div", {"data-testid": "ingredient"})
            parts = [
                self._clean_text(quantity.get_text()) if quantity else "",
                self._clean_text(unit.get_text()) if unit else "",
                self._clean_text(name.get_text()) if name else self._clean_text(li.get("data-name", "")),
            ]
            text = " ".join([p for p in parts if p])
            if text:
                ingredients.append(text)

        # fallback if no data-name attributes
        if not ingredients:
            ul = self.soup.find("ul", {"data-testid": "ingredient-list"})
            if ul:
                for li in ul.find_all("li"):
                    text = self._clean_text(li.get_text(" ", strip=True))
                    if text:
                        ingredients.append(text)

        return ingredients

    # -------------------------------------------------------------------------
    # Instructions
    # -------------------------------------------------------------------------
    def instructions(self):
        ol = self.soup.find("ol", attrs={"data-rid": re.compile(r"^cooking-step$", re.I)})

        # Fallback: look for “Passo a Passo” section
        if not ol:
            for art in self.soup.find_all("article"):
                heading = art.find(["h2", "h3"])
                if heading and "passo a passo" in heading.get_text(strip=True).lower():
                    cand = art.find("ol")
                    if cand:
                        ol = cand
                        break

        if not ol:
            return ""

        steps = []
        for li in ol.find_all("li"):
            # Remove bullet markers or numbering spans
            for sp in li.find_all("span"):
                if sp.get("class") and any("marker" in c for c in sp.get("class")):
                    sp.decompose()

            text = li.get_text(" ", strip=True)
            if text:
                text = re.sub(r"\s*\n\s*", " ", text)
                steps.append(self._clean_text(text))

        return "\n".join(steps)

    def instruction_list(self):
        return [s for s in map(str.strip, self.instructions().split("\n")) if s]

    # -------------------------------------------------------------------------
    # Image
    # -------------------------------------------------------------------------
    def image(self):
        picture = self.soup.find("picture", {"data-testid": "recipe-detail-image"})
        if not picture:
            return None

        sources = picture.find_all("source")
        if sources:
            srcset_urls = []
            for s in sources:
                srcset = s.get("srcset")
                if srcset:
                    urls = [u.strip().split(" ")[0] for u in srcset.split(",")]
                    srcset_urls.extend(urls)
            if srcset_urls:
                srcset_urls.sort(
                    key=lambda x: int(re.search(r"_(\d+)x", x).group(1)) if re.search(r"_(\d+)x", x) else 0,
                    reverse=True,
                )
                return srcset_urls[0]

        img = picture.find("img")
        if img and img.get("src"):
            return img.get("src")

        meta_img = self.soup.find("meta", property="og:image")
        if meta_img:
            return meta_img.get("content")

        return None

    # -------------------------------------------------------------------------
    # Nutrients
    # -------------------------------------------------------------------------
    def nutrients(self):
        nutrients = {}
        section = self.soup.find("h2", string=re.compile("Informação Nutricional", re.I))
        if not section:
            return None

        container = section.find_next("div", class_=re.compile("flex flex-wrap"))
        if not container:
            return None

        for block in container.find_all("div", class_=re.compile("flex flex-col")):
            labels = block.find_all("span")
            if len(labels) >= 2:
                name = self._clean_text(labels[0].get_text())
                value = self._clean_text(labels[1].get_text())
                if name and value:
                    nutrients[name] = value

        return nutrients if nutrients else None

    # -------------------------------------------------------------------------
    # Keywords
    # -------------------------------------------------------------------------
    def keywords(self):
        keywords = []
        tag_section = self.soup.find("nav", {"data-rid": "tag-box"})
        if not tag_section:
            return keywords

        for p in tag_section.select("p.font-small_1-base-mobile"):
            text = self._clean_text(p.get_text())
            if text:
                keywords.append(text.capitalize())

        return keywords

    # -------------------------------------------------------------------------
    # Optional / Extended Fields
    # -------------------------------------------------------------------------
    def cuisine(self):
        return None

    def ratings(self):
        stars = self.soup.find("div", {"data-testid": "rating-stars"})
        if not stars:
            return None
        label = stars.get("aria-label", "")
        match = re.search(r"([\d.,]+)\s+de\s+5", label)
        if match:
            try:
                return float(match.group(1).replace(",", "."))
            except ValueError:
                return None
        return None

    def ratings_count(self):
        count = self.soup.find("span", {"data-testid": "rating-count"})
        if count:
            digits = re.search(r"(\d+)", count.get_text())
            if digits:
                return int(digits.group(1))
        return None

    def equipment(self):
        return None

    def cooking_method(self):
        text = self.instructions().lower()
        if "forno" in text:
            return "forno"
        if "frigideira" in text:
            return "frigideira"
        if "grelhar" in text:
            return "grelhar"
        return None

    def dietary_restrictions(self):
        # Could infer later from keywords (e.g. vegan, vegetariano)
        return None
