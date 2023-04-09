# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class EatingWell(AbstractScraper):
    @classmethod
    def host(cls):
        return "eatingwell.com"

    def title(self):
        return self.schema.title()

    def author(self):
        return self.schema.author()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def total_time(self):
        # Old Implementation, new Implementation based on schema below
        # d = {
        #
        # }
        # divlist = self.soup.findAll("div", {"class": "mntl-recipe-details__item"})
        #
        ## For every element that matches mntl-recipe-details__item class
        # for element in divlist:
        #    # Find the child that contains "Value" (this is what we care about for number of minutes)
        #    val = element.findChildren("div", {"class": "mntl-recipe-details__value"})
        #    # If the value contains the text "mins", it is either total_time or active_time
        #    if ("mins" in val[0].text):
        #        # Set the dict to this value and return it after the loop ends
        #        d["total"] = val[0].text
        #
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()
