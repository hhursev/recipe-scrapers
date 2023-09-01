# mypy: allow-untyped-defs

from recipe_scrapers.omnivorescookbook import OmnivoresCookbook
from tests import ScraperTest


class TestOmnivoresCookbookScraper(ScraperTest):
    scraper_class = OmnivoresCookbook
    test_file_name = "omnivorescookbook_2"

    def test_host(self):
        self.assertEqual("omnivorescookbook.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Maggie Zhu", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Beef Pan-Fried Noodles", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Main", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://omnivorescookbook.com/wp-content/uploads/2020/06/200430_Beef-Pan-Fried-Noodles_550.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "8 oz (225 g) flank steak (or skirt steak) , thinly sliced against the grain",
                "8 oz (225 g) fresh Hong Kong pan fry noodles (or other type of thin noodles) (Footnote 1)",
                "2 tablespoons Shaoxing wine (or dry sherry)",
                "2 teaspoons cornstarch",
                "1/4 teaspoon salt",
                "1 cup low-sodium beef broth",
                "2 tablespoons soy sauce (*Footnote 2)",
                "2 tablespoons oyster sauce",
                "1 tablespoon Shaoxing wine (or dry sherry)",
                "2 tablespoons cornstarch",
                "1 teaspoon sugar",
                "1/4 teaspoon Chinkiang vinegar",
                "1/4 teaspoon white pepper",
                "4 tablespoons peanut oil , divided",
                "4 heads baby bok choy , quartered",
                "4 cloves garlic , minced",
                "1 inch (2.5 cm) ginger , minced",
                "1/2 yellow onion , sliced",
                "1/2 carrot , sliced into strips",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Combine the beef and the marinade ingredients in a medium-sized bowl. Toss with your hands to coat the "
            "beef evenly and let marinate while preparing other ingredients.\n"
            "Combine the sauce ingredients in a medium-sized bowl and stir to mix thoroughly.\n"
            "Prepare the noodles according to package directions (*Footnote 3). Drain and set aside in a colander to "
            "dry.\n"
            "Heat a large heavy-bottomed pan (nonstick or carbon steel) with 2 tablespoons of peanut oil over "
            "medium-high heat until hot. Spread the noodles into a patty shape (*Footnote 4). Cook without flipping "
            "until the bottoms turn golden. Turn the noodles to fry the other side until golden. Drizzle in a bit "
            "more oil to help with the frying, if needed. Once done, transfer the noodles to a big serving plate.\n"
            "Pour 1 tablespoon of oil into the same pan. Add the beef and spread it out in a single layer using a "
            "pair of tongs or chopsticks. Let cook undisturbed for 30 seconds or so, or until the bottom turns golden "
            "brown. Flip to cook the other side until browned. Stir a few times until the beef is cooked (it’s OK if "
            "there’s a hint of pink inside), transfer to a big plate, and set aside.\n"
            "Add the remaining 1 tablespoon of oil to the pan. Add the onion and carrots. Quickly stir a few times to "
            "mix well. Add the ginger and garlic. Stir and cook for 30 seconds to release the fragrance.\n"
            "Add the bok choy. Cook and stir for another minute, until the veggies start to soften.\n"
            "Stir the sauce thoroughly to dissolve the cornstarch completely and pour the sauce into the pan. Stir "
            "and cook to bring the sauce to a boil, and cook until it starts to thicken.\n"
            "Add the cooked beef back into the pan. Stir to mix everything well. Once the sauce reaches the desired "
            "consistency, pour everything over the fried noodles. (*Footnote 5)\n"
            "Serve immediately as a main dish.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.81, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Chinese", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Turn your kitchen into a Chinese restaurant by making crispy pan fried noodles with juicy beef in a rich "
            "and savory sauce that tastes too good to be true!",
            self.harvester_class.description(),
        )
