from ._abstract import AbstractScraper

class TwentyFourKitchenPT(AbstractScraper):
    @classmethod
    def host(cls):
        return "24kitchen.pt"

    # -----------------------------
    # BASIC META DATA
    # -----------------------------
    def author(self):
        try:
            return self.schema.author()
        except Exception:
            # fallback: meta tag author or fixed
            meta = self.soup.find("meta", attrs={"name": "author"})
            return meta["content"].strip() if meta and meta.get("content") else None

    def title(self):
        try:
            return self.schema.title()
        except Exception:
            tag = self.soup.find("title")
            return tag.get_text(strip=True).split(" - ")[0] if tag else None

    def category(self):
        try:
            return self.schema.category()
        except Exception:
            # fallback: look for “Sobremesas”, etc.
            breadcrumb = self.soup.select_one("nav.breadcrumb a:last-child")
            return breadcrumb.get_text(strip=True) if breadcrumb else None

    def total_time(self):
        try:
            return self.schema.total_time()
        except Exception:
            return None

    def prep_time(self):
        try:
            return self.schema.prep_time()
        except Exception:
            return None

    def cook_time(self):
        try:
            return self.schema.cook_time()
        except Exception:
            return None

    def yields(self):
        try:
            return self.schema.yields()
        except Exception:
            return None

    def image(self):
        try:
            return self.schema.image()
        except Exception:
            img = self.soup.find("meta", property="og:image")
            return img["content"] if img else None

    def description(self):
        try:
            return self.schema.description()
        except Exception:
            meta = self.soup.find("meta", attrs={"name": "description"})
            return meta["content"].strip() if meta and meta.get("content") else None

    # -----------------------------
    # CONTENT DATA
    # -----------------------------
    def ingredients(self):
        try:
            return self.schema.ingredients()
        except Exception:
            ingredients = [
                el.get_text(strip=True)
                for el in self.soup.select("div.field--name-field-ingredients li")
            ]
            return ingredients or None

    def instructions(self):
        try:
            return self.schema.instructions()
        except Exception:
            # fallback: text version
            steps = [
                el.get_text(strip=True)
                for el in self.soup.select("div.field--name-field-preparation li, div.field--name-field-preparation p")
            ]
            return "\n".join(steps) if steps else None

    def instruction_list(self):
        try:
            return self.schema.instructions()
        except Exception:
            result = []
            for el in self.soup.select("div.field--name-field-preparation *"):
                if el.name in ["h2", "h3"]:
                    section = el.get_text(strip=True)
                    if section:
                        result.append(section)
                elif el.name in ["p", "li"]:
                    text = el.get_text(strip=True)
                    if text:
                        result.append(text)
            return result or []

    def ratings(self):
        try:
            return self.schema.ratings()
        except Exception:
            return None

    def ratings_count(self):
        try:
            return self.schema.ratings_count()
        except Exception:
            return None

    def cuisine(self):
        try:
            return self.schema.cuisine()
        except Exception:
            return None

    # -----------------------------
    # EXTRA OPTIONAL FIELDS
    # -----------------------------
    def keywords(self):
        # Extract tags displayed below recipe title
        tags = [
            a.get_text(strip=True)
            for a in self.soup.select("ul.subtags__list li.subtags__item a.subtags__link")
        ]
        return tags or None

    def equipment(self):
        return None

    def cooking_method(self):
        return None

    def dietary_restrictions(self):
        return None

    def nutrients(self):
        return {}
