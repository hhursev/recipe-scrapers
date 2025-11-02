import re
import html
from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class ClaraDeSousa(AbstractScraper):
    @classmethod
    def host(cls):
        return "claradesousa.pt"

    def site_name(self):
        return "Clara de Sousa"

    def language(self):
        return "pt-PT"

    def author(self):
        return "Clara de Sousa"

    # -------------------------------------------------------------------------
    # CORE FIELDS
    # -------------------------------------------------------------------------
    def title(self):
        h1 = self.soup.find("h1", class_="elementor-heading-title")
        if h1:
            return html.unescape(h1.get_text(strip=True))
        meta = self.soup.find("meta", property="og:title")
        if meta and meta.get("content"):
            return html.unescape(meta["content"])
        return None

    def description(self):
        meta = self.soup.find("meta", {"name": "description"})
        if meta and meta.get("content"):
            return html.unescape(meta["content"])
        first_p = self.soup.find("p")
        if first_p:
            return html.unescape(first_p.get_text(strip=True))
        return None

    def image(self):
        meta_img = self.soup.find("meta", property="og:image")
        if meta_img and meta_img.get("content"):
            return meta_img["content"]
        img = self.soup.find("img")
        if img and img.get("src"):
            return img["src"]
        return None

    def canonical_url(self):
        link = self.soup.find("link", rel="canonical")
        return link["href"] if link else self.url

    # -------------------------------------------------------------------------
    # TIME AND YIELD
    # -------------------------------------------------------------------------
    def prep_time(self):
        section = self.soup.find("section", class_=re.compile(r"recipe-details", re.I))
        if not section:
            return 0
    
        # Look for the specific widget that contains the label
        div = section.find(lambda t: t.name == "div" and "tempo de preparação" in t.get_text(strip=True).lower())
        if not div:
            return 0
    
        text = div.get_text(" ", strip=True)
        # First minutes mentioned are the actual prep time
        m = re.search(r"(\d+)\s*(?:minutos?|mins?)", text, re.I)
        return int(m.group(1)) if m else 0
    
    
    def cook_time(self):
        section = self.soup.find("section", class_=re.compile(r"recipe-details", re.I))
        if not section:
            return 0
    
        div = section.find(lambda t: t.name == "div" and "tempo de preparação" in t.get_text(strip=True).lower())
        if not div:
            return 0
    
        text = div.get_text(" ", strip=True)
    
        # Prefer refrigeration HOURS after the '+'
        m_hours = re.search(r"\+\s*(\d+)\s*horas?\b", text, re.I)
        if m_hours:
            return int(m_hours.group(1)) * 60
    
        # If refrigeration time is in minutes after '+'
        m_mins = re.search(r"\+\s*(\d+)\s*(?:minutos?|mins?)\b", text, re.I)
        if m_mins:
            return int(m_mins.group(1))
    
        # Fallback: any "X horas ... refrigeração"
        m_any_hours = re.search(r"(\d+)\s*horas?.*refrigera", text, re.I)
        if m_any_hours:
            return int(m_any_hours.group(1)) * 60
    
        # Fallback: any "X minutos ... refrigeração"
        m_any_mins = re.search(r"(\d+)\s*(?:minutos?|mins?).*refrigera", text, re.I)
        if m_any_mins:
            return int(m_any_mins.group(1))
    
        return 0
    
    
    def total_time(self):
        return (self.prep_time() or 0) + (self.cook_time() or 0)
    
    
    def yields(self):
        section = self.soup.find("section", class_=re.compile(r"recipe-details", re.I))
        if not section:
            return None
    
        # Target the element that actually contains the 'doses:' label
        # and only read its own text (avoids grabbing the '15' from prep time)
        div = section.find(lambda t: t.name == "div" and "doses" in t.get_text(strip=True).lower())
        if not div:
            return None
    
        local_text = " ".join(div.stripped_strings)  # stay local to this widget
        # e.g., "doses: 6"
        m = re.search(r"doses\s*:\s*(\d+)", local_text, re.I)
        if m:
            return f"{m.group(1)} doses"
    
        # fallback: last integer in this local text
        m2 = re.findall(r"(\d+)", local_text)
        if m2:
            return f"{m2[-1]} doses"
    
        return None


    # -------------------------------------------------------------------------
    # CATEGORY AND KEYWORDS
    # -------------------------------------------------------------------------
    def category(self):
        body = self.soup.find("body")
        if not body:
            return None
        classes = body.get("class", [])
        cats = [html.unescape(c.replace("category-", "").replace("-", " ").title())
                for c in classes if c.startswith("category-")]
        return cats or None

    def keywords(self):
        body = self.soup.find("body")
        if not body:
            return []
        classes = body.get("class", [])
        tags = [html.unescape(c.replace("tag-", "").replace("-", " ").title())
                for c in classes if c.startswith("tag-")]
        return tags

    # -------------------------------------------------------------------------
    # INGREDIENTS AND INSTRUCTIONS
    # -------------------------------------------------------------------------    
    def ingredients(self):
        ingredients = []
    
        # locate heading that contains "Ingredientes"
        heading = self.soup.find(lambda tag: tag.name in ["h2", "h3"] and "ingredientes:" in tag.get_text(strip=True).lower())
        if not heading:
            return ingredients
    
        # search downward from that heading until we hit a <ul> in the same column
        ul = heading.find_next(lambda tag: tag.name == "ul" and tag.find_parent("div", class_=re.compile("elementor-element")))
        if not ul:
            return ingredients
    
        for li in ul.find_all("li"):
            text = li.get_text(" ", strip=True)
            if text:
                ingredients.append(html.unescape(text))
    
        return ingredients

    def instructions(self):
        steps = []
    
        # Find header “Confecção” or “Preparação”
        header = self.soup.find(lambda t: t.name in ["h2", "h3"] and re.search(r"conf[eçc][aã]o|prepar", t.get_text(strip=True), re.I))
        if not header:
            return ""
    
        # Search anywhere after the heading for the <ol> list
        ol = header.find_next("ol")
        if not ol:
            return ""
    
        for li in ol.find_all("li"):
            text = li.get_text(" ", strip=True)
            if text:
                steps.append(html.unescape(text))
        return "\n".join(steps)

    def instruction_list(self):
        text = self.instructions()
        if not text:
            return []
        return [s.strip() for s in text.split("\n") if s.strip()]

    # -------------------------------------------------------------------------
    # OPTIONAL FIELDS
    # -------------------------------------------------------------------------
    def nutrients(self):
        # None present on site
        return None

    def ratings(self):
        # Clara's site doesn't include ratings
        return None

    def ratings_count(self):
        return None

    def equipment(self):
        equipment = []
    
        # Find the heading "UTENSÍLIOS"
        header = self.soup.find(lambda tag: tag.name in ["h2", "h3"] and "utens" in tag.get_text(strip=True).lower())
        if not header:
            return None
    
        # The next Elementor text block contains the list
        next_div = header.find_next("div", class_=re.compile("elementor-widget-text-editor"))
        if not next_div:
            return None
    
        for li in next_div.find_all("li"):
            text = li.get_text(" ", strip=True)
            if text:
                equipment.append(html.unescape(text))
    
        return equipment or None

    def cooking_method(self):
        instr = self.instructions().lower()
        if "forno" in instr:
            return "forno"
        if "fritar" in instr:
            return "fritar"
        if "grelhar" in instr:
            return "grelhar"
        return None

    def dietary_restrictions(self):
        tags = self.keywords()
        restrictions = [t for t in tags if "Sem" in t or "Vegetariano" in t]
        return restrictions or None

    def cuisine(self):
        # Not specified in Clara’s recipes
        return None
