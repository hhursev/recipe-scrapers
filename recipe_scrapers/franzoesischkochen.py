from ._abstract import AbstractScraper


class FranzoesischKochen(AbstractScraper):
    @classmethod
    def host(cls):
        return "franzoesischkochen.de"

    def author(self):
        # TODO: check to see whether the pages begin using 'name' (lowercase initial)
        # if they do, then we can use self.schema.author() instead here
        return self.schema.data.get("author").get("Name")

    def yields(self):
        # TODO: can recipe yields / servings be retrieved from these pages?
        return None
