from ._exceptions import StaticValueException
from .americastestkitchen import AmericasTestKitchen


class CooksIllustrated(AmericasTestKitchen):

    @classmethod
    def host(cls):
        return "cooksillustrated.com"

    def site_name(self):
        raise StaticValueException(return_value="Cook's Illustrated")
