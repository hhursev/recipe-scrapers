import json
import re

from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml, FieldNotProvidedByWebsiteException
from ._utils import get_yields, normalize_string

# Section headers like "Make the …:", "Grill the …:", "Combine the …:", etc.
# Avoid matching across sentence periods (e.g. "Serve at room temperature. Note:").
_INSTRUCTION_START = re.compile(
    r"\b(?:Make|Cook|Prepare|Grill|Finish|Combine|Assemble|Bake|Fry|Toss)"
    r"(?:\s+the)?\s+[^.:]{1,60}:|\bInstructions:\s*",
    re.IGNORECASE,
)
_YIELD = re.compile(r"\b(?:Serves|Makes)\s+(\d+(?:\s+to\s+\d+)?)", re.IGNORECASE)
_FIRST_INGREDIENT = re.compile(
    r"(?<!\w)"
    r"(?:"
    r"\d+[\d/½¼¾⅓⅔]*\s*(?:\(\d+[^)]+\)\s+)?"
    r"|[¼½¾⅓⅔]\s*"
    r")"
    r"(?:\d+[\d/]*\s+)?"
    r"(?:cups?|tablespoons?|teaspoons?|pounds?|ounces?|eggs?|live|cloves?|inch|sticks?|"
    r"cans?|pieces?|sprigs?|heads?|bags?|medium|large|small|whole|dry|raw|guajillo|chiles?)",
    re.IGNORECASE,
)
# Amount-less lines that are still ingredients (not section headers).
_AMOUNTLESS_INGREDIENT = re.compile(
    r"^(?:Kosher salt|Salt and pepper|Salt|Pepper|"
    r"Sliced chives,? for serving|Tostadas,? for serving|Pitted dates,? for serving|"
    r"Basil leaves|Yellow peach slices)\b",
    re.IGNORECASE,
)
_AMOUNTLESS_SPLIT_NAMES = (
    "Kosher salt",
    "Salt and pepper",
    "Sliced chives",
    "Tostadas,",
    "Tostadas ",
    "Pitted dates",
    "Basil leaves",
    "Yellow peach slices",
)
_SENTENCE_STEP = re.compile(r"(?<=\.)\s+(?=[A-Z])")
# Do not start a new ingredient at a quantity that continues a range/alternative
# ("1 large or 2 medium", "into ¼-inch slices").
_QUANTITY_CONTINUATION = re.compile(r"\b(?:or|to|and|into)$", re.IGNORECASE)


