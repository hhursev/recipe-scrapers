# mypy: allow-untyped-defs
import re

from ._abstract import AbstractScraper


class ProjectGezond(AbstractScraper):
    @classmethod
    def host(cls):
        return "projectgezond.nl"

    def author(self):
        return "Project Gezond"

    def title(self):
        return self.soup.find("h1", {"class": "entry-title"}).text

    def category(self):
        return ", ".join(
            [
                element.text
                for element in self.soup.find(
                    "span", {"class": "meta-category"}
                ).find_all(
                    "a", {"class": lambda x: x is not None and x.startswith("category")}
                )
            ]
        )

    def total_time(self):
        time_element = self.soup.find("em", string="Bereidingstijd:").parent
        return "".join(
            [
                element.text
                for element in time_element.children
                if element.text != "Bereidingstijd:"
            ]
        ).strip()

    def yields(self):
        # Match everything in the h2 with 'Dit heb je nodig'
        # The text inside the parentheses contains the yield for the ingredients that are listed
        return re.search(
            r"Dit heb je nodig \(([^)]+)",
            self.soup.find(
                "h2", string=lambda x: x.startswith("Dit heb je nodig")
            ).text,
        ).group(1)

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients_table = self.soup.find(
            "h2", string=lambda x: x.startswith("Dit heb je nodig")
        ).next_sibling.next_sibling
        ingredients = [
            ingredient.text
            for ingredient in ingredients_table
            if ingredient.text.strip()
        ]
        return ingredients

    def instructions(self):
        instructions_table = self.soup.find(
            "h2", string=lambda x: x.startswith("Zo maak je het")
        ).next_sibling.next_sibling.next_sibling.next_sibling
        instructions = [
            instruction.text
            for instruction in instructions_table
            if instruction.text.strip()
        ]
        return "\n".join(instructions).strip()

    def ratings(self):
        # Ratings do not exist on this site
        return None

    def cuisine(self):
        # Not listed on site
        return None

    def description(self):
        # Get the recipe's content start. The recipe will start with the description until
        # we reach the instructions.
        content_start = self.soup.find("div", {"class", "entry-content"})

        description = ""
        for content_element in content_start.children:
            # If we reach this, the ingredients are listed and the description is complete
            if content_element.text.startswith("Dit heb je nodig"):
                break

            description += content_element.text

        return description.strip()
