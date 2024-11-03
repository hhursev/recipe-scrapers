from .aldisued import AldiSued


class AldiSuisse(AldiSued):
    @classmethod
    def host(cls):
        return "aldi-suisse.ch"
