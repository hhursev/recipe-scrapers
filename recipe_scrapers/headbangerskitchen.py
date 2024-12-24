from ._abstract import AbstractScraper


class HeadbangersKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "headbangerskitchen.com"

    def site_name(self):
        return self.opengraph.site_name()
