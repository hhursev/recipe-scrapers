from ._abstract import AbstractScraper


class StaySnatched(AbstractScraper):
    @classmethod
    def host(cls):
        return "staysnatched.com"

    def author(self):
        author_element = self.soup.find(
            "div",
            {
                "class": "wprm-recipe-block-container wprm-recipe-block-container-columns wprm-block-text-normal wprm-recipe-author-container"
            },
        )
        return author_element.find("a").get_text() if author_element else "Unknown"
