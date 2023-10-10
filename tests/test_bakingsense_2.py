from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.bakingsense import BakingSense
from tests import ScraperTest


class TestBakingSense(ScraperTest):

    scraper_class = BakingSense
    test_file_name = "bakingsense_2"

    def test_host(self):
        self.assertEqual("baking-sense.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.baking-sense.com/2022/04/14/chocolate-cake-with-strawberry-mousse-filling/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Eileen Gray", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Chocolate Cake with Strawberry Mousse Recipe", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Dessert", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(250, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("12 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.baking-sense.com/wp-content/uploads/2022/04/choc-sberry-cake-featured.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            '1 recipe Chocolate Chiffon Cake (baked in two 9" pans)',
            "2 oz freeze dried strawberries (3 cups before grinding)",
            "24 oz fresh strawberries ( hulled and chopped)",
            "5 1/4 oz granulated sugar (2/3 cup, divided)",
            "2 tablespoon orange liquor (or use water)",
            "2 teaspoons unflavored gelatin powder",
            "8 oz heavy cream (1 cup)",
            "1 recipe Swiss Meringue Buttercream (or your favorite buttercream)",
            "12 strawberries (can be dipped in chocolate)",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        '1 recipe Chocolate Chiffon Cake (baked in two 9" pans)',
                        "2 oz freeze dried strawberries (3 cups before grinding)",
                    ],
                    purpose=None,
                ),
                IngredientGroup(
                    ingredients=[
                        "24 oz fresh strawberries ( hulled and chopped)",
                        "5 1/4 oz granulated sugar (2/3 cup, divided)",
                        "2 tablespoon orange liquor (or use water)",
                        "2 teaspoons unflavored gelatin powder",
                        "8 oz heavy cream (1 cup)",
                    ],
                    purpose="Strawberry Mousse",
                ),
                IngredientGroup(
                    ingredients=[
                        "1 recipe Swiss Meringue Buttercream (or your favorite buttercream)",
                        "12 strawberries (can be dipped in chocolate)",
                    ],
                    purpose="Assembly",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        expected_instructions = (
            "Split each cake horizontally so that you have a total of 4 cake layers. Cover and set aside. Use a food processor to grind the freeze dried strawberries to a powder. Divide the powder into 2 portions and set them aside.\n"
            "Toss the fresh strawberries with 1/3 cup of the sugar. Macerate 30 minutes.\n"
            "Strawberry Mousse\nPuree and strain the fresh strawberries to make 2 cups of puree. If you have more than 2 cups save the excess for another use. Stir one portion of the strawberry powder into the puree.\n"
            "Place the liquor (or cool water) into a medium size microwave safe bowl. Sprinkle the gelatin in an even layer over the liquor and set it aside to bloom. Whip the cream with the other 1/3 cup of the sugar and fold it into the strawberry puree.\n"
            "Heat the bloomed gelatin in the microwave in 10 second increments until it's hot to the touch. Working quickly, add a 1/2 cup of the mousse to the warmed gelatin. Whisk to combine. Pour the gelatin mixture back into the mousse. Immediately whisk until the mousse is smooth and the gelatin is evenly incorporated. Use immediately to assemble the cake before the gelatin sets.\n"
            "Assembly\nWhisk the remaining strawberry powder into the prepared buttercream. Scoop half the buttercream into a piping bag fitted with a star tip.\n"
            'Place one cake layer on a cardboard cake circle or on a serving platter. Pipe a "dam" of strawberry buttercream around the edge of the cake layer.\n'
            "Scoop 1/3 of the strawberry mousse onto the layer and spread to fill in the buttercream dam. Repeat with the other cake layers.\n"
            "The cake will be quite soft at this point. Cover the cake with plastic wrap and refrigerate the cake for at least 30 minutes to set the buttercream dams and to allow the gelatin to start setting. Once the cake is firmed up, ice it with a thin crumb coat of buttercream. Chill to set the crumb coat then ice the cake with a final coating of buttercream.\n"
            "Pipe 12 buttercream rosettes around the top of the cake. Place a strawberry (can be dipped in chocolate) onto each rosette. Refrigerate for at least 5-6 hours to make sure the filling is completely set. Remove the cake from the refrigerator 1/2 hour before serving."
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(4.34, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        expected_description = "A light Chocolate Chiffon cake is filled with Strawberry Mousse. This is an ethereal, light as air dessert. It's the cake form of a chocolate covered strawberry."
        self.assertEqual(expected_description, self.harvester_class.description())
