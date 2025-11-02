import json
import re
import html
from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class Continente(AbstractScraper):
    @classmethod
    def host(cls):
        return "feed.continente.pt"

    def site_name(self):
        return "Continente"

    def language(self):
        return "pt-PT"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._data = self._extract_json_ld()

    # --- Helpers -------------------------------------------------------------

    def _extract_json_ld(self):
        script = self.soup.find("script", type="application/ld+json")
        if not script:
            return {}
        try:
            data = json.loads(script.string)
            if isinstance(data, list):
                data = next((item for item in data if item.get("@type") == "Recipe"), {})
            if data.get("@type") == "Recipe":
                return data
        except Exception:
            pass
        return {}

    # --- Core Fields ---------------------------------------------------------

    def author(self):
        return "Continente"

    def title(self):
        return self._data.get("name") or self.soup.find("h1").get_text(strip=True)

    def description(self):
        return normalize_string(
            self._data.get("description")
            or self.soup.find("meta", {"name": "description"}).get("content", "")
        )

    def image(self):
        image = self._data.get("image")
        if isinstance(image, list):
            return image[0]
        if isinstance(image, str):
            return image
        meta_img = self.soup.find("meta", property="og:image")
        return meta_img.get("content") if meta_img else None

    def category(self):
        breadcrumb = self.soup.find("nav", {"aria-label": "breadcrumb"})
        if breadcrumb:
            links = breadcrumb.find_all("a")
            if links:
                text = links[-1].get_text(strip=True)
                return html.unescape(text)
        tag_section = self.soup.find("div", class_=re.compile("tags|categoria", re.I))
        if tag_section:
            tag = tag_section.find("a")
            if tag:
                return html.unescape(tag.get_text(strip=True))
        return None

    def cuisine(self):
        cuisine = self._data.get("recipeCuisine")
        return cuisine or None

    def prep_time(self):
        return get_minutes(self._data.get("prepTime"))

    def cook_time(self):
        return self.prep_time()

    def total_time(self):
        return self.prep_time()

    def yields(self):
        return get_yields(self._data.get("recipeYield"))

    def ingredients(self):
        ingredients = self._data.get("recipeIngredient")
        if ingredients:
            return [normalize_string(i) for i in ingredients]
        # fallback
        container = self.soup.find("div", class_=re.compile("ingredientList", re.I))
        if container:
            return [li.get_text(strip=True) for li in container.find_all("li")]
        return []

    def instructions(self):
        instructions = self._data.get("recipeInstructions")
        if isinstance(instructions, list):
            return "\n".join(step.get("text") for step in instructions if step.get("text"))
        elif isinstance(instructions, str):
            return normalize_string(instructions)

        # fallback to HTML
        steps = []
        container = self.soup.find("div", {"data-control": "recipeSteps"})
        if container:
            for p in container.select("p"):
                text = p.get_text(" ", strip=True)
                if text:
                    steps.append(text)
        return "\n".join(steps)

    def instruction_list(self):
        instructions = self._data.get("recipeInstructions")
        if isinstance(instructions, list):
            return [step.get("text") for step in instructions if step.get("text")]
        return self.instructions().splitlines()

    def keywords(self):
        kw = self._data.get("keywords")
        if isinstance(kw, str):
            return [k.strip() for k in kw.split(",") if k.strip()]
        elif isinstance(kw, list):
            return kw
        return []

    def nutrients(self):
        agg = self._data.get("nutrition", {})
        if isinstance(agg, dict):
            return {k: v for k, v in agg.items() if v}
        table = self.soup.find("table", class_=re.compile("nutri", re.I))
        if table:
            result = {}
            for row in table.find_all("tr"):
                cols = [c.get_text(strip=True) for c in row.find_all(["th", "td"])]
                if len(cols) >= 2:
                    result[cols[0]] = cols[1]
            return result or None
        return None

    def ratings(self):
        agg = self._data.get("aggregateRating")
        if isinstance(agg, dict):
            value = agg.get("ratingValue")
            if value:
                return float(value.replace(",", "."))
        return None

    def ratings_count(self):
        agg = self._data.get("aggregateRating")
        if isinstance(agg, dict):
            return int(float(agg.get("ratingCount", 0)))
        return None

    def equipment(self):
        video = self._data.get("video", {})
        if isinstance(video, dict) and "description" in video:
            if any(word in video["description"].lower() for word in ["tacho", "forno", "taça"]):
                return ["tacho", "forno", "taça"]
        return None

    def dietary_restrictions(self):
        # None explicitly on site, could infer keywords like “vegan” later
        return None

    def cooking_method(self):
        instr = self.instructions().lower()
        if "forno" in instr:
            return "forno"
        if "fritar" in instr:
            return "fritar"
        if "grelhar" in instr:
            return "grelhar"
        return None
