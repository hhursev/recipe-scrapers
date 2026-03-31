from ._abstract import AbstractScraper


class Mob(AbstractScraper):
    @classmethod
    def host(cls):
        return "mob.co.uk"

    def author(self):
        author_tag = self.soup.select_one("div.RecipeHero__detailsContainer h3")
        return author_tag.get_text(strip=True)
