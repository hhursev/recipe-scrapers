from ._abstract import AbstractScraper
from ._utils import normalize_string, get_minutes, get_yields


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
        headings = self.soup.find_all(['h2'])
        for h in headings:
            text = h.get_text(" ", strip=True)
            normalized = text.replace("'", "'").replace("'", "'")
            
            # First, check for standalone "Total Time" heading
            if normalized.lower().strip() == "total time":
                sib = h.find_next_sibling()
                while sib and getattr(sib, 'name', None) != 'p':
                    sib = sib.find_next_sibling()
                if sib and sib.name == 'p':
                    try:
                        time_text = sib.get_text(" ", strip=True)
                        total_time = get_minutes(time_text)
                        if total_time:
                            return total_time
                    except Exception:
                        pass
            
            # check for "Servings & Time" heading
            if "servings" in normalized.lower() and "time" in normalized.lower():
                # find the next sibling paragraph
                sib = h.find_next_sibling()
                while sib and getattr(sib, 'name', None) != 'p':
                    sib = sib.find_next_sibling()
                if sib and sib.name == 'p':
                    # parse prep time, cook time, and total time from the paragraph
                    p_text = sib.get_text(" ", strip=True)
                    prep_time = None
                    cook_time = None
                    total_time = None
                    
                    # Check for "Total Time:" field directly
                    if "total time:" in p_text.lower():
                        try:
                            total_match = p_text.lower().split("total time:")[1].strip()
                            for delimiter in ["prep time:", "cook time:", "\n", "<"]:
                                if delimiter in total_match:
                                    total_match = total_match.split(delimiter)[0].strip()
                                    break
                            total_time = get_minutes(total_match)
                            if total_time:
                                return total_time
                        except Exception:
                            pass
                    
                    # Look for "Prep time:" pattern
                    if "prep time:" in p_text.lower():
                        try:
                            prep_match = p_text.lower().split("prep time:")[1]
                            for delimiter in ["cook time:", "total time:", "\n", "<"]:
                                if delimiter in prep_match:
                                    prep_match = prep_match.split(delimiter)[0].strip()
                                    break
                            else:
                                prep_match = prep_match.strip()
                            prep_time = get_minutes(prep_match)
                        except Exception:
                            pass
                    
                    # Look for "Cook time:" pattern
                    if "cook time:" in p_text.lower():
                        try:
                            cook_match = p_text.lower().split("cook time:")[1]
                            for delimiter in ["prep time:", "total time:", "\n", "<"]:
                                if delimiter in cook_match:
                                    cook_match = cook_match.split(delimiter)[0].strip()
                                    break
                            else:
                                cook_match = cook_match.strip()
                            
                            # Handle "8 hours on low or 4 hours on high" or "6–8 hours on low, or 3–4 hours on high" edge cases
                            # Split by "or" or "," and take the first option
                            if " or " in cook_match:
                                cook_match = cook_match.split(" or ")[0].strip()
                            elif ", or " in cook_match:
                                cook_match = cook_match.split(", or ")[0].strip()
                            
                            # Handle ranges like "6–8 hours" (en dash or hyphen) - take the higher value
                            if "–" in cook_match or "-" in cook_match:
                                # Replace dash with hyphen for consistency then split by hyphen and take the second (higher) value
                                cook_match = cook_match.replace("–", "-")
                                parts = cook_match.split("-", 1)
                                if len(parts) == 2:
                                    cook_match = parts[1].strip()
                            
                            # Clean up any extra text like "on low" or "on high" before parsing
                            # get_minutes should handle this, but we can help by removing common phrases
                            for phrase in [" on low", " on high", " on medium"]:
                                if phrase in cook_match.lower():
                                    cook_match = cook_match.lower().split(phrase)[0].strip()
                                    break
                            
                            cook_time = get_minutes(cook_match)
                        except Exception:
                            pass
                    
                    # Return sum if both prep and cook found, otherwise return what we have
                    if prep_time and cook_time:
                        return prep_time + cook_time
                    elif prep_time:
                        return prep_time
                    elif cook_time:
                        return cook_time

        return None

    def _extract_time_from_servings_section(self, time_type):
        """Helper method to extract prep_time or cook_time from the Servings & Time section."""
        headings = self.soup.find_all(['h2'])
        for h in headings:
            text = h.get_text(" ", strip=True)
            normalized = text.replace("'", "'").replace("'", "'").lower()
            
            # Check for "Servings & Time" heading
            if "servings" in normalized and "time" in normalized:
                sib = h.find_next_sibling()
                while sib and getattr(sib, 'name', None) != 'p':
                    sib = sib.find_next_sibling()
                if sib and sib.name == 'p':
                    p_text = sib.get_text(" ", strip=True)
                    
                    # Look for the specific time type
                    pattern = f"{time_type} time:"
                    if pattern in p_text.lower():
                        try:
                            time_match = p_text.lower().split(pattern)[1]
                            # Split by other time fields or newlines
                            for delimiter in ["prep time:", "cook time:", "total time:", "\n", "<"]:
                                if delimiter in time_match:
                                    time_match = time_match.split(delimiter)[0].strip()
                                    break
                            else:
                                time_match = time_match.strip()
                            
                            # Handle "8 hours on low or 4 hours on high" - take first option
                            if " or " in time_match:
                                time_match = time_match.split(" or ")[0].strip()
                            elif ", or " in time_match:
                                time_match = time_match.split(", or ")[0].strip()
                            
                            # Handle ranges like "6–8 hours" - take the higher value
                            if "–" in time_match or "-" in time_match:
                                time_match = time_match.replace("–", "-")
                                parts = time_match.split("-", 1)
                                if len(parts) == 2:
                                    time_match = parts[1].strip()
                            
                            # Clean up extra text like "on low" or "on high"
                            for phrase in [" on low", " on high", " on medium"]:
                                if phrase in time_match.lower():
                                    time_match = time_match.lower().split(phrase)[0].strip()
                                    break
                            
                            return get_minutes(time_match)
                        except Exception:
                            pass
        return None

    def prep_time(self):
        return self._extract_time_from_servings_section("prep")

    def cook_time(self):
        return self._extract_time_from_servings_section("cook")

    def yields(self):
        headings = self.soup.find_all(['h2'])
        for h in headings:
            text = h.get_text(" ", strip=True)
            normalized = text.replace("'", "'").replace("'", "'").lower()
            
            # Check for "Servings & Time" heading - extract "Serves:" from paragraph
            if "servings" in normalized and "time" in normalized:
                sib = h.find_next_sibling()
                while sib and getattr(sib, 'name', None) != 'p':
                    sib = sib.find_next_sibling()
                if sib and sib.name == 'p':
                    p_text = sib.get_text(" ", strip=True)
                    # Look for "Serves:" pattern
                    if "serves:" in p_text.lower():
                        try:
                            serves_match = p_text.lower().split("serves:")[1]
                            # Split by common delimiters
                            for delimiter in ["prep time:", "cook time:", "total time:", "\n", "<", "<br"]:
                                if delimiter in serves_match:
                                    serves_match = serves_match.split(delimiter)[0].strip()
                                    break
                            else:
                                serves_match = serves_match.strip()
                            if serves_match:
                                return get_yields(serves_match)
                        except Exception:
                            pass
            
            # Check for standalone "Makes", "Servings", or "Serves" headings
            if normalized.strip() in ["makes", "servings", "serves"]:
                sib = h.find_next_sibling()
                while sib and getattr(sib, 'name', None) != 'p':
                    sib = sib.find_next_sibling()
                if sib and sib.name == 'p':
                    try:
                        yields_text = sib.get_text(" ", strip=True)
                        if yields_text:
                            return get_yields(yields_text)
                    except Exception:
                        pass
        
        return None

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
        if not entry:
            return ""
        
        # locate the H2 that labels the instructions section
        instr_heading = None
        for h in entry.find_all(['h2']):
            text = h.get_text(' ', strip=True).lower()
            if 'instructions' in text or 'how to make' in text:
                instr_heading = h
                break

        if not instr_heading:
            return ""

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
