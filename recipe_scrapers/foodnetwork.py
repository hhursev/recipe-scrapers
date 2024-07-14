from ._abstract import AbstractScraper


class FoodNetwork(AbstractScraper):
    @classmethod
    def host(cls, domain="co.uk"):
        return f"foodnetwork.{domain}"

    def author(self):
        return self.schema.data.get("copyrightNotice") or self.schema.author()

    def site_name(self):
        return self.schema.author()
