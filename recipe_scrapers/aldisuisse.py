from .aldisued import AldiSued


class AldiSuisse(AldiSued):
    @classmethod
    def host(cls, domain="aldi-suisse.ch"):
        return domain
