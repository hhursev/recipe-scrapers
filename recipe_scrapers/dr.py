from ._abstract import AbstractScraper
from ._utils import normalize_string


class Dr(AbstractScraper):
    @classmethod
    def host(cls):
        return "dr.dk"

    def title(self):
        title_span = self.soup.find("span", {"class": "dre-title-text"})
        return title_span.get_text() if title_span else None

    def author(self):
        author_div = self.soup.find(
            "div", {"class": "dre-byline__contribution-details"}
        )
        author_span = (
            author_div.find("span", {"itemprop": "name"}) if author_div else None
        )
        return author_span.get_text() if author_span else None

    def ingredients(self):
        ingredients_divs = self.soup.findAll("div", {"class": "dre-list dre-variables"})
        ingredients_list = []

        for div in ingredients_divs:
            ul = div.find("ul", {"class": "dre-list__list"})
            lis = ul.findAll("li", {"class": "dre-list-item"})

            for li in lis:
                span = li.find("span", {"class": "dre-list-item__content"})
                if span:
                    p = span.find("p")
                    if p:
                        ingredients_list.append(normalize_string(p.get_text()))

        return ingredients_list

    def instructions(self):
        fremgangsmade_div = self.soup.find("div", string="Fremgangsmåde")
        if fremgangsmade_div:
            parent_section = fremgangsmade_div.find_parent("section")
            if parent_section:
                instructions_list = []
                instructions_divs = parent_section.findAll(
                    "div", {"class": "dre-speech"}
                )
                for div in instructions_divs:
                    p = div.find("p", {"class": "dre-article-body-paragraph"})
                    if p:
                        instructions_list.append(normalize_string(p.get_text()))
                return "\n".join(instructions_list)
