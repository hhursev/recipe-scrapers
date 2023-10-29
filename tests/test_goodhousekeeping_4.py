# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.goodhousekeeping import GoodHousekeeping
from tests import ScraperTest


class TestGoodHousekeepingScraper(ScraperTest):
    scraper_class = GoodHousekeeping
    test_file_name = "goodhousekeeping_4"

    def test_host(self):
        self.assertEqual("goodhousekeeping.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Ailsa Burt", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Jaffa Cake cheesecake", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("baking,dessert", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(85, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("10 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://hips.hearstapps.com/hmg-prod/images/jaffa-cheesecake-1548684397.jpg?crop=0.502xw:1.00xh;0.498xw,0&resize=1200:*",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "100 g unsalted butter, very soft, plus extra to grease",
                "100 g caster sugar",
                "2 medium eggs",
                "100 g self-raising flour",
                "1 tbsp. milk",
                "1 tsp. vanilla extract",
                "500 g cream cheese",
                "100 g icing sugar",
                "1 tsp. vanilla extract",
                "300 mL double cream",
                "Vegetable oil, to grease",
                "5 gelatine leaves",
                "275 g good quality no-peel Seville orange marmalade",
                "200 g good quality dark chocolate, broken into pieces",
                "1 1/2 tsp. sunflower oil",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    purpose="For the sponge",
                    ingredients=[
                        "100 g unsalted butter, very soft, plus extra to grease",
                        "100 g caster sugar",
                        "2 medium eggs",
                        "100 g self-raising flour",
                        "1 tbsp. milk",
                        "1 tsp. vanilla extract",
                    ],
                ),
                IngredientGroup(
                    purpose="For the cheesecake filling",
                    ingredients=[
                        "500 g cream cheese",
                        "100 g icing sugar",
                        "1 tsp. vanilla extract",
                        "300 mL double cream",
                    ],
                ),
                IngredientGroup(
                    purpose="For the jelly",
                    ingredients=[
                        "Vegetable oil, to grease",
                        "5 gelatine leaves",
                        "275 g good quality no-peel Seville orange marmalade",
                    ],
                ),
                IngredientGroup(
                    purpose="For the chocolate topping",
                    ingredients=[
                        "200 g good quality dark chocolate, broken into pieces",
                        "1 1/2 tsp. sunflower oil",
                    ],
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        instructions = [
            "Make the sponge. Preheat oven to 170°C (150°C fan) mark 3. Lightly grease the base and sides of a 20.5cm (8in) round springform tin. Line the base of the tin with parchment.",
            "Put the ingredients for the cake in a mixing bowl. Beat for 30sec until smooth and combined, using a hand-held electric whisk. Tip the mixture into the tin and spread to level. Bake for 25min, or until the cake is golden, risen and a skewer inserted into the centre comes out clean.",
            "Leave to cool in tin for 5min, then unclip and remove cake from tin on to a wire rack and leave to cool completely. Clean tin. Turn base of tin over so it’s flat-side up. Take a 30.5cm (12in) sheet of baking parchment and lay it over the base of the tin. Carefully clip the paper-covered base back into the tin so paper is tightly stretched over base and any overhang is trapped between base and sides of tin, then grease and line sides of tin with another piece of baking parchment. Peel and discard parchment from the bottom of the cake, then place into the prepared tin, flat side down.",
            "Make the filling. Using a hand-held electric whisk, beat together the cream cheese and icing sugar until smooth, then beat in the double cream and vanilla until the mixture is thick and holds its shape.",
            "Spoon the cheesecake mixture into the cake tin and spread on top of the cake to make an even layer. Chill in the fridge for at least 6hr or overnight.",
            "While the cheesecake sets, make the jelly. Grease a 18cm (7in) round tin. Line with a large piece of clingfilm, smoothing any creases and air bubbles out with your fingers as best as possible. Put gelatine leaves to soak in a small bowl of cold water for 5min.",
            "Gently heat marmalade in a small pan, whisking frequently until melted and smooth. Lift gelatine out of bowl and squeeze out excess water. Add soaked gelatine leaves to marmalade and whisk again over a low heat until gelatine is melted and combined. Pour marmalade mixture into the cling film lined tin and leave to cool to room temperature. Chill for 30min or until set, then remove from fridge and keep at room temperature.",
            "When the cheesecake has set, make the chocolate topping. Put chocolate in a heatproof bowl set over a pan of gently simmering water, stirring occasionally until melted and smooth (don’t let the bottom of the bowl come in contact with the water). Remove from heat and stir oil in really well. Leave to cool for 5-10min, until chocolate is room temperature and no longer feels warm when you spoon a drop on your finger.",
            "Meanwhile, unclip cheesecake from tin and slide on to a serving plate. Peel off the parchment around the sides. Remove the jelly layer from the tin and carefully put on top of the cheesecake layer, in the centre.",
            "Carefully pour cooled melted chocolate on top of jelly and spread gently to the edge of the cheesecake. Working quickly, lightly press a wire rack down on to the melted chocolate and lift immediately to make a criss-cross pattern. Chill the cheesecake for at least 15min or until the chocolate is set, then slice and serve (see GH Tip).",
        ]
        self.assertEqual("\n".join(instructions), self.harvester_class.instructions())

    def test_cuisine(self):
        self.assertEqual(None, self.harvester_class.cuisine())

    def test_nutrients(self):
        self.assertEqual(
            {
                "calories": "555cals",
                "fatContent": "36g",
                "fiberContent": "1g",
                "proteinContent": "7g",
                "saturatedFatContent": "22g",
                "sugarContent": "43g",
                "carbohydrateContent": "50g",
            },
            self.harvester_class.nutrients(),
        )

    def test_description(self):
        self.assertEqual(
            "Full moon, half moon, total eclipse - this jaffa cake cheesecake is bound to please to whole family!",
            self.harvester_class.description(),
        )
