from ._abstract import AbstractScraper
from ._utils import normalize_string


class Picnic(AbstractScraper):
    @classmethod
    def host(cls):
        return "picnic.app"

    def instructions(self):
        # Picnic names the steps "Schritt 1" ("step 1") and the current verison of
        # instructions() add the name and the text as separate steps.
        # That's why we extract the steps here manually to skip this.
        new_instructions = []
        for instruction in self.schema.data.get("recipeInstructions"):
            new_instructions.append(instruction["text"])
        return "\n".join(
            normalize_string(instruction) for instruction in new_instructions
        )

    def site_name(self):
        # Picnic recipes have the site name as author and mentioned nowhere else alone
        # That's why we return author here
        return self.author()

    def canonical_url(self):
        # Picnic "hides" the canonical recipe URL in the instructions, so we grab it from there
        # As it's only relative to the root, we have to combine it with https:// and the host.
        instructions = self.schema.data.get("recipeInstructions")
        return "https://{}{}".format(self.host(), instructions[0]["url"])

    def language(self):
        # The recipe's language is encoded in the URL, directly after the host name
        # e.g. https://picnic.app/de/ or https://picnic.app/en/
        return self.canonical_url()[19:21]
