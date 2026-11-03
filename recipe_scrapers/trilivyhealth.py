import re

from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml
from ._grouping_utils import IngredientGroup
from ._utils import get_minutes, get_yields, normalize_string

# The site is a Wix blog without schema.org Recipe markup, so the recipe is parsed
# from the post body. Section headings vary between posts ("Ingredients",
# "What you'll need...", "Directions", "How to make..."), so sections are located
# by heading text, then items are collected until the next heading of the same or
# higher level. Ingredient sub-headings (h3/h4) become ingredient groups.
HEADING_TAGS = ["h1", "h2", "h3", "h4", "h5", "h6"]
INGREDIENTS_HEADING = re.compile(r"ingredients|you(?:'|’)ll need|what you need", re.I)
INSTRUCTIONS_HEADING = re.compile(
    r"directions|instructions|how to make|step[- ]by[- ]step", re.I
)
STEP_LABEL = re.compile(r"^step\s*\d+\b", re.I)
METADATA_LINE = re.compile(
    r"^(?:yield|servings?|serves|per serving|total time|prep time|cook time)\b",
    re.I,
)
YIELD_LINE = re.compile(r"^(?:yield|servings?|serves)\s*:\s*(.+)$", re.I)
MAKES_SERVINGS = re.compile(r"\bmakes\s+(\d+\s+servings?)\b", re.I)


class TrilivyHealth(AbstractScraper):
    @classmethod
    def host(cls):
        return "blog.trilivyhealth.com"

    def author(self):
        # Posts don't display an author; the JSON-LD only has a Wix username.
        return self.site_name()

    def title(self):
        title = self.soup.find("h1", {"data-hook": "post-title"})
        if not title:
            raise ElementNotFoundInHtml("Could not find the post title.")
        return title.get_text()

    def description(self):
        # Wix emits this tag only for an author-written SEO description; otherwise
        # the JSON-LD and OpenGraph descriptions are an excerpt of the post body.
        description = self.soup.find("meta", {"name": "description", "content": True})
        if not description:
            raise ElementNotFoundInHtml("Could not find the post description.")
        return normalize_string(description["content"])

    def image(self):
        return self.opengraph.image()

    def total_time(self):
        return get_minutes(self._labelled_value("total time"))

    def prep_time(self):
        return get_minutes(self._labelled_value("prep time"))

    def yields(self):
        for text in self._block_texts():
            if match := YIELD_LINE.match(text):
                return get_yields(match.group(1))
        if match := MAKES_SERVINGS.search(self._post().get_text(" ")):
            return get_yields(match.group(1))
        raise ElementNotFoundInHtml("Could not find the recipe yield.")

    def ingredients(self):
        return [
            ingredient
            for group in self.ingredient_groups()
            for ingredient in group.ingredients
        ]

    def ingredient_groups(self):
        heading = self._find_heading(INGREDIENTS_HEADING)
        if heading is None:
            raise ElementNotFoundInHtml("Could not find the ingredients section.")

        groups = [IngredientGroup(ingredients=[], purpose=None)]
        paragraphs = []
        for element in self._section_elements(heading):
            if element.name in HEADING_TAGS:
                purpose = normalize_string(element.get_text()).rstrip(":").strip()
                groups.append(IngredientGroup(ingredients=[], purpose=purpose))
            elif element.name == "li":
                if text := self._item_text(element):
                    groups[-1].ingredients.append(text)
            elif text := self._item_text(element):
                paragraphs.append(text)

        groups = [group for group in groups if group.ingredients]
        if not groups and paragraphs:
            # Some posts list each ingredient as its own paragraph.
            groups = [IngredientGroup(ingredients=paragraphs, purpose=None)]
        return groups

    def instructions(self):
        start = self._find_heading(INGREDIENTS_HEADING)
        heading = self._find_heading(INSTRUCTIONS_HEADING, after=start)
        if heading is None:
            raise ElementNotFoundInHtml("Could not find the instructions section.")

        steps, paragraphs = [], []
        for element in self._section_elements(heading):
            if element.name in HEADING_TAGS:
                continue
            text = self._item_text(element)
            if not text:
                continue
            (steps if element.name == "li" else paragraphs).append(text)

        if not steps:
            # Some posts write steps as "Step 1: ..." paragraphs, preceded by an
            # introduction and the yield/time summary.
            first_step = next(
                (i for i, text in enumerate(paragraphs) if STEP_LABEL.match(text)),
                0,
            )
            steps = [
                text
                for text in paragraphs[first_step:]
                if not STEP_LABEL.match(text) and not METADATA_LINE.match(text)
            ]
        return "\n".join(steps)

    def _post(self):
        post = self.soup.find(attrs={"data-hook": "post-description"})
        if post is None:
            raise ElementNotFoundInHtml("Could not find the post content.")
        return post

    def _find_heading(self, pattern, after=None):
        headings = [
            heading
            for heading in self._post().find_all(HEADING_TAGS)
            if not heading.find_parent("li")
        ]
        start = next((i + 1 for i, h in enumerate(headings) if h is after), 0)
        for heading in headings[start:]:
            if pattern.search(heading.get_text()):
                return heading
        return None

    def _section_elements(self, heading):
        """Yield the sub-headings, top-level list items and paragraphs that
        follow `heading`, until the next heading of the same or higher level."""
        level = int(heading.name[1])
        post = self._post()
        for element in heading.find_all_next(HEADING_TAGS + ["li", "p"]):
            if not any(parent is post for parent in element.parents):
                return
            if element.name in HEADING_TAGS:
                if int(element.name[1]) <= level:
                    return
                yield element
            elif element.name == "li":
                if not element.find_parent("li"):
                    yield element
            elif not element.find_parent(["li"] + HEADING_TAGS):
                yield element

    @staticmethod
    def _item_text(element):
        # Wix sometimes nests the next group's heading inside the previous list
        # item, so heading text is excluded from item text.
        parts = [
            text
            for text in element.find_all(string=True)
            if not text.find_parent(HEADING_TAGS)
        ]
        return normalize_string("".join(parts))

    def _block_texts(self):
        for element in self._post().find_all(["p", "li"] + HEADING_TAGS):
            if text := normalize_string(element.get_text(" ")):
                yield text

    def _labelled_value(self, label):
        pattern = re.compile(rf"^{label}\s*:\s*(.+)$", re.I)
        for text in self._block_texts():
            if match := pattern.match(text):
                return match.group(1)
        raise ElementNotFoundInHtml(f"Could not find '{label}' in the post.")
