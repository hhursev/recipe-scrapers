from ._abstract import AbstractScraper


class Coop(AbstractScraper):
    @classmethod
    def host(cls):
        return "coop.se"

    def author(self):
        author = self.schema.author()
        if author is None:
            author = self.schema.data.get("Author")
            if (
                author
                and isinstance(author, list)
                and len(author) >= 1
                and isinstance(author[0], dict)
            ):
                author = author[0]
            if author and isinstance(author, dict):
                author = author.get("name")
        return author

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def cook_time(self):
        return self.schema.cook_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        image = self.schema.image()
        if image is None or image == '':
            image = self.schema.data.get("image")
            if (
                image
                and isinstance(image, list)
                and len(image) >= 1
                and isinstance(image[0], str)
                and image[0].startswith("//")
            ):
                image = "https:" + image[0]
        return image

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
