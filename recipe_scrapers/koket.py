import json

import regex as re

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
        jsData = re.search(
            r'(?<=<script id="__NEXT_DATA__" type="application\/json">)(.*?)(?=<\/script>)',
            str(self.soup),
        )
        data = json.loads(jsData.group(0))
        return data["props"]["pageProps"]["item"]["cooking_steps"]

    def ratings(self):
        jsData = re.search(
            r'(?<=<script id="__NEXT_DATA__" type="application\/json">)(.*?)(?=<\/script>)',
            str(self.soup),
        )
        data = json.loads(jsData.group(0))
        data = data["props"]["pageProps"]["item"]
        return [data["rating_value"], data["rating_count"]]
