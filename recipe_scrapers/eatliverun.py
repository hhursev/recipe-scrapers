from ._abstract import AbstractScraper


class EatLiveRun(AbstractScraper):
    @classmethod
    def host(cls):
        return "eatliverun.com"

    def site_name(self):
        return "Eat, Live, Run"
