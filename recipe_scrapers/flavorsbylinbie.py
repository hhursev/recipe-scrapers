from ._abstract import AbstractScraper
from ._utils import normalize_string


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
        
        meta = self.soup.select_one('meta[property="article:section]')
        if meta and meta.get("content"):
            return normalize_string(meta.get("content"))

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        headings = self.soup.find_all(['h2'])
        for h in headings:
            text = h.get_text(" ", strip=True)
            normalized = text.replace("’", "'").replace("‘", "'")
            # check for "What You'll Need" heading
            if "what you'll need" in normalized.lower():
                # find the next sibling UL (skip intervening strings/comments)
                sib = h.find_next_sibling()
                while sib and getattr(sib, 'name', None) != 'ul':
                    sib = sib.find_next_sibling()
                if sib and sib.name == 'ul':
                    # add all ingredients to items list
                    items = []
                    for li in sib.find_all('li'):
                        text = li.get_text(" ", strip=True)
                        if text:
                            items.append(normalize_string(text))
                    return items

    def instructions(self):
        # isolate the main content area
        entry = self.soup.find(class_='entry-content') or self.soup.find(itemprop='text')
        
        # locate the H2 that labels the instructions section
        instr_heading = None
        for h in entry.find_all(['h2']):
            if 'instructions' in h.get_text(' ', strip=True).lower():
                instr_heading = h
                break

        # collect paragraph texts until next H2
        instructions = []
        sib = instr_heading.find_next_sibling()
        while sib:
            name = getattr(sib, 'name', None)
            # stop if we hit another top-level H2 block
            if name == 'h2':
                break
            # add paragraph text to instructions list
            if name == 'p':
                text = normalize_string(sib.get_text(' ', strip=True))
                if text:
                    instructions.append(text)
            sib = sib.find_next_sibling()

            return '\n'.join(instructions)



    def description(self):
        # isolate the main content area
        entry = self.soup.find(class_='entry-content') or self.soup.find(itemprop='text')

        # get the first paragraph tag in the entry
        first_p = entry.find('p')
        return normalize_string(first_p.get_text(" ", strip=True))
