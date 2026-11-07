from ._abstract import AbstractScraper


class ExperimenteAusMeinerKueche(AbstractScraper):
    @classmethod
    def host(cls):
        return "experimenteausmeinerkueche.de"
