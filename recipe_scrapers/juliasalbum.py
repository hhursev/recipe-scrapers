from ._abstract import AbstractScraper


class JuliasAlbum(AbstractScraper):
    @classmethod
    def host(cls):
        return "juliasalbum.com"
