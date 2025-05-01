from ._abstract import AbstractScraper


class HealthyWithAChanceOfSprinkles(AbstractScraper):
    @classmethod
    def host(cls):
        return "healthywithachanceofsprinkles.com"
