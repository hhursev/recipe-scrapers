from .mob import Mob


class MobKitchen(Mob):
    @classmethod
    def host(cls):
        return "mobkitchen.co.uk"
