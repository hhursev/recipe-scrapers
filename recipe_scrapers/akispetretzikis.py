import json

from ._abstract import AbstractScraper


class AkisPetretzikis(AbstractScraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.recipe_json = json.loads(
            self.soup.find("script", {"id": "__NEXT_DATA__"}).get_text()
        )

    @classmethod
    def host(cls):
        return "akispetretzikis.com"

    def language(self):
        return self.recipe_json["locale"]
