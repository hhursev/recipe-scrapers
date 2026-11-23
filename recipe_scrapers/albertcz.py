import re

import requests

from ._abstract import AbstractScraper

GRAPHQL_ENDPOINT = "https://www.albert.cz/api/v1/"
GRAPHQL_QUERY = "query getRecipe($code:String! $lang:String!) { getRecipe(code:$code lang:$lang) { recipeCookingSteps { description stepNumber } } }"


class AlbertCz(AbstractScraper):
    @classmethod
    def host(cls):
        return "albert.cz"

    def author(self):
        return "Albert"

    def site_name(self):
        return "Albert"

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
        return self.schema.ingredients()

    def instructions(self):
        schema_instructions = self.schema.instructions()
        if schema_instructions:
            filtered = [
                line
                for line in schema_instructions.split("\n")
                if not line.strip().endswith(".") or not line.strip()[:-1].isdigit()
            ]
            return "\n".join(filtered)

        # albert.cz serves empty recipeInstructions in JSON-LD; fetch via GraphQL
        match = re.search(r"/r/([A-Za-z0-9]+)(?:[/?#]|$)", self.canonical_url())
        if not match:
            return ""

        code = match.group(1)
        try:
            response = requests.post(
                GRAPHQL_ENDPOINT,
                json={
                    "operationName": "getRecipe",
                    "variables": {"code": code, "lang": "cs"},
                    "query": GRAPHQL_QUERY,
                },
                headers={
                    "Content-Type": "application/json",
                    "Origin": "https://www.albert.cz",
                    "Referer": "https://www.albert.cz/",
                },
                timeout=10,
            )
            steps = sorted(
                response.json()["data"]["getRecipe"]["recipeCookingSteps"],
                key=lambda s: s["stepNumber"],
            )
            return "\n".join(step["description"] for step in steps)
        except Exception:
            return ""

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        meta = self.soup.find("meta", {"name": "description"})
        if meta:
            return meta.get("content")
        return self.schema.description()
