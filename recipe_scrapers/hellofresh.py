# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class HelloFresh(AbstractScraper):
    @classmethod
    def host(self, domain="com"):
        return f"hellofresh.{domain}"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ingredients(self):
        if not self._serving_one_on_page():
            return self.schema.ingredients()
        else:
            return [f"2 * {ingredient}" for ingredient in self.schema.ingredients()]

    def instructions(self):
        return self.schema.instructions()

    def image(self):
        return self.schema.image()

    def nutrients(self):
        return self.schema.nutrients()

    def cuisine(self):
        return self.schema.cuisine()

    def category(self):
        return self.schema.category()

    def _serving_one_on_page(self):
        # ad-hoc solution for https://github.com/hhursev/recipe-scrapers/issues/527
        try:
            return (
                self.soup.find("div", {"data-test-id": "serving-amount-container"})
                .find("div", {"class": "fela-_txm046"})
                .select("div[class*=ds]")[0]
                .get_text()
                == "1"
            )
        except (AttributeError, IndexError):
            # AttributeError if .find(..) method errored
            # IndexError if the .select(..)[0] did not work as expected
            # both cases to fall back to default behaviour
            return True
