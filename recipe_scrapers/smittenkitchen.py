import functools
import re
from bs4 import Tag

from ._abstract import AbstractScraper
from ._exceptions import FieldNotProvidedByWebsiteException
from ._utils import normalize_string, get_yields


class SmittenKitchen(AbstractScraper):
    """
    Smitten Kitchen has two prominent layout styles:
    
    1. Modern format (approx. 2020+): Uses h-recipe microformat with schema.org
       - Contains .hrecipe container
       - Uses .jetpack-recipe-* classes
       - Has proper schema.org Recipe metadata
       
    2. Old format (pre-2020): Plain HTML embedded in blog post
       - Recipe content in .entry-content div
       - Title in <p><b>Title</b></p> after print-hide div
       - Ingredients in <u>Section</u> headers with <br/> separated items
       - Instructions in <i>Header:</i> paragraphs
       - Yields in "Serves X" text
    """

    @classmethod
    def host(cls):
        return "smittenkitchen.com"

    def _has_modern_format(self):
        """Check if the page uses the modern h-recipe format."""
        return self.soup.find("div", class_="hrecipe") is not None

    def _get_entry_content(self):
        """Get the entry-content div which contains the recipe in old format."""
        return self.soup.find("div", class_="entry-content")

    def author(self):
        """Return the recipe author."""
        if self._has_modern_format():
            try:
                author = self.schema.author()
                if author:
                    return author
            except Exception:
                pass
        # Both formats: Deb Perelman is the author
        return "Deb Perelman"

    def title(self):
        """Return the recipe title."""
        if self._has_modern_format():
            # Modern format: try schema first, then h-recipe title
            try:
                title = self.schema.title()
                if title:
                    return title
            except Exception:
                pass
            title_elem = self.soup.find("h3", class_="jetpack-recipe-title")
            if title_elem:
                return normalize_string(title_elem.get_text())
        else:
            # Old format: title is in <p><b>Title</b></p> after print-hide div
            entry = self._get_entry_content()
            if entry:
                print_hide = entry.find("div", class_="smittenkitchen-print-hide")
                if print_hide:
                    # Look for next p > b after print-hide
                    for elem in print_hide.find_all_next("p"):
                        if isinstance(elem, Tag) and elem.find("b"):
                            b = elem.find("b")
                            return normalize_string(b.get_text())
        # Fallback to entry-title h1
        title_elem = self.soup.find("h1", class_="entry-title")
        if title_elem:
            return normalize_string(title_elem.get_text())
        return ""

    def ingredients(self):
        """Return the list of ingredients."""
        if self._has_modern_format():
            return self._ingredients_modern()
        else:
            return self._ingredients_old()

    def _ingredients_modern(self):
        """Extract ingredients from modern h-recipe format."""
        try:
            return self.schema.ingredients()
        except Exception:
            pass
        # Fallback to direct extraction
        ingredients = []
        for li in self.soup.find_all("li", class_="jetpack-recipe-ingredient"):
            text = normalize_string(li.get_text())
            if text:
                ingredients.append(text)
        return ingredients

    def _ingredients_old(self):
        """
        Extract ingredients from old format.
        
        Old format structure:
        <p><u>For the chickpeas</u><br/>
        1 pound dried chickpeas...<br/>
        1/4 cup olive oil<br/>
        ...</p>
        """
        entry = self._get_entry_content()
        if not entry:
            return []

        ingredients = []
        
        # Find the print-hide div to know where to start looking
        print_hide = entry.find("div", class_="smittenkitchen-print-hide")
        start_from = print_hide if print_hide else entry
        
        # Look for paragraphs with underlined headers (ingredient sections)
        for p in start_from.find_all_next("p") if print_hide else entry.find_all("p"):
            if not isinstance(p, Tag):
                continue
                
            u = p.find("u")
            if u:
                # This is an ingredient section header - extract items
                # Get text after the <u> element, split by <br/>
                html_str = str(p)
                # Remove the <u>...</u> part
                html_str = re.sub(r'<u>[^<]*</u>', '', html_str, count=1)
                # Get text content
                text_content = p.get_text(separator="\n")
                lines = text_content.split("\n")
                
                for line in lines:
                    line = normalize_string(line)
                    # Skip empty lines and section headers
                    if line and not line.endswith(":") and not line.lower().startswith("for "):
                        # Check if it looks like an ingredient (has measurement)
                        if any(c.isdigit() for c in line) or any(unit in line.lower() for unit in ["cup", "tbsp", "tsp", "tablespoon", "teaspoon", "ounce", "pound", "lb", "oz", "gram", "g ", "kg", "ml", "l ", "bunch", "handful", "clove", "slice"]):
                            if not line.lower().startswith("serves") and not line.lower().startswith("note:"):
                                ingredients.append(line)
            else:
                # Check for "Fixings" style paragraph
                text = p.get_text(strip=True)
                if text.startswith("Fixings") or text.startswith("For the"):
                    # Process br-separated items
                    html_str = str(p)
                    # Remove the header text
                    if "<br" in html_str.lower():
                        # Split by br tags and process
                        parts = re.split(r'<br\s*/?>', html_str, flags=re.IGNORECASE)
                        for part in parts[1:]:  # Skip first part (header)
                            # Extract text between tags
                            clean = re.sub(r'<[^>]*>', '', part)
                            line = normalize_string(clean)
                            if line and any(c.isdigit() for c in line):
                                ingredients.append(line)
        
        return ingredients

    @functools.cached_property
    def _instructions_list_data(self):
        """
        Cached instructions extraction for both formats.
        Returns list of instruction strings.
        """
        if self._has_modern_format():
            return self._instructions_list_modern()
        else:
            return self._instructions_list_old()

    def _instructions_list_modern(self):
        """Extract instructions from modern h-recipe format."""
        try:
            return self.instructions_list()
        except Exception:
            pass
        # Fallback
        directions = self.soup.find("div", class_="jetpack-recipe-directions")
        if directions:
            instructions = []
            for p in directions.find_all("p"):
                text = normalize_string(p.get_text())
                if text:
                    instructions.append(text)
            return instructions
        return []

    def _instructions_list_old(self):
        """
        Extract instructions from old format.
        
        Old format structure:
        <p><i>Soak dried chickpeas:</i> Do you have to...</p>
        <p><i>Prepare your chickpeas:</i> Heat oven...</p>
        <p><em>To make pita chips:</em> Separate...</p>
        """
        entry = self._get_entry_content()
        if not entry:
            return []

        instructions = []
        
        # Find print-hide div to start after
        print_hide = entry.find("div", class_="smittenkitchen-print-hide")
        
        # Find all paragraphs with italic or emphasized headers
        for p in entry.find_all("p"):
            if not isinstance(p, Tag):
                continue
            
            # Skip paragraphs before print-hide if present
            if print_hide and p.sourceline and print_hide.sourceline:
                if p.sourceline <= print_hide.sourceline:
                    continue
            
            text = normalize_string(p.get_text())
            if not text:
                continue
            
            # Check for italic instruction headers (ends with :)
            i = p.find("i")
            if i:
                header_text = i.get_text()
                if header_text.endswith(":"):
                    instructions.append(text)
                    continue
            
            # Check for emphasized sub-instructions (starts with "To ")
            em = p.find("em")
            if em:
                em_text = em.get_text()
                if em_text.lower().startswith("to "):
                    instructions.append(text)
        
        return instructions

    def instructions(self):
        """Return the recipe instructions as a string."""
        data = self._instructions_list_data
        return "\n".join(data) if data else None

    def instructions_list(self):
        """Return the recipe instructions as a list."""
        return self._instructions_list_data

    def yields(self):
        """Return the recipe yield."""
        if self._has_modern_format():
            # Modern format
            try:
                return self.schema.yields()
            except Exception:
                pass
            servings = self.soup.find("li", class_="jetpack-recipe-servings")
            if servings:
                text = servings.get_text()
                if "Servings:" in text:
                    return get_yields(text.split("Servings:", 1)[1].strip())
        else:
            # Old format: look for "Serves X" text
            entry = self._get_entry_content()
            if entry:
                # Find print-hide to start after
                print_hide = entry.find("div", class_="smittenkitchen-print-hide")
                search_in = print_hide.find_all_next("p") if print_hide else entry.find_all("p")
                
                for p in search_in:
                    if not isinstance(p, Tag):
                        continue
                    text = p.get_text(strip=True)
                    if text.lower().startswith("serves "):
                        return get_yields(text)
        return None

    def total_time(self):
        """Return the total time in minutes."""
        if self._has_modern_format():
            try:
                return self.schema.total_time()
            except Exception:
                pass
            # Parse ISO 8601 duration
            time_elem = self.soup.find("time", itemprop="totalTime")
            if time_elem and time_elem.get("datetime"):
                dt = time_elem["datetime"]
                # Parse P0DT1H30M0S format
                match = re.search(r'PT(?:(\d+)H)?(?:(\d+)M)?', dt)
                if match:
                    hours = int(match.group(1) or 0)
                    minutes = int(match.group(2) or 0)
                    return hours * 60 + minutes
        # Old format doesn't consistently have time
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def prep_time(self):
        """Return the prep time in minutes."""
        if self._has_modern_format():
            try:
                return self.schema.prep_time()
            except Exception:
                pass
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def cook_time(self):
        """Return the cook time in minutes."""
        if self._has_modern_format():
            try:
                return self.schema.cook_time()
            except Exception:
                pass
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def image(self):
        """Return the recipe image URL."""
        if self._has_modern_format():
            try:
                return self.schema.image()
            except Exception:
                pass
        # Fallback to first image in entry content
        entry = self._get_entry_content()
        if entry:
            img = entry.find("img", src=True)
            if img:
                return img["src"]
        return None

    def description(self):
        """Return the recipe description."""
        if self._has_modern_format():
            try:
                return self.schema.description()
            except Exception:
                pass
        # Try meta description
        meta = self.soup.find("meta", property="og:description")
        if meta:
            return meta.get("content", "")
        return None

    def site_name(self):
        """Return the site name."""
        return "smitten kitchen"

    def language(self):
        """Return the recipe language."""
        html = self.soup.find("html", lang=True)
        if html:
            return html.get("lang")
        return "en-US"
