from ._exceptions import StaticValueException
from .americastestkitchen import AmericasTestKitchen


class CooksCountry(AmericasTestKitchen):

    @classmethod
    def host(cls):
        return "cookscountry.com"

    def site_name(self):
        raise StaticValueException(return_value="Cook's Country")
