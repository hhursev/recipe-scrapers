import re

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields


class Panelinha(AbstractScraper):
    @classmethod
    def host(cls):
        return "panelinha.com.br"

    def yields(self):
        main_element = self.soup.find("main")
        yield_text = main_element.get("data-item-p-yield")
        yield_number = re.search(r"\d+", yield_text)
        if yield_number:
            return get_yields(yield_number.group())

    def total_time(self):
        tempo_de_preparo = (
            self.soup.find("dt", string="Tempo de preparo").find_next(name="dd").text
        )
        return get_minutes(tempo_de_preparo)
