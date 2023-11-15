# mypy: disallow_untyped_defs=False

from ._abstract import AbstractScraper
from ._utils import normalize_string


class Reishunger(AbstractScraper):
    @classmethod
    def host(cls):
        return "reishunger.de"

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
        return self.schema.ingredients()

    def instructions(self):
        # find the "instructions" heading (Zubereitung in German)
        for heading in self.soup.findAll("h3"):
            if "Zubereitung" in heading.get_text():
                break

        results = []

        # locate the first recipe instruction
        step1 = heading.parent.parent.find("div", {"class": "leading-normal"})

        # iterate through each step in the recipe
        for step in step1.next_siblings:
            # check whether the instruction has a list of preparations
            # fixme: this can throw an exception if 'step' is not a bs4 Tag
            try:
                preparations = step.find("div", {"preparation": True})
            except Exception:
                preparations = None

            # if it does, add every preparation step as an instruction entry
            if preparations:
                for preparation in preparations.findAll("div", {"id": True}):
                    instruction = normalize_string(preparation.text)
                    results.append(instruction)

            # otherwise, add only one instruction entry
            else:
                if step.find("p"):
                    instruction = normalize_string(step.text)
                    results.append(instruction)

            # continue on to the next instruction
            step = step.next_sibling

        # filter out empty lines
        results = [instruction for instruction in results if instruction]
        return "\n".join(results)

    def ratings(self):
        return self.schema.ratings()
