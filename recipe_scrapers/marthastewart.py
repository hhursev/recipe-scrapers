# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class MarthaStewart(AbstractScraper):
    @classmethod
    def host(cls):
        return "marthastewart.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return (
            self.soup.findAll("div", {"class": "two-subcol-content-wrapper"})[1]
            .find("div", {"class": "recipe-meta-item-body"})
            .text.strip()
        )

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()
