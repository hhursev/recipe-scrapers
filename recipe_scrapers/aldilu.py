from .aldinord import AldiNord


class AldiLu(AldiNord):
    @classmethod
    def host(cls, domain: str = "aldi.lu"):
        return domain
