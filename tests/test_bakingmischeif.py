from recipe_scrapers.bakingmischeif import BakingMischeif
from tests import ScraperTest


class TestBakingMischeifScraper(ScraperTest):

    scraper_class = BakingMischeif

    def test_host(self):
        self.assertEqual("bakingmischief.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Tracy", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Barbacoa Burrito Bowls", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(190, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://bakingmischief.com/wp-content/uploads/2020/12/barbacoa-burrito-bowls-image-square-2.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 boneless 2-3 pound chuck roast ( trimmed and cut into fist-size chunks)",
                "Salt and pepper",
                "1 medium white or yellow onion diced",
                "3 tablespoons vegetable oil",
                "1-6 cups beef or chicken broth",
                "1/4 cup lime juice",
                "1/4 cup apple cider vinegar",
                "2 chipotle peppers in adobo sauce minced (optional)",
                "1 tablespoon ground cumin",
                "1 tablespoon dried oregano",
                "1/4 teaspoon ground cloves optional",
                "3/4 teaspoon salt",
                "3 bay leaves",
                "Juice from 1 lime (about 2 tablespoons)",
                "Scant 2 cups chicken broth",
                "1 cup long-grain rice",
                "Zest from 1 lime (divided)",
                "1 tablespoon (14g) butter (salted or unsalted is fine)",
                "1/4 teaspoon salt",
                "1/4 cup chopped loosely packed cilantro (divided)",
                "1 15-ounce can black beans (rinsed, drained, and warmed)",
                "1 15- 15-ounce can corn (drained and warmed)",
                "1/2 cup (2oz) shredded Mexican-blend cheese",
                "1 cup pico de gallo",
                "1/2 cup guacamole",
                "1/4 cup sour cream",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Barbacoa\nGenerously salt and pepper meat on all sides.\nIn a large dutch oven (or skillet if you’ll be using a slow cooker), heat oil over medium-high heat. Brown meat on all sides, in batches if necessary. This may take up to 15 minutes.\nStovetop Barbacoa\nAdd onion and just enough chicken or beef broth to mostly submerge the meat. Stir, scraping the bottom of the pan to remove any stuck-on bits. Stir in remaining ingredients and bring mixture to a low simmer. Cook, stirring occasionally for 2 1/2 to 3 hours, until meat is very tender and can be pulled apart with a fork.\nSlow Cooker Barbacoa\nIf using a slow cooker, transfer meat and any drippings remaining in the pan to the slow cooker and add onions, 1 cup of broth and remaining ingredients. Cook on high for 3 to 4 hours, low for 7 to 8 hours, until the beef is tender and can be easily shredded with a fork.\nShred\nOnce meat is done, use a slotted spoon to transfer the pieces to a cutting board. Use two forks to shred the meat, discarding any large pieces of fat as you go.\nReturn shredded meat to the cooking liquid. Add more salt and pepper to taste.\nCilantro Lime Rice\nAdd lime juice to a 2-cup measuring cup. Fill the measuring cup the rest of the way with chicken broth.\nIn a saucepan or rice cooker, cook rice according to package instructions, replacing the water with the lime juice/chicken broth mixture and adding butter and salt when you add the rice (if the package instructions already call for salt, do not add additional salt).\nAfter rice has finished cooking, stir in half of the lime zest and cilantro. Taste and add more lime and cilantro to taste.\nBurrito Bowls\nDivide cilantro rice between bowls or food prep containers. Top rice with shredded barbacoa and the rest of your burrito bowl toppings. Serve and enjoy.",
            self.harvester_class.instructions(),
        )
