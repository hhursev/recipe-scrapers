from ._abstract import AbstractScraper


class Therecipecritic(AbstractScraper):
    @classmethod
    def host(cls):
        return "therecipecritic.com"

    def author(self):
        return "The Recipe Critic"
