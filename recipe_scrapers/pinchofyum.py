from ._abstract import AbstractScraper


class PinchOfYum(AbstractScraper):
    @classmethod
    def host(cls):
        return "pinchofyum.com"
