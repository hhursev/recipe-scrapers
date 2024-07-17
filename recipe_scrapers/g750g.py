from ._abstract import AbstractScraper


class G750g(AbstractScraper):
    @classmethod
    def host(cls):
        return "750g.com"

    def site_name(self):
        return self.opengraph.site_name()