class SFChronicle(AbstractScraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._news_article = self._find_news_article()

    @classmethod
    def host(cls):
        return "sfchronicle.com"

    def _find_news_article(self):
        for script in self.soup.find_all("script", type="application/ld+json"):
            if not script.string:
                continue
            try:
                data = json.loads(script.string)
            except json.JSONDecodeError:
                continue
            items = data if isinstance(data, list) else [data]
            for item in items:
                if not isinstance(item, dict):
                    continue
                item_type = item.get("@type", "")
                types = item_type if isinstance(item_type, list) else [item_type]
                if any(t == "NewsArticle" for t in types):
                    return item
        raise ElementNotFoundInHtml("Could not find NewsArticle JSON-LD.")

    def _article_body(self):
        return self._news_article.get("articleBody") or ""

    def _first_instruction_match(self, body):
        match = _INSTRUCTION_START.search(body)
        if not match:
            raise ElementNotFoundInHtml(
                "Could not find recipe instructions in articleBody."
            )
        return match

    def _ingredient_blob(self, body):
        match = self._first_instruction_match(body)
        preamble = body[: match.start()]
        yield_matches = list(_YIELD.finditer(preamble))
        if yield_matches:
            preamble = preamble[yield_matches[-1].end() :]
        first_ingredient = _FIRST_INGREDIENT.search(preamble)
        if first_ingredient:
            return preamble[first_ingredient.start() :]
        quantity = re.search(r"(?<=\s)(\d+\s+\w+\b)", preamble)
        if quantity:
            return preamble[quantity.start(1) :]
        return preamble

    def author(self):
        author = self._news_article.get("author")
        if isinstance(author, list) and author:
            author = author[0]
        if isinstance(author, dict):
            return author.get("name")
        if isinstance(author, str):
            return author
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def title(self):
        headline = self._news_article.get("headline", "")
        return re.sub(r"^Recipe:\s*", "", headline, flags=re.IGNORECASE).strip()

    def category(self):
        return self._news_article.get("articleSection")

    def total_time(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def yields(self):
        match = _YIELD.search(self._article_body())
        if match:
            return get_yields(match.group(0))
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def image(self):
        image = self._news_article.get("image")
        if isinstance(image, dict):
            return image.get("url") or image.get("thumbnailUrl")
        if isinstance(image, str):
            return image
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def ingredients(self):
        blob = re.sub(r"\s+", " ", self._ingredient_blob(self._article_body())).strip()
        ingredients = [
            normalize_string(token) for token in _split_ingredient_blob(blob) if token
        ]
        return _merge_parenthetical_ingredients(ingredients)

    def instructions(self):
        return "\n".join(self.instructions_list())

    def instructions_list(self):
        body = self._article_body()
        matches = list(_INSTRUCTION_START.finditer(body))
        if not matches:
            raise ElementNotFoundInHtml(
                "Could not find recipe instructions in articleBody."
            )

        steps = []
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
            text = body[match.end() : end].strip()
            if re.match(r"^Instructions:\s*", match.group(0), re.IGNORECASE):
                text = re.sub(
                    r"^Instructions:\s*", "", text, count=1, flags=re.IGNORECASE
                )
            else:
                text = re.sub(
                    r"^(?:Make|Cook|Prepare|Grill|Finish|Combine|Assemble|Bake|Fry|Toss)"
                    r"(?:\s+the)?\s+[^.:]+:\s*",
                    "",
                    text,
                    count=1,
                    flags=re.IGNORECASE,
                )
            if re.search(r"\bPeel the eggs\b", text):
                # Huevos: one Make-block with several sentences, then Finish.
                steps.extend(
                    normalize_string(step)
                    for step in _huevos_instruction_steps(text)
                    if step.strip()
                )
            elif len(matches) > 1:
                steps.append(normalize_string(text))
            else:
                for step in _split_instruction_text(text):
                    if step.strip():
                        steps.append(normalize_string(step))
        return steps

    def description(self):
        description = self._news_article.get("description")
        if description:
            return normalize_string(description)
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def site_name(self):
        publisher = self._news_article.get("publisher", {})
        if isinstance(publisher, dict) and publisher.get("name"):
            return publisher["name"]
        return "San Francisco Chronicle"


def _is_section_header(token: str) -> bool:
    text = token.strip()
    if not text or len(text) > 60:
        return False
    if re.match(r"^[\d¼½¾⅓⅔]", text):
        return False
    if _AMOUNTLESS_INGREDIENT.match(text):
        return False
    if "." in text or text.endswith(","):
        return False
    if not re.match(r"^[A-Za-z]", text):
        return False
    if len(text.split()) > 6:
        return False
    return True


def _split_ingredient_blob(blob: str):
    marks = set()
    for match in re.finditer(
        r"(?<=\s)(?=(?:\d+[\d/½¼¾⅓⅔]*|[¼½¾⅓⅔]|1[¼½¾⅓⅔])(?:\s|-))"
        r"|(?<=[a-z,])\s+(?=\d+\-\w+\b)",
        blob,
        re.IGNORECASE,
    ):
        prev = blob[: match.start()].rstrip()
        if _QUANTITY_CONTINUATION.search(prev):
            continue
        marks.add(match.start())

    for name in _AMOUNTLESS_SPLIT_NAMES:
        for match in re.finditer(rf"(?<=\s)(?={re.escape(name)})", blob, re.IGNORECASE):
            marks.add(match.start())

    parts = []
    start = 0
    for pos in sorted(marks):
        if pos <= start:
            continue
        parts.append(blob[start:pos].strip())
        start = pos
    parts.append(blob[start:].strip())

    ingredients = []
    for token in parts:
        if not token:
            continue
        leading_header = re.match(
            r"^(.+?)\s+((?:\d+[\d/½¼¾⅓⅔]*|[¼½¾⅓⅔]).*)$",
            token,
        )
        if leading_header and _is_section_header(leading_header.group(1)):
            token = leading_header.group(2)
        if (
            _is_section_header(token)
            and not _AMOUNTLESS_INGREDIENT.match(token)
            and not re.match(r"^[\d¼½¾⅓⅔]", token)
        ):
            continue
        trailing = re.search(
            r"^(.*(?:oil|Parmesan|chopped|packed|vinegar|salt|pepper|powder|"
            r"instructions?|grilled|cubes?|slices?|serving))\s+"
            r"([A-Z][A-Za-z-]*(?:\s+[A-Za-z-]*){0,4})$",
            token,
        )
        if trailing and _is_section_header(trailing.group(2)):
            token = trailing.group(1).strip()
        if token:
            ingredients.append(token)
    return ingredients


def _merge_parenthetical_ingredients(ingredients):
    merged = []
    index = 0
    while index < len(ingredients):
        ingredient = ingredients[index]
        while ingredient.count("(") > ingredient.count(")") and index + 1 < len(
            ingredients
        ):
            index += 1
            ingredient = f"{ingredient} {ingredients[index]}"
        merged.append(ingredient)
        index += 1
    return merged


def _split_instruction_text(text):
    steps = [step for step in _SENTENCE_STEP.split(text) if step.strip()]
    return steps if steps else [text]


def _huevos_instruction_steps(text):
    """Huevos Make-block runs several steps together before Finish."""
    splits = [
        r"(?<=\.)\s+(?=Peel the eggs\b)",
        r"(?<=\.)\s+(?=Heat oil in\b)",
        r"Finish the tostadas:\s*",
    ]
    parts = [text]
    for pattern in splits:
        next_parts = []
        for part in parts:
            next_parts.extend(re.split(pattern, part, flags=re.IGNORECASE))
        parts = next_parts
    return [part for part in parts if part.strip()]
