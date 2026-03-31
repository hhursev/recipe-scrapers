from .aldisued import AldiSued


class Hofer(AldiSued):
    @classmethod
    def host(cls, domain="hofer.at"):
        return domain
