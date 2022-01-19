import json
import re

from ._abstract import AbstractScraper


class Koket(AbstractScraper):
    @classmethod
    def host(cls):
        return "koket.se"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        jsData = re.search(
            r'(?<=<script id="__NEXT_DATA__" type="application\/json">)(.*?)(?=<\/script>)',
            str(self.soup),
        )
        data = json.loads(jsData.group(0))
        return data["props"]["pageProps"]["item"]["ingredients"]

    def instructions(self):
        instructions = []
        for instruction in self.soup.find("section", {"id": "step-by-step"}).find_all(
            "span"
        ):
            try:
                header = instruction.find("b")
                instructions.append({"type": "header", "name": header.get_text()})
                instructions.append(
                    {"type": "instruction", "name": header.next_sibling.next_sibling}
                )
            except AttributeError:
                instructions.append(
                    {"type": "instruction", "name": instruction.get_text()}
                )
        return instructions

    def ratings(self):
        jsData = re.search(
            r'(?<=<script id="__NEXT_DATA__" type="application\/json">)(.*?)(?=<\/script>)',
            str(self.soup),
        )
        data = json.loads(jsData.group(0))
        data = data["props"]["pageProps"]["item"]
        return {
            "rating_value": data["rating_value"],
            "rating_count": data["rating_count"],
        }
