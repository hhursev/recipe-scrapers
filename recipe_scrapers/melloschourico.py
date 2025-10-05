from ._abstract import AbstractScraper
from ._exceptions import FieldNotProvidedByWebsiteException
from ._utils import normalize_string


class MellosChourico(AbstractScraper):
    @classmethod
    def host(cls):
        return "melloschourico.com"

    def author(self):
        name_meta = self.soup.find("meta", itemprop="author")
        return normalize_string(name_meta["content"])

    def title(self):
        return normalize_string(self.soup.find("h1", class_="BlogItem-title").text)

    def _extract_information_blocks(self, keyword):
        content_blocks = self.soup.find_all("div", class_="sqs-html-content")
        keyword_upper = keyword.upper()

        for block in content_blocks:
            heading = block.find(
                lambda tag: tag.name in ["h1", "h2"]
                and keyword_upper in (tag.get_text() or "").upper()
            )
            if heading:
                for tag_name in ["ul", "ol"]:
                    list_tag = heading.find_next(tag_name)
                    if list_tag:
                        return [
                            normalize_string(li.get_text())
                            for li in list_tag.find_all("li")
                        ]

        return []

    def ingredients(self):
        return self._extract_information_blocks("INGREDIENTS")

    def instructions(self):
        steps = self._extract_information_blocks("INSTRUCTIONS")
        return "\n".join(steps)

    def yields(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def total_time(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)
