from recipe_scrapers.ditchthecarbs import DitchTheCarbs
from tests import ScraperTest


class TestDitchTheCarbs(ScraperTest):

    scraper_class = DitchTheCarbs

    def test_host(self):
        self.assertEqual("ditchthecarbs.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.ditchthecarbs.com/easy-keto-hamburger-buns-almond-flour/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Keto Hamburger Buns")

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.ditchthecarbs.com/wp-content/uploads/2021/04/Easy-Keto-Hamburger-Buns-almond-flour-1200x1200-1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 egg",
                "1 tsp apple cider vinegar",
                "¼ cup ground flaxseed/linseed (ground)",
                "¾ cup almond meal/flour",
                "1¾ cup pre-shredded/grated mozzarella",
                "2 tbsp cream cheese",
                "1 tsp baking powder",
                "1 tsp extra virgin olive oil",
                "1 tsp sesame seeds",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat your oven to 375°F/190°C. In a small bowl mix together your egg and apple cider vinegar. Set aside until ready to use.\nMix\nAdd your flax seen to a grinder or blender, coarsely grind. Pour the flax seed in a microwave safe bowl. Add the almond flour and shredded mozzarella cheese to the bowl and mix. Then add your cream cheese to the bowl. There is no need to mix the cream cheese in just yet.\nMicrowave\nPlace your bowl with the cheese in the microwave. Melt your cheese for 1 minute, remove the bowl and mix with a silicone spatula. If your cheese is not completely melted yet microwave for 30 more seconds until your cheese is completely melted.\nMix\nWhile your mozzarella dough is still hot add your baking powder. Mix and fold together. Add the egg/vinegar mixture to your dough. Fold in with your silicone spatula.\nRoll your dough into a ball and cut into 4 equal sections. Roll each section into a ball and then flatten the top and bottom of the ball to shape into a hamburger bun.\nPlace on a baking sheet lined with baking paper. Brush the olive oil over your buns and sprinkle the tops with sesame seeds. Bake in the oven at 375°F/190°C for 12-15 minutes. Your burger buns will be done when the tops are golden brown and the dough is cooked in the centre.\nBake\nRemove the buns from the oven and let them cool on a wire rack or towel for 5 minutes before slicing and serving.",
            self.harvester_class.instructions(),
        )
