# mypy: allow-untyped-defs
from .americastestkitchen import AmericasTestKitchen


class CooksIllustrated(AmericasTestKitchen):

    @classmethod
    def host(cls):
        return "cooksillustrated.com"
