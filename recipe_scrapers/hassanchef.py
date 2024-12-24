from ._abstract import AbstractScraper


class HassanChef(AbstractScraper):
    @classmethod
    def host(cls):
        return "hassanchef.com"

    def author(self):
        return self.schema.author().title()
