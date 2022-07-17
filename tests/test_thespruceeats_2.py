from recipe_scrapers.thespruceeats import TheSpruceEats
from tests import ScraperTest


class TestTheSpruceEatsScraper(ScraperTest):

    scraper_class = TheSpruceEats

    @property
    def test_file_name(self):
        return "{}_2".format(self.scraper_class.__name__.lower())

    def test_host(self):
        self.assertEqual("thespruceeats.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.thespruceeats.com/creamy-potato-soup-with-ham-3059797",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Creamy Potato Soup With Ham")

    def test_total_time(self):
        self.assertEqual(55, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.thespruceeats.com/thmb/cRHLNY5mOubzxULIsfs4qE5aBsU=/960x0/filters:no_upscale():max_bytes(150000):strip_icc()/creamy-potato-soup-with-ham-3059797-stovetop-step-12-99dc3bf1962c4e26a2d225ee3c25ecad.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 tablespoons butter",
                "1 1/2 to 2 cups onion (chopped)",
                "1 cup celery (chopped)",
                "2 large carrots (peeled and chopped)",
                "2 to 3 cups ham (about 1 pound, diced)",
                "1 clove garlic (minced)",
                "2 cups vegetable broth",
                "1 cup water",
                "4 to 5 cups potatoes (peeled and diced)",
                "3 tablespoons all-purpose flour",
                "1 cup heavy cream",
                "1 cup half-and-half (or whole milk, more if needed to thin)",
                "Dash salt (to taste)",
                "Dash freshly ground black pepper (to taste)",
                "Optional: 2 tablespoons fresh parsley (chopped)",
                "Garnish: green onions or chives (sliced)",
                "Optional: cheddar cheese or cheddar-jack blend (shredded)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions_list(self):
        return self.assertEqual(
            [
                "Gather the ingredients.",
                "In a large saucepan, melt butter over medium-low heat.",
                "Add onion, celery, carrots, and ham.",
                "Cook, stirring frequently until onions are tender, about 5 minutes.",
                "Add the garlic and continue cooking for 1 to 2 minutes longer.",
                "Add vegetable broth, water, and potatoes.",
                "Cover and cook for about 25 minutes, until potatoes are tender.",
                "Whisk flour into the heavy cream until smooth.",
                "Stir into the hot mixture.",
                "Stir in the half-and-half or milk. Taste and add salt and pepper, as desired. Continue cooking until hot.",
                "Using a potato masher or fork, mash the potatoes slightly to thicken; add more milk if the soup is too thick.",
                "Serve the potato soup garnished with parsley, sliced green onions or chives, or a little bit of shredded cheese.",
                "Gather the ingredients.",
                "In a large saucepan, melt butter over medium-low heat.",
                "Add onion, celery, carrots, and ham.",
                "Cook, stirring frequently until onions are tender, about 5 minutes.",
                "Add the garlic and continue cooking for 1 to 2 minutes longer.",
                "Then transfer the cooked vegetables to the slow cooker and add the broth, water, and potatoes.",
                "Cover and cook on HIGH for about 2 to 3 hours, or until the potatoes are very tender.",
                "Whisk flour into the heavy cream until smooth.",
                "Stir the flour-cream mixture into the slow cooker.",
                "Stir in the half-and-half or milk. Taste and add salt and pepper, as desired. Continue cooking until hot.",
                "Using a potato masher or fork, mash the potatoes slightly to thicken; add more milk if the soup is too thick.",
                "Serve the potato soup garnished with parsley, sliced green onions or chives, or a little bit of shredded cheese.",
            ],
            self.harvester_class.instructions_list(),
        )
