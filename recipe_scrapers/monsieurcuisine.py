from ._abstract import AbstractScraper


class MonsieurCuisine(AbstractScraper):
    @classmethod
    def host(cls):
        return "monsieur-cuisine.com"

    def author(self):
        return self.soup.find("span", {"class": "primary--text font-weight-bold ml-1"}).get_text().strip()

    def title(self):
        return self.soup.find('h1').get_text()

    def category(self):
        return self.schema.category()

    def total_time(self):
        container = self.soup.find("div", {"class": "duration-information"}).find(
            "div", {"class": "recipe-duration-total"}
        )

        total_time = container.b.get_text()
        total_time_hours = total_time.split(":")[0]
        total_time_mins = total_time.split(":")[1]

        return total_time_mins + 60 * total_time_hours

    def yields(self):
        container = self.soup.find("div", {"class": "recipe--info"}).find(
            "div", {"class": "recipe-portions"}
        )

        return container.get_text()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        container = self.soup.find(
            "div", {"class": "recipe--ingredients-html-item col-md-8"}
        )

        ingredients = container.findAll("li")
        return ingredients

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
