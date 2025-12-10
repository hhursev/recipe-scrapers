from ._abstract import AbstractScraper
from ._utils import normalize_string, get_minutes, get_yields
import re

class FlavorsByLinbie(AbstractScraper):
    @classmethod
    def host(cls):
        return "flavorsbylinbie.com"

    def author(self):
        # Try schema first (in case there's a Recipe schema)
        author_from_schema = self.schema.author()
        if author_from_schema:
            return author_from_schema

        # Try extracting from author link in HTML
        author_link = self.soup.select_one('a[href*="/author/"]')
        if author_link:
            author_text = author_link.get_text(strip=True)
            if author_text:
                return normalize_string(author_text)

        # Fallback to site name
        return "Flavors By Linbie"

    def title(self):
        title_tag = self.soup.find("title")
        if title_tag:
            return normalize_string(title_tag.get_text(" ", strip=True))

        # Fallback to main H1 heading
        h1 = self.soup.find("h1")
        if h1:
            return normalize_string(h1.get_text(" ", strip=True))

        return ""

    def category(self):
        category_from_schema = self.schema.category()
        if category_from_schema:
            return category_from_schema

        meta = self.soup.select_one('meta[property="article:section"]')
        if meta and meta.get("content"):
            return normalize_string(meta.get("content"))

    def total_time(self):
        headings = self.soup.find_all(["h2"])
        for h in headings:
            text = h.get_text(" ", strip=True)
            normalized = text.lower().strip()

            if normalized == "total time":
                sib = h.find_next_sibling()
                while sib and getattr(sib, "name", None) != "p":
                    sib = sib.find_next_sibling()
                if sib and sib.name == "p":
                    try:
                        value = sib.get_text(" ", strip=True)
                        minutes = get_minutes(value)
                        if minutes:
                            return minutes
                    except Exception:
                        pass

        paragraph = self._get_servings_time_paragraph()
        if not paragraph:
            return None

        total = self._extract_time_from_paragraph(paragraph, "total time:")
        if total:
            return total

        prep = self._extract_time_from_paragraph(paragraph, "prep time:")
        cook = self._extract_time_from_paragraph(paragraph, "cook time:")

        if prep and cook:
            return prep + cook
        return prep or cook

    def _extract_time_from_servings_section(self, time_type):
        paragraph = self._get_servings_time_paragraph()
        if not paragraph:
            return None
        label = f"{time_type} time:"
        return self._extract_time_from_paragraph(paragraph, label)

    def prep_time(self):
        return self._extract_time_from_servings_section("prep")

    def cook_time(self):
        return self._extract_time_from_servings_section("cook")

    def yields(self):
        paragraph = self._get_servings_time_paragraph()
        if paragraph:
            value = self._slice_field(paragraph, "serves:")
            if value:
                try:
                    return get_yields(value)
                except Exception:
                    pass

        headings = self.soup.find_all(["h2"])
        for h in headings:
            text = h.get_text(" ", strip=True)
            normalized = text.lower().strip()

            if normalized in ["makes", "servings", "serves"]:
                sib = h.find_next_sibling()
                while sib and getattr(sib, "name", None) != "p":
                    sib = sib.find_next_sibling()
                if sib and sib.name == "p":
                    try:
                        value = sib.get_text(" ", strip=True)
                        if value:
                            return get_yields(value)
                    except Exception:
                        pass

        return None

    def _get_servings_time_paragraph(self) -> str:
        headings = self.soup.find_all(["h2"])
        for h in headings:
            text = h.get_text(" ", strip=True).lower()
            if "servings" in text and "time" in text:
                sib = h.find_next_sibling()
                while sib and getattr(sib, "name", None) != "p":
                    sib = sib.find_next_sibling()
                if sib and sib.name == "p":
                    return sib.get_text(" ", strip=True)

        for p in self.soup.find_all("p"):
            text = p.get_text(" ", strip=True)
            lower = text.lower()
            if "serves:" in lower and "total time" in lower:
                return text

        return ""

    def _slice_field(self, paragraph: str, label: str) -> str:
        lower = paragraph.lower()
        if label not in lower:
            return ""
        value = lower.split(label, 1)[1]
        for delimiter in [
            "prep time:",
            "cook time:",
            "total time:",
            "serves:",
            "\n",
            "<",
            "<br",
        ]:
            if delimiter in value:
                value = value.split(delimiter, 1)[0]
                break
        return value.strip()

    def _normalize_time_phrase(self, text: str) -> str:
        value = text
        if " or " in value:
            value = value.split(" or ", 1)[0].strip()
        elif ", or " in value:
            value = value.split(", or ", 1)[0].strip()

        value = value.replace("–", "-")
        if "-" in value:
            parts = value.split("-", 1)
            if len(parts) == 2:
                value = parts[1].strip()

        lower = value.lower()
        for phrase in [" on low", " on high", " on medium"]:
            if phrase in lower:
                idx = lower.index(phrase)
                value = value[:idx].strip()
                break

        return value

    def _extract_time_from_paragraph(self, paragraph: str, label: str) -> int | None:
        field = self._slice_field(paragraph, label)
        if not field:
            return None
        cleaned = self._normalize_time_phrase(field)
        try:
            return get_minutes(cleaned)
        except Exception:
            return None

    def image(self):
        return self.schema.image()

    def ingredients(self):
        headings = self.soup.find_all(["h2"])
        for h in headings:
            text = h.get_text(" ", strip=True)
            normalized = text.replace("’", "'").replace("‘", "'")
            # check for "What You'll Need" heading
            if "what you'll need" in normalized.lower():
                items = []
                sib = h.find_next_sibling()
                while sib:
                    name = getattr(sib, "name", None)
                    if name == "h2":
                        break
                    if name == "ul":
                        for li in sib.find_all("li"):
                            li_text = li.get_text(" ", strip=True)
                            items.append(normalize_string(li_text))
                    sib = sib.find_next_sibling()
                return items

    def instructions(self):
        # isolate the main content area
        entry = self.soup.find(class_="entry-content") or self.soup.find(
            itemprop="text"
        )
        if not entry:
            return ""

        # locate the H2 that labels the instructions section
        instr_heading = None
        for h in entry.find_all(["h2"]):
            text = h.get_text(" ", strip=True).lower()
            if "instructions" in text or "how to make" in text:
                instr_heading = h
                break

        if not instr_heading:
            return ""

        # collect paragraph texts until next H2
        instructions = []
        sib = instr_heading.find_next_sibling()
        while sib:
            name = getattr(sib, "name", None)
            if name == "h2":
                break
            # add paragraph text to instructions list
            if name == "p":
                text = normalize_string(sib.get_text(" ", strip=True))
                if text:
                    instructions.append(text)
            sib = sib.find_next_sibling()

        return "\n".join(instructions)

    def description(self):
        entry = self.soup.find(class_="entry-content") or self.soup.find(
            itemprop="text"
        )
        if not entry:
            return ""

        for p in entry.find_all("p"):
            text = normalize_string(p.get_text(" ", strip=True))
            if not text:
                continue
            if text.lower().startswith("serves:"):
                continue
            # Remove spaces before punctuation (caused by get_text separator)
            text = re.sub(r"\s+([.!?,;:])", r"\1", text)
            return text

        return ""
