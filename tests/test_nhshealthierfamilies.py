from recipe_scrapers.nhshealthierfamilies import NHSHealthierFamilies
from tests import ScraperTest


class TestNHSHealthierFamiliesScraper(ScraperTest):

    scraper_class = NHSHealthierFamilies

    def test_host(self):
        self.assertEqual("nhs.uk", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("NHS Better Health", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Chilli con carne", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://assets.nhs.uk/campaigns-cms-prod/images/Chilli-con-carne_x7m8d91.width-320.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "300g extra-lean minced beef",
                "1 large onion, finely chopped",
                "2 garlic cloves, finely chopped",
                "400g chopped tomatoes",
                "2 tablespoons tomato purée",
                "2 teaspoons chilli powder",
                "1 teaspoon ground cumin",
                "1 red pepper, deseeded and chopped",
                "2 handfuls of cup or button mushrooms, sliced",
                "410g red kidney beans, drained",
                "150ml reduced-salt vegetable or chicken stock",
                "300g easy-cook white or brown rice",
                "1 pinch ground black pepper",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "Heat a large saucepan and add the minced beef, a handful at a time, cooking it until browned. Add the onion and garlic, then cook for another 2 to 3 minutes.",
                    "Add the chopped tomatoes, tomato purée, spices, red pepper, mushrooms, kidney beans and stock. Stir well, bring to the boil, then lower the heat and simmer gently for 15 to 20 minutes.",
                    "Meanwhile, cook the rice according to pack instructions.",
                    "Season the chilli with pepper and serve with the boiled rice.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            "This classic chilli is packed with flavour. It also freezes well, so is perfect for batch-cooking.",
            self.harvester_class.description(),
        )
