from ._abstract import AbstractScraper


class FranzoesischKochen(AbstractScraper):
    @classmethod
    def host(cls):
        return "franzoesischkochen.de"

    def author(self):
        # TODO: check to see whether the pages begin using 'name' (lowercase initial)
        # if they do, then we can use self.schema.author() instead here
        return self.schema.data.get("author").get("Name")

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        # TODO: can recipe yields / servings be retrieved from these pages?
        return None

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()
