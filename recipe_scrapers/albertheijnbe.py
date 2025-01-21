from .albertheijn import AlbertHeijn


class AlbertHeijnBe(AlbertHeijn):
    @classmethod
    def host(cls):
        return "ah.be"
