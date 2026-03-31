from ._abstract import AbstractScraper


class TheRecipeCritic(AbstractScraper):
    @classmethod
    def host(cls):
        return "therecipecritic.com"

    def author(self):
        return "The Recipe Critic"
