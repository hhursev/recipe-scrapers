import json
import re

from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml, FieldNotProvidedByWebsiteException
from ._utils import get_yields, normalize_string

_INSTRUCTION_START = re.compile(
    r"\b(?:Make|Cook|Prepare) the [^:]{1,80}:|\bInstructions:\s*",
)
_YIELD = re.compile(r"\b(?:Serves|Makes)\s+(\d+(?:\s+to\s+\d+)?)", re.IGNORECASE)
_SECTION_HEADER = re.compile(
    r"\s+(?:Spicy Egg Salad|Tostadas and Toppings)\s+",
    re.IGNORECASE,
)
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
_INGREDIENT_SPLIT = re.compile(
    r"(?<=\s)(?<!about )(?=(?:\d+[/\d]*|\d+|[\u00bc\u00bd\u00be\u2153\u2154]|\d+[\u00bc\u00bd\u00be\u2153\u2154])\s)"
    r"|(?<=\s)(?<!about )(?=\d+\s)"
    r"|(?<=[a-z,])\s+(?=\d+\-\w+\b)"
    r"|(?<=[a-z])\s+(?=1[\u00bc\u00bd\u00be\u2153\u2154]\s)"
    r"|(?<=\s)(?=(?:Kosher salt|Sliced chives|Tostadas,|Salt and pepper|Pitted dates)\b)",
    re.IGNORECASE,
)
_SENTENCE_STEP = re.compile(r"(?<=\.)\s+(?=[A-Z])")


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
            raise ElementNotFoundInHtml("Could not find recipe instructions in articleBody.")
        return match

    def _ingredient_blob(self, body):
        match = self._first_instruction_match(body)
        preamble = body[: match.start()]
        yield_matches = list(_YIELD.finditer(preamble))
        if yield_matches:
            preamble = preamble[yield_matches[-1].end() :]
        section = re.search(r"Spicy Egg Salad\s*", preamble, re.IGNORECASE)
        if section:
            preamble = preamble[section.end() :]
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
        blob = self._ingredient_blob(self._article_body())
        blob = _SECTION_HEADER.sub(" ", blob)
        blob = re.sub(r"\s+", " ", blob).strip()
        ingredients = [part.strip() for part in _INGREDIENT_SPLIT.split(blob) if part.strip()]
        normalized = []
        for ingredient in ingredients:
            if "Sliced chives" in ingredient and "Tostadas, for serving" in ingredient:
                ingredient = ingredient.replace("Tostadas, for serving", "").strip()
                normalized.append(ingredient)
                normalized.append("Tostadas, for serving")
            else:
                normalized.append(ingredient)
        return [
            normalize_string(ingredient) for ingredient in _merge_parenthetical_ingredients(normalized)
        ]

    def instructions(self):
        return "\n".join(self.instructions_list())

    def instructions_list(self):
        body = self._article_body()
        matches = list(_INSTRUCTION_START.finditer(body))
        if not matches:
            raise ElementNotFoundInHtml("Could not find recipe instructions in articleBody.")

        steps = []
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
            text = body[match.end() : end].strip()
            if re.match(r"^Instructions:\s*", match.group(0), re.IGNORECASE):
                text = re.sub(r"^Instructions:\s*", "", text, count=1, flags=re.IGNORECASE)
            else:
                text = re.sub(
                    r"^(?:Make|Cook|Prepare) the [^:]+:\s*",
                    "",
                    text,
                    count=1,
                    flags=re.IGNORECASE,
                )
            if len(matches) > 1:
                steps.append(normalize_string(text))
            elif re.match(r"^Instructions:\s*", match.group(0), re.IGNORECASE):
                steps.extend(
                    normalize_string(step)
                    for step in _split_instruction_text(text)
                    if step.strip()
                )
            elif re.search(r"\bPeel the eggs\b", text):
                steps.extend(
                    normalize_string(step)
                    for step in _huevos_instruction_steps(text)
                    if step.strip()
                )
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


def _merge_parenthetical_ingredients(ingredients):
    merged = []
    index = 0
    while index < len(ingredients):
        ingredient = ingredients[index]
        while ingredient.count("(") > ingredient.count(")") and index + 1 < len(ingredients):
            index += 1
            ingredient = f"{ingredient} {ingredients[index]}"
        merged.append(ingredient)
        index += 1
    return merged


def _split_instruction_text(text):
    steps = [step for step in _SENTENCE_STEP.split(text) if step.strip()]
    return steps if steps else [text]


def _huevos_instruction_steps(text):
    """Huevos articleBody runs steps together without Make-the subsections."""
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
