from .aldinord import AldiNord


class AldiEs(AldiNord):
    @classmethod
    def host(cls, domain: str = "aldi.es"):
        return domain
