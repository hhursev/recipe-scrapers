# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class PinchOfYum(AbstractScraper):
    @classmethod
    def host(cls):
        return "pinchofyum.com"


    def description(self):
        return self.schema.description()
