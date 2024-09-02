from ._abstract import AbstractScraper


class ProjectGezond(AbstractScraper):
    @classmethod
    def host(cls):
        return "projectgezond.nl"

    def author(self):
        return "Project Gezond"
