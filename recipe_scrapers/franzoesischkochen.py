from ._abstract import AbstractScraper


class FranzoesischKochen(AbstractScraper):
    @classmethod
    def host(cls):
        return "franzoesischkochen.de"

    def author(self):
        return self.soup.find("meta", {"name": "author"}).get("content")

    def yields(self):
        # TODO: can recipe yields / servings be retrieved from these pages?
        return None

    def instructions(self):
        instructions = self.schema.instructions()
        filtered_instructions = "\n".join(
            line for line in instructions.split("\n") if not line.startswith("Schritt")
        )
        return filtered_instructions
