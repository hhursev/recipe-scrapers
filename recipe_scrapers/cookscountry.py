# mypy: allow-untyped-defs
from .americastestkitchen import AmericasTestKitchen


class CooksCountry(AmericasTestKitchen):

    @classmethod
    def host(cls):
        return "cookscountry.com"
