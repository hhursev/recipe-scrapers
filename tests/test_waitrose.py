# mypy: allow-untyped-defs

from recipe_scrapers.waitrose import Waitrose
from tests import ScraperTest


class TestWaitroseScraper(ScraperTest):

    scraper_class = Waitrose

    def test_host(self):
        self.assertEqual("waitrose.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("waitrose.com", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Banana, chocolate and oatmeal tea bread", self.harvester_class.title()
        )

    def test_total_time(self):
        self.assertEqual(65, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "d1v30bmd12dhid.cloudfront.net/static/version6/content/dam/waitrose/recipes/images/b/0804058-r05.jpg/_jcr_content/renditions/cq5dam.thumbnail.200.200.png",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "1 Large egg",
            "75ml Vegetable oil",
            "125g Caster sugar",
            "3 Bananas, or 2 bananas and a handful dried banana chips",
            "30g Rolled oats",
            "150g Plain flour",
            "½ tsp Baking powder",
            "½ tsp Bicarbonate soda",
            "1 tsp Ground cinnamon",
            "40g Dark chocolate, finely chopped",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = [
            "Preheat the oven to 180°C/gas 4. Line a 1 litre (15cm x 7.5cm) loaf tin with buttered, non-stick baking parchment or silicone paper. Whisk the egg, oil and sugar together until thick. Slice 2 bananas finely and whisk into the mixture. Set aside 1 tbsp of the oats; fold in the remaining ingredients until the mixture is smooth.",
            "Pour the batter into the prepared tin and sprinkle the surface with the reserved oats.",
            "Slice the remaining banana and arrange the pieces on top, or use the dried chips.",
            "Bake for 40–50 minutes or until golden.",
            "The cake is done when a metal skewer inserted into the centre of the cake comes out clean. Allow the tea bread to cool in the tin, then transfer to a wire rack to cool completely.",
        ]
        expected_instructions = "\n".join(expected_instructions)
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(4.0, self.harvester_class.ratings())

    def test_description(self):
        self.assertEqual(
            "We make a fresh tea bread and muffins of the same flavour every day in the restaurant and shop kitchen. Many of our customers buy them for their children as they contain less added sugar than some other tea breads. The best bananas to use would be those slightly browning on the skin – not yellow ones. Use the best-quality bitter chocolate you can.",
            self.harvester_class.description(),
        )
