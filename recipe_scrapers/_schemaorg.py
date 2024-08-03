# IF things in this file continue get messy (I'd say 300+ lines) it may be time to
# find a package that parses https://schema.org/Recipe properly (or create one ourselves).
from __future__ import annotations

from itertools import chain

import extruct

from recipe_scrapers.settings import settings

from ._exceptions import SchemaOrgException
from ._utils import (
    csv_to_tags,
    format_diet_name,
    get_minutes,
    get_yields,
    normalize_string,
)

SCHEMA_ORG_HOST = "schema.org"

SYNTAXES = ["json-ld", "microdata"]


class SchemaOrg:
    @staticmethod
    def _contains_schematype(item, schematype):
        itemtype = item.get("@type", "")
        itemtypes = itemtype if isinstance(itemtype, list) else [itemtype]
        return schematype.lower() in "\n".join(itemtypes).lower()

    def _find_entity(self, item, schematype):
        if self._contains_schematype(item, schematype):
            return item
        for graph in item.get("@graph", []):
            for node in graph if isinstance(graph, list) else [graph]:
                if self._contains_schematype(node, schematype):
                    return node

    def __init__(self, page_data):
        self.format = None
        self.data = {}
        self.people = {}
        self.ratingsdata = {}
        self.website_name = None

        data = extruct.extract(
            page_data,
            syntaxes=SYNTAXES,
            errors="log" if settings.LOG_LEVEL <= 10 else "ignore",
            uniform=True,
        )

        # Extract website data
        for syntax in SYNTAXES:
            syntax_data = data.get(syntax, [])
            for item in syntax_data:
                website = self._find_entity(item, "WebSite")
                if website:
                    self.website_name = website.get("name")

        # Extract person references
        for syntax in SYNTAXES:
            syntax_data = data.get(syntax, [])
            for item in syntax_data:
                if person := self._find_entity(item, "Person"):
                    key = person.get("@id") or person.get("url")
                    if key:
                        self.people[key] = person

        # Extract ratings data
        for syntax in SYNTAXES:
            syntax_data = data.get(syntax, [])
            for item in syntax_data:
                rating = self._find_entity(item, "AggregateRating")
                if rating:
                    rating_id = rating.get("@id")
                    if rating_id:
                        self.ratingsdata[rating_id] = rating

        for syntax in SYNTAXES:
            # Make sure entries of type Recipe are always parsed first
            syntax_data = data.get(syntax, [])
            try:
                index = [x.get("@type", "") for x in syntax_data].index("Recipe")
                syntax_data.insert(0, syntax_data.pop(index))
            except ValueError:
                pass

            for item in syntax_data:
                if SCHEMA_ORG_HOST not in item.get("@context", ""):
                    continue

                # If the item itself is a recipe, then use it directly as our datasource
                if recipe := self._find_entity(item, "Recipe"):
                    self.format = syntax
                    self.data = recipe
                    return

                # If the item is a webpage and describes a recipe entity, use the entity as our datasource
                if self._contains_schematype(item, "WebPage"):
                    main_entity = item.get("mainEntity", {})
                    if self._contains_schematype(main_entity, "Recipe"):
                        self.format = syntax
                        self.data = main_entity
                        return

    def site_name(self):
        if not self.website_name:
            raise SchemaOrgException("Site name not found in SchemaOrg")

        return normalize_string(self.website_name)

    def language(self):
        return self.data.get("inLanguage") or self.data.get("language")

    def title(self):
        return normalize_string(self.data.get("name"))

    def category(self):
        category = self.data.get("recipeCategory")
        if isinstance(category, list):
            return ",".join(category)
        return category

    def author(self):
        author = self.data.get("author") or self.data.get("Author")
        if (
            author
            and isinstance(author, list)
            and len(author) >= 1
            and isinstance(author[0], dict)
        ):
            author = author[0]
        if author and isinstance(author, dict):
            author_key = author.get("@id") or author.get("url")
            if author_key and author_key in self.people:
                author = self.people[author_key]
        if author and isinstance(author, dict):
            author = author.get("name")
        if author:
            return author.strip()

    def _read_duration_field(self, k: str) -> int | None:
        v = self.data.get(k)
        if v is None:
            return None
        if isinstance(v, str):
            return get_minutes(v)
        # Workaround: strictly speaking schema.org does not provide for minValue and maxValue properties on objects of type Duration; they are however present on objects with type QuantitativeValue
        # Refs:
        #  - https://schema.org/Duration
        #  - https://schema.org/QuantitativeValue
        if isinstance(v, dict) and v.get("maxValue"):
            return get_minutes(v["maxValue"])
        return None

    def total_time(self):
        if not (self.data.keys() & {"totalTime", "prepTime", "cookTime"}):
            raise SchemaOrgException("Cooking time information not found in SchemaOrg")

        total_time = self._read_duration_field("totalTime")
        if total_time:
            return total_time

        prep_time = self._read_duration_field("prepTime") or 0
        cook_time = self._read_duration_field("cookTime") or 0
        if prep_time or cook_time:
            return prep_time + cook_time

    def cook_time(self):
        if not (self.data.keys() & {"cookTime"}):
            raise SchemaOrgException("Cooktime information not found in SchemaOrg")
        return self._read_duration_field("cookTime")

    def prep_time(self):
        if not (self.data.keys() & {"prepTime"}):
            raise SchemaOrgException("Preptime information not found in SchemaOrg")
        return self._read_duration_field("prepTime")

    def yields(self):
        if not (self.data.keys() & {"recipeYield", "yield"}):
            raise SchemaOrgException("Servings information not found in SchemaOrg")
        yield_data = self.data.get("recipeYield") or self.data.get("yield")
        if yield_data and isinstance(yield_data, list):
            yield_data = yield_data[0]
        recipe_yield = str(yield_data)
        return get_yields(recipe_yield)

    def image(self):
        image = self.data.get("image")

        if image is None:
            raise SchemaOrgException("Image not found in SchemaOrg")

        if isinstance(image, list):
            # Could contain a dict
            image = image[0]

        if isinstance(image, dict):
            image = image.get("url")

        if "http://" not in image and "https://" not in image:
            # Some sites use relative image paths;
            # prefer generic image retrieval code in those cases.
            image = ""

        return image

    def ingredients(self):
        ingredients = (
            self.data.get("recipeIngredient") or self.data.get("ingredients") or []
        )

        if ingredients and isinstance(ingredients[0], list):
            ingredients = list(chain(*ingredients))  # flatten

        if ingredients and isinstance(ingredients, str):
            ingredients = [ingredients]

        return [
            normalize_string(ingredient) for ingredient in ingredients if ingredient
        ]

    def nutrients(self):
        nutrients = self.data.get("nutrition", {})
        cleaned_nutrients = {}

        for key, val in nutrients.items():
            if not key or key.startswith("@") or not val:
                continue

            cleaned_nutrients[key] = str(val)

        return {
            normalize_string(nutrient): normalize_string(value)
            for nutrient, value in cleaned_nutrients.items()
        }

    def _extract_howto_instructions_text(self, schema_item):
        instructions_gist = []
        if type(schema_item) is str:
            instructions_gist.append(schema_item)
        elif schema_item.get("@type") == "HowToStep":
            if schema_item.get("name", False):
                # some sites have duplicated name and text properties (1:1)
                # others have name same as text but truncated to X chars.
                # ignore name in these cases and add the name value only if it's different from the text
                if not schema_item.get("text").startswith(
                    schema_item.get("name").rstrip(".")
                ):
                    instructions_gist.append(schema_item.get("name"))
            if schema_item.get("itemListElement"):
                schema_item = schema_item.get("itemListElement")
            instructions_gist.append(schema_item.get("text"))
        elif schema_item.get("@type") == "HowToSection":
            name = schema_item.get("name") or schema_item.get("Name")
            if name is not None:
                instructions_gist.append(name)
            for item in schema_item.get("itemListElement"):
                instructions_gist += self._extract_howto_instructions_text(item)
        return instructions_gist

    def instructions(self):
        instructions = self.data.get("recipeInstructions") or ""

        if (
            instructions
            and isinstance(instructions, list)
            and isinstance(instructions[0], list)
        ):
            instructions = list(chain(*instructions))  # flatten

        if isinstance(instructions, dict):
            instructions = instructions.get("itemListElement")

        if isinstance(instructions, list):
            instructions_gist = []
            for schema_instruction_item in instructions:
                instructions_gist += self._extract_howto_instructions_text(
                    schema_instruction_item
                )

            return "\n".join(
                normalize_string(instruction) for instruction in instructions_gist
            )

        return instructions

    def ratings(self):
        ratings = self.data.get("aggregateRating") or self._find_entity(
            self.data, "AggregateRating"
        )
        if ratings and isinstance(ratings, dict):
            rating_id = ratings.get("@id")
            if rating_id and rating_id in self.ratingsdata:
                ratings = self.ratingsdata[rating_id]
        if ratings and isinstance(ratings, dict):
            ratings = ratings.get("ratingValue")
        if ratings:
            return round(float(ratings), 2)
        raise SchemaOrgException("No ratingValue in SchemaOrg.")

    def ratings_count(self):
        ratings = self.data.get("aggregateRating") or self._find_entity(
            self.data, "AggregateRating"
        )
        if isinstance(ratings, dict):
            rating_id = ratings.get("@id")
            if rating_id:
                ratings = self.ratingsdata.get(rating_id, ratings)
            ratings = ratings.get("ratingCount") or ratings.get("reviewCount")
        if ratings:
            return int(float(ratings)) if float(ratings) != 0 else None
        raise SchemaOrgException("No ratingCount in SchemaOrg.")

    def cuisine(self):
        cuisine = self.data.get("recipeCuisine")
        if cuisine is None:
            raise SchemaOrgException("No cuisine data in SchemaOrg.")
        elif isinstance(cuisine, list):
            return ",".join(cuisine)
        return cuisine

    def description(self):
        description = self.data.get("description")
        if description is None:
            raise SchemaOrgException("No description data in SchemaOrg.")
        if description and isinstance(description, list):
            description = description[0]
        return normalize_string(description)

    def cooking_method(self):
        cooking_method = self.data.get("cookingMethod")
        if cooking_method is None:
            raise SchemaOrgException("No cooking method data in SchemaOrg")
        if cooking_method and isinstance(cooking_method, list):
            cooking_method = cooking_method[0]
        return normalize_string(cooking_method)

    def keywords(self):
        keywords = self.data.get("keywords")
        if keywords is None:
            raise SchemaOrgException("No keywords data in SchemaOrg")
        if keywords:
            if isinstance(keywords, list):
                keywords = ", ".join(keywords)
            keywords = normalize_string(keywords)
            keywords = csv_to_tags(keywords)
        return keywords

    def dietary_restrictions(self):
        dietary_restrictions = self.data.get("suitableForDiet")
        if dietary_restrictions is None:
            raise SchemaOrgException("No dietary restrictions data in SchemaOrg.")
        if not isinstance(dietary_restrictions, list):
            dietary_restrictions = [dietary_restrictions]

        formatted_diets = [format_diet_name(diet) for diet in dietary_restrictions]
        formatted_diets = ", ".join(formatted_diets)
        final_diets = csv_to_tags(formatted_diets)

        return final_diets
