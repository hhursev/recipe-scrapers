from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.tasteau import TasteAU
from tests import ScraperTest


class TestTasteAUScraper2(ScraperTest):

    scraper_class = TasteAU
    test_file_name = "tasteau_2"

    def test_host(self):
        self.assertEqual("taste.com.au", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Michelle Southan", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Milo crumble hot chocolate cake recipe", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("dessert", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(115, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("16 servings", self.harvester_class.yields())

    def test_ratings(self):
        self.assertEqual(3.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("australian", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Indulge in this spectacular layered cake, with crunchy Milo clusters, hot chocolate syrup, and jumbo marshmallows. This rich chocolate cake will have everyone asking for a second slice!",
            self.harvester_class.description(),
        )

    def test_image(self):
        self.assertEqual(
            "https://img.taste.com.au/M1fun6UC/taste/2019/06/milo-crumble-hot-chocolate-cake-151265-3.jpg",
            self.harvester_class.image(),
        )

    def test_consistent_ingredients_lists(self):
        self.assertEqual(
            sorted(
                [
                    "100g (1/2 cup, firmly packed) brown sugar",
                    "100g dark cooking chocolate, coarsely chopped",
                    "125ml (1/2 cup) thickened cream",
                    "17.40 gm vanilla extract",  # Added this line
                    "185ml (3/4 cup) milk",
                    "2 x 250g pkt cream cheese, at room temperature",
                    "20.00 gm cocoa powder",
                    "200g sour cream",
                    "21.00 gm fresh lemon juice",
                    "27.80 gm glucose syrup",
                    "3.00 gm gelatine powder",
                    "300g unsalted butter, at room temperature",
                    "30g (1/4 cup) almond meal",
                    "315g (1 1/2 cups) caster sugar",
                    "395g can sweetened condensed milk",
                    "4 eggs, at room temperature",
                    "4.40 gm vanilla extract",
                    "450g (3 cups) self-raising flour",
                    "55g (1/3 cup) malted milk drink powder",
                    "55g (1/4 cup, firmly packed) brown sugar",
                    "60g butter, chopped",
                    "7-8 jumbo marshmallows",
                    "70g (1/2 cup) Milo",
                    "75g (1/2 cup) self-raising flour",
                ]
            ),
            sorted(self.harvester_class.ingredients()),
        )

    def test_instructions(self):
        instructions = self.harvester_class.instructions()
        expected_instructions = (
            "Preheat oven to 180C/160C fan forced. Grease three 8cm-deep, 20cm round cake pans. Line base and side with baking paper.\n"
            "Use electric beaters to beat butter, caster sugar and vanilla in a bowl until pale and creamy. Add eggs, 1 at a time, beating well after each addition. Add half the flour and half the combined sour cream and milk. Beat on low until just combined. Repeat with remaining flour and combined sour cream and milk until just combined. Divide mixture among the prepared pans. Smooth surface.\n"
            "Bake for 30 minutes or until a skewer inserted into the centre of the cakes comes out clean. Set aside in pans for 15 minutes to cool slightly before transferring to wire racks to cool completely.\n"
            "Meanwhile, to make the crumble, line a baking tray with baking paper. Place flour and butter in a bowl. Use fingertips to rub butter into flour until mixture resembles coarse crumbs. Stir in the Milo, brown sugar and almond meal until well combined and evenly coloured. Spread over the prepared tray. Bake, stirring every 10 minutes, for 20-25 minutes or until crisp and darkened slightly. Set aside to cool and harden.\n"
            "While crumble is baking, make the hot chocolate syrup. Combine all the ingredients in a saucepan with 250ml (1 cup) water. Stir over a low heat until sugar dissolves. Increase heat to medium. Bring to a rapid simmer. Simmer for 10-15 minutes or until reduces slightly and thickens to 185ml (3/4 cup).\n"
            "To make the cheesecake, use electric beaters to beat cream cheese and malt powder in a bowl until smooth. Beat in the condensed milk. Place the lemon juice in a small microwave-safe bowl. Sprinkle with the gelatine. Use a fork to whisk until just combined. Microwave on High for 8-10 seconds to heat slightly. Whisk until dissolved. With the beaters running, beat into cream cheese mixture until combined.\n"
            "Line an 8cm-deep, 20cm round cake pan with baking paper, making sure paper extends at least 5cm above pan. Use a large serrated knife to trim top of each cake to level. Place 1 cake, trimmed-side up, into prepared pan. Brush cake with one-third of hot syrup. Spoon half the cheesecake on top and spread until even and fully covering cake. Use hands to crush 85g (3/4 cup) Milo crumble into smaller pieces and scatter over with the gelatine. Use a fork to whisk until just combined. Microwave on High for 8-10 seconds to heat slightly. Whisk until dissolved. With the beaters running, beat into cream cheese mixture until combined. 7 Line an 8cm-deep, 20cm round cake pan with baking paper, making sure paper extends at least 5cm above pan. Use a large serrated knife to trim top of each cake to level. Place 1 cake, trimmed-side up, into prepared pan. Brush cake with one-third of hot syrup. Spoon half the cheesecake on top and spread until even and fully covering cake. Use hands to crush 85g (3⁄4 cup) Milo crumble into smaller pieces and scatter over cheesecake. Repeat with another cake, half the remaining syrup, remaining cheesecake and 85g (3/4 cup) remaining crumble. Brush trimmed side of last cake with remaining syrup and place, syrup-side down, on top of layers, pressing down very lightly. Cover with plastic wrap. Place in the fridge for at least 6 hours or overnight to chill and set.\n"
            "Remove the cake from the fridge and set aside for 30 minutes to bring to room temperature. Place cake on a serving plate.\n"
            "Place marshmallows on a baking tray. Use a blowtorch to caramelise. (Be careful as they can ignite quickly if flame is too close.)\n"
            "Place the dark chocolate, thickened cream and glucose in a microwave-safe bowl. Microwave on High for 1-2 minutes or until melted. Stir until smooth.\n"
            "Pour warm chocolate sauce over cake and, working quickly, spread over edge so it drips down side of cake. Top with toasted marshmallows and remaining crumble."
        )
        self.assertEqual(expected_instructions, instructions)

    def test_ingredient_groups(self):
        return self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "300g unsalted butter, at room temperature",
                        "315g (1 1/2 cups) caster sugar",
                        "4.40 gm vanilla extract",
                        "4 eggs, at room temperature",
                        "450g (3 cups) self-raising flour",
                        "200g sour cream",
                        "185ml (3/4 cup) milk",
                        "7-8 jumbo marshmallows",
                        "100g dark cooking chocolate, coarsely chopped",
                        "125ml (1/2 cup) thickened cream",
                        "27.80 gm glucose syrup",
                    ],
                    purpose=None,
                ),
                IngredientGroup(
                    ingredients=[
                        "75g (1/2 cup) self-raising flour",
                        "60g butter, chopped",
                        "70g (1/2 cup) Milo",
                        "55g (1/4 cup, firmly packed) brown sugar",
                        "30g (1/4 cup) almond meal",
                    ],
                    purpose="Milo Crumble",
                ),
                IngredientGroup(
                    ingredients=[
                        "20.00 gm cocoa powder",
                        "4.40 gm vanilla extract",
                        "100g (1/2 cup, firmly packed) brown sugar",
                    ],
                    purpose="Hot chocolate syrup",
                ),
                IngredientGroup(
                    ingredients=[
                        "2 x 250g pkt cream cheese, at room temperature",
                        "55g (1/3 cup) malted milk drink powder",
                        "395g can sweetened condensed milk",
                        "21.00 gm fresh lemon juice",
                        "3.00 gm gelatine powder",
                    ],
                    purpose="Malt cheesecake",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )
