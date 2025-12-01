from ._abstract import AbstractScraper
from ._utils import normalize_string


class FlavorsByLinbie(AbstractScraper):
    @classmethod
    def host(cls):
        return "flavorsbylinbie.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

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
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        # isolate the main content area
        entry = self.soup.find(class_='entry-content') or self.soup.find(itemprop='text')

        # get the first paragraph tag in the entry
        first_p = entry.find('p')
        return normalize_string(first_p.get_text(" ", strip=True))
