# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._exceptions import SchemaOrgException


class SallysBakingAddiction(AbstractScraper):
    @classmethod
    def host(cls):
        return "sallysbakingaddiction.com"

    def title(self):
        return self.schema.title()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()

    def prep_time(self):
        return self.schema.prep_time()

    def cook_time(self):
        return self.schema.cook_time()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        image = self.data.get("image")

        if image is None:
            raise SchemaOrgException("Image not found in SchemaOrg")

        if isinstance(image, list):
            image = image[-1]

        if isinstance(image, dict):
            image = image.get("url")

        if "http://" not in image and "https://" not in image:
            image = ""

        return image

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()
