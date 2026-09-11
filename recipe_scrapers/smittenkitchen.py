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

    def _get_old_format_recipe_bounds(self, entry):
        """
        Find the start and end boundaries of the recipe content in old format.
        
        Returns (start_elem, end_elem) where:
        - start_elem: The paragraph containing the recipe title
        - end_elem: The element where recipe content ends (sharedaddy, jp-relatedposts, etc.)
        """
        print_hide = entry.find("div", class_="smittenkitchen-print-hide")
        
        # Find end boundary first - these mark the end of recipe content
        end_markers = [
            entry.find("div", class_="sharedaddy"),
            entry.find("div", id="jp-relatedposts"),
            entry.find("script", string=re.compile(r"printRecipeButton")),
        ]
        # Filter out None values and get the first one with lowest line number
        end_markers = [m for m in end_markers if m is not None]
        end_elem = None
        if end_markers:
            # Sort by sourceline to get the first one
            end_markers.sort(key=lambda x: getattr(x, 'sourceline', float('inf')))
            end_elem = end_markers[0]
        
        # Find start - look for the recipe title paragraph
        # Must be after print-hide and before end_elem
        start_elem = None
        
        # Get candidate paragraphs
        if print_hide:
            candidates = list(print_hide.find_all_next("p"))
        else:
            candidates = list(entry.find_all("p"))
        
        # Filter to those before end_elem
        if end_elem:
            candidates = [p for p in candidates 
                         if p.sourceline and end_elem.sourceline 
                         and p.sourceline < end_elem.sourceline]
        
        # Find the first paragraph with <b> that looks like a recipe title
        for p in candidates:
            if not isinstance(p, Tag):
                continue
                
            b = p.find("b")
            if b:
                b_text = normalize_string(b.get_text())
                # Skip "One year ago" style content - these are sidebar widgets
                if any(phrase in b_text.lower() for phrase in ["year ago", "years ago", "months ago", "one year", "two years", "three years", "four years", "five years", "six years", "seven years", "eight years"]):
                    continue
                # Skip if too short or looks like a date reference
                if len(b_text) < 3:
                    continue
                # This looks like a recipe title
                start_elem = p
                break
        
        return start_elem, end_elem

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
        # Both formats: h1.entry-title has the correct lowercase title
        title_elem = self.soup.find("h1", class_="entry-title")
        if title_elem:
            return normalize_string(title_elem.get_text())
        
        if self._has_modern_format():
            # Modern format fallback: try schema then h-recipe title
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
            # Old format fallback: use the bounded search
            entry = self._get_entry_content()
            if entry:
                start_elem, _ = self._get_old_format_recipe_bounds(entry)
                if start_elem:
                    b = start_elem.find("b")
                    if b:
                        return normalize_string(b.get_text())
        
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
        start_elem, end_elem = self._get_old_format_recipe_bounds(entry)
        
        if not start_elem:
            return []
        
        # Get all paragraphs between start and end
        candidates = list(start_elem.find_all_next("p"))
        if end_elem:
            candidates = [p for p in candidates 
                         if p.sourceline and end_elem.sourceline 
                         and p.sourceline < end_elem.sourceline]
        
        for p in candidates:
            if not isinstance(p, Tag):
                continue
            
            # Skip the "See also:" section
            text = p.get_text(strip=True)
            if text.startswith("See also:"):
                continue
                
            u = p.find("u")
            if u:
                # This is an ingredient section - extract items split by <br/>
                u_text = normalize_string(u.get_text())
                
                # Get the full paragraph HTML to split by br tags
                html_str = str(p)
                
                # Remove the <u>...</u> part
                html_str = re.sub(r'<u>[^\u003c]*</u>', '', html_str, count=1)
                
                # Split by <br> tags
                parts = re.split(r'<br\s*/?>', html_str, flags=re.IGNORECASE)
                
                for part in parts:
                    # Remove any remaining HTML tags
                    clean = re.sub(r'<[^>]*>', '', part)
                    line = normalize_string(clean)
                    
                    # Skip empty lines
                    if not line:
                        continue
                    # Skip section header text
                    if line.lower() == u_text.lower():
                        continue
                    # Skip instructional text in parentheses
                    if line.startswith("(") and line.endswith(")"):
                        continue
                    if line.lower() in ["(all instructions below)"]:
                        continue
                    
                    # Check if it looks like an ingredient
                    # Ingredients should be relatively short (not full sentences)
                    is_short = len(line) < 150  # Exclude blog text
                    
                    # Has measurement indicators
                    has_measurement = (
                        any(c.isdigit() for c in line) or 
                        any(unit in line.lower() for unit in ["cup", "tbsp", "tsp", "tablespoon", "teaspoon", "ounce", "pound", "lb", "oz", "gram", "g ", "kg", "ml", "l ", "bunch", "handful", "clove", "slice", "pinch", "dash", "grating", "sprinkling"])
                    )
                    
                    # Is a food item (based on keywords)
                    is_food = any(keyword in line.lower() for keyword in [
                        "fresh ", "salt", "pepper", "zest", "juice", "salad", "yogurt", 
                        "sauce", "oil", "butter", "cheese", "herb", "spice", "nut", "seed"
                    ])
                    
                    # Is likely an ingredient if it's short and (has measurement or is a food item)
                    if is_short and (has_measurement or is_food):
                        if not line.lower().startswith("serves") and not line.lower().startswith("note:"):
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
        directions = self.soup.find("div", class_="jetpack-recipe-directions")
        if directions:
            instructions = []
            
            # The directions div is sometimes wrapped in a <p> tag
            # and the instructions are siblings of that wrapper
            # HTML structure: <p><div class="directions">...</div></p> <p>instruction</p>
            
            # Get text from the directions div itself (first instruction)
            div_text = normalize_string(directions.get_text())
            if div_text:
                instructions.append(div_text)
            
            # Find the container (parent <p> or the div itself) to get siblings
            container = directions.parent if directions.parent and directions.parent.name == 'p' else directions
            
            # Get subsequent <p> siblings
            for sibling in container.find_next_siblings("p"):
                text = normalize_string(sibling.get_text())
                if text:
                    instructions.append(text)
            
            if instructions:
                return instructions
        
        # Fallback: Try schema.org
        try:
            schema_instr = self.schema.instructions()
            if schema_instr:
                lines = [line.strip() for line in schema_instr.split('\n') if line.strip()]
                if len(lines) > 1:
                    return lines
                text = lines[0] if lines else ""
                if text:
                    steps = re.split(r'\.\s+(?=[A-Z])', text)
                    steps = [s.strip() + '.' if not s.strip().endswith('.') else s.strip() for s in steps if s.strip()]
                    if len(steps) > 1:
                        return steps
                    return [text]
        except Exception:
            pass
        
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
        start_elem, end_elem = self._get_old_format_recipe_bounds(entry)
        
        if not start_elem:
            return []
        
        # Get all paragraphs between start and end
        # Skip the start_elem itself (it's the title, not an instruction)
        candidates = list(start_elem.find_all_next("p"))
        if end_elem:
            candidates = [p for p in candidates 
                         if p.sourceline and end_elem.sourceline 
                         and p.sourceline < end_elem.sourceline]
        
        # Track whether we've found the first actual recipe instruction
        # Recipe instructions start with <i>Header:</i> or <em>To ...</em>
        for p in candidates:
            if not isinstance(p, Tag):
                continue
            
            text = normalize_string(p.get_text())
            if not text:
                continue
            
            # Check for italic instruction headers (ends with :)
            i = p.find("i")
            if i:
                header_text = normalize_string(i.get_text())
                if header_text.endswith(":"):
                    # Skip if it looks like "Note:" without actual instruction content
                    if header_text.lower() == "note:" and len(text) < 20:
                        continue
                    instructions.append(text)
                    continue
            
            # Check for emphasized sub-instructions (starts with "To ")
            em = p.find("em")
            if em:
                em_text = normalize_string(em.get_text())
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
            # Modern format: Check HTML element first, then schema
            servings = self.soup.find("li", class_="jetpack-recipe-servings")
            if servings:
                text = servings.get_text()
                if "Servings:" in text:
                    servings_text = text.split("Servings:", 1)[1].strip()
                    # Handle ranges like "20 to 24" directly
                    import re
                    range_match = re.search(r'(\d+)\s+to\s+(\d+)', servings_text)
                    if range_match:
                        return f"{range_match.group(1)} to {range_match.group(2)} servings"
                    return get_yields(servings_text)
            
            # Fallback to schema
            try:
                return self.schema.yields()
            except Exception:
                pass
        else:
            # Old format: look for "Serves X" text
            entry = self._get_entry_content()
            if entry:
                start_elem, end_elem = self._get_old_format_recipe_bounds(entry)
                
                # Search in paragraphs between bounds
                candidates = list(start_elem.find_all_next("p")) if start_elem else entry.find_all("p")
                if end_elem:
                    candidates = [p for p in candidates 
                                 if p.sourceline and end_elem.sourceline 
                                 and p.sourceline < end_elem.sourceline]
                
                for p in candidates:
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
