from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class Hogarmania(AbstractScraper):
    @classmethod
    def host(cls):
        return "hogarmania.com"

    def site_name(self):
        return self.soup.find("meta", property="og:site_name")["content"]

    def _get_duration(self, field: str):
        v = self.schema.data.get(field)
        if v is None:
            return None
        # hogarmania uses {'@type': 'Duration', '@value': 'P0DT0H40M0S'} format
        if isinstance(v, dict):
            v = v.get("@value") or v.get("maxValue")
        if v:
            return get_minutes(v)
        return None

    def total_time(self):
        t = self._get_duration("totalTime")
        if t:
            return t
        prep = self._get_duration("prepTime") or 0
        cook = self._get_duration("cookTime") or 0
        return (prep + cook) or None

    def cook_time(self):
        return self._get_duration("cookTime")

    def prep_time(self):
        return self._get_duration("prepTime")

    def instructions(self):
        schema_instructions = self.schema.instructions()
        if schema_instructions:
            return schema_instructions
        # fallback for older pages without recipeInstructions in schema
        main = self.soup.find("main") or self.soup.find(id="content-body")
        if not main:
            return ""
        for h2 in main.find_all("h2"):
            if "elaboraci" in h2.get_text().lower():
                steps = []
                sib = h2.find_next_sibling()
                while sib and sib.name != "h2":
                    text = normalize_string(sib.get_text())
                    if text:
                        steps.append(text)
                    sib = sib.find_next_sibling()
                return "\n".join(steps)
        return ""
