from ._abstract import AbstractScraper, HEADERS
import extruct
import isodate
import requests
from w3lib.html import get_base_url

SCHEMA_ORG_HOST = "schema.org"
SCHEMA_NAME = "Recipe"
SCHEMA_URL = f"https://{SCHEMA_ORG_HOST}/{SCHEMA_NAME}"

SYNTAXES = ["microdata", "json-ld"]


class SchemaOrg(AbstractScraper):

    def __init__(self, url, test=False):
        self.format = None
        self.testing_mode = test
        self.data = {}
        self.format = None

        if test:  # when testing, we load a file
            with url:
                r = url.read()
                data = extruct.extract(
                    r,
                    base_url="https://www.allrecipes.com/recipe/133948/four-cheese-margherita-pizza/",
                    syntaxes=SYNTAXES,
                    uniform=True,
            )
        else:
            r = requests.get(url, headers=HEADERS)
            data = extruct.extract(
                r.text,
                base_url=get_base_url(r.text, r.url),
                syntaxes=SYNTAXES,
                uniform=True,
            )

        for syntax in SYNTAXES:
            for item in data.get(syntax, []):
                if (
                    "@context" in item and
                    item["@context"] == SCHEMA_ORG_HOST and
                    "@type" in item and
                    item["@type"].lower() == SCHEMA_NAME.lower()
                ):
                    self.format = syntax
                    self.data = item
                    return

    def host(self):
        return SCHEMA_ORG_HOST

    def title(self):
        return self.data.get("name")

    def total_time(self):
        iso_cook_time = self.data.get("cookTime")
        iso_prep_time = self.data.get("prepTime")
        if not iso_prep_time and not iso_cook_time:
            return None

        total = 0
        if iso_prep_time:
            total += isodate.parse_duration(iso_prep_time).total_seconds * 60
        if iso_cook_time:
            total += isodate.parse_duration(iso_cook_time).total_seconds * 60
        return total

    def yields(self):
        return self.data.get("recipeYield")

    def image(self):
        return self.data.get("image")

    def ingredients(self):
        return self.data.get("recipeIngredient")

    def instructions(self):
        return self.data.get("recipeInstructions")

    def ratings(self):
        return self.data.get("aggregateRating")
