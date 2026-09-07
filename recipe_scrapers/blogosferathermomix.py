from ._abstract import AbstractScraper
from ._utils import normalize_string


class BlogosferaThermomix(AbstractScraper):
    @classmethod
    def host(cls, domain="blogosferathermomix.es"):
        return domain

    def canonical_url(self):
        # Next.js SSR may deliver attributes with escaped quotes (\"value\");
        # strip them from extracted values as a precaution.
        for link in self.soup.find_all("link"):
            rel = link.get("rel") or []
            rel_str = rel if isinstance(rel, str) else " ".join(rel)
            if "canonical" in rel_str:
                return link.get("href", "").strip('\\"')
        raise NotImplementedError

    def author(self):
        for nav in self.soup.find_all("nav"):
            if "breadcrumb" in (nav.get("aria-label") or ""):
                items = nav.find_all("a")
                if len(items) >= 3:
                    return items[2].get_text().strip().title()
        raise NotImplementedError

    def site_name(self):
        for meta in self.soup.find_all("meta"):
            if "og:site_name" in (meta.get("property") or ""):
                return meta.get("content", "").strip('\\"')
        raise NotImplementedError

    def title(self):
        return normalize_string(self.soup.find("h1").get_text())

    def image(self):
        for img in self.soup.select("main p a img, main p img"):
            src = (img.get("src") or img.get("data-src") or "").strip('\\"')
            if src and "recipeImgFallback" not in src:
                return src
        raise NotImplementedError

    def _find_section_header(self, keyword):
        """Return the <p> whose stripped text matches keyword (ignoring trailing .:)."""
        for p in self.soup.find_all("p"):
            text = p.get_text().strip().rstrip(".:").strip()
            if text == keyword:
                return p
        return None

    def ingredients(self):
        # Format 1: <p><strong>Ingredientes</strong></p> + <ul>
        for strong in self.soup.find_all("strong"):
            if strong.get_text().strip() == "Ingredientes":
                ul = strong.parent.find_next_sibling("ul")
                if ul:
                    return [normalize_string(li.get_text()) for li in ul.find_all("li")]

        # Formats 2 & 3: <p> header (may use <b><u> or plain text) + following content
        header = self._find_section_header("Ingredientes")
        if header:
            result = []
            sib = header.find_next_sibling()
            while sib:
                if sib.name == "p":
                    sib_kw = sib.get_text().strip().rstrip(".:").strip()
                    # Stop at Preparación / Elaboración section
                    if sib_kw in ("Preparación", "Elaboración"):
                        break
                    if any(
                        kw in (el.get_text() or "")
                        for el in sib.find_all(["b", "strong", "u"])
                        for kw in ("Preparación", "Elaboración")
                    ):
                        break
                    # Skip image-only paragraphs
                    if sib.find("img") and not sib.get_text().strip():
                        sib = sib.find_next_sibling()
                        continue
                    # Split <br>-separated items
                    for br in sib.find_all("br"):
                        br.replace_with("\n")
                    lines = [
                        normalize_string(line)
                        for line in sib.get_text().splitlines()
                        if normalize_string(line)
                    ]
                    result.extend(lines)
                elif sib.name == "ul":
                    result.extend(
                        normalize_string(li.get_text()) for li in sib.find_all("li")
                    )
                sib = sib.find_next_sibling()
            if result:
                return result

        raise NotImplementedError

    def instructions(self):
        # Format 1: <p><strong>Preparación</strong></p> + <ol>
        for strong in self.soup.find_all("strong"):
            if strong.get_text().strip() == "Preparación":
                ol = strong.parent.find_next_sibling("ol")
                if ol:
                    steps = []
                    for li in ol.find_all("li"):
                        for br in li.find_all("br"):
                            br.replace_with(" ")
                        steps.append(normalize_string(li.get_text()))
                    return "\n".join(steps)

        # Formats 2 & 3: <p> header + following paragraphs
        header = self._find_section_header("Preparación")
        if not header:
            header = self._find_section_header("Elaboración")
        if header:
            result = []
            sib = header.find_next_sibling()
            while sib:
                if sib.name == "p":
                    # Skip pure image paragraphs
                    if sib.find("img") and not sib.get_text().strip():
                        sib = sib.find_next_sibling()
                        continue
                    for br in sib.find_all("br"):
                        br.replace_with("\n")
                    lines = [
                        normalize_string(line)
                        for line in sib.get_text().splitlines()
                        if normalize_string(line)
                    ]
                    result.extend(lines)
                elif sib.name == "ol":
                    for li in sib.find_all("li"):
                        for br in li.find_all("br"):
                            br.replace_with(" ")
                        result.append(normalize_string(li.get_text()))
                sib = sib.find_next_sibling()
            if result:
                return "\n".join(result)

        raise NotImplementedError

    def yields(self):
        for p in self.soup.find_all("p"):
            if "Ración para" in p.get_text():
                sibling = p.find_next_sibling("p")
                if sibling:
                    return normalize_string(sibling.get_text())
        raise NotImplementedError

    def language(self):
        return "es"
