from recipe_scrapers.theclevercarrot import TheCleverCarrot
from tests import ScraperTest


class TestTheCleverCarrotScraper(ScraperTest):

    scraper_class = TheCleverCarrot

    def test_host(self):
        self.assertEqual("theclevercarrot.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.theclevercarrot.com/2017/12/how-to-make-sourdough-cinnamon-rolls-step-by-step-guide/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Soft Sourdough Cinnamon Rolls")

    def test_yields(self):
        self.assertEqual("8 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.theclevercarrot.com/wp-content/uploads/2017/12/How-to-Make-Sourdough-Cinnamon-Rolls-a-step-by-step-guide-13-225x225.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "160 g (2/3 cup) milk, whole or 2%",
                "28 g (2 tbsp) unsalted butter, melted (see note below)",
                "1 large egg",
                "100 g (1/2 cup) bubbly, active sourdough starter",
                "24 g (2 tbsp) granulated sugar",
                "300 g (2½ cups) all-purpose flour (I use King Arthur)",
                "5 g (1 tsp) fine sea salt",
                "cooking spray or oil, for coating",
                "28 g (2 tbsp) unsalted butter",
                "100 g (1/2 cup) granulated sugar",
                "3 tsp. ground cinnamon",
                "1 level tbsp. flour",
                "2 tbsp unsalted butter, softened",
                "⅓ cup whipped cream cheese, room temperature",
                "¼- 1/2 cup powdered sugar, sifted (add more if you like it sweet!)",
                "1-2 tbsp milk",
                "For a richer dough, increase the butter to 115 (8 tbsp) and use 360 g (3 cups) flour total. A reader recommended this tip, and I have to say, it’s my preferred method.",
                "Make sure the melted butter and milk mixture has cooled slightly before making the dough. If it’s too hot, the dough will become incredibly sticky like cake batter (I’ve experienced this many times). If this happens to you, don’t worry- wait for the dough to cool down before adding more flour, if needed.",
                "Recent recipe update: flour has been added to the cinnamon-sugar filling as a binder to prevent the butter from leaking out of the rolls.",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Baker's Schedule\nOvernight Option\nMake the dough in the evening and let rise overnight. The following morning, roll, cut and shape the dough. Rest for 1-2 hours (second rise) before baking.\nAs an alternative, after resting for 1 hour, cover the dough and chill until ready to use. Rest at room temperature before baking. The dough should be plump and puffy before baking.\nMake-Ahead Option (Freeze): Place the cut & shaped cinnamon rolls into a parchment lined 9-inch springform pan. Cover with two layers of plastic wrap. Freeze until ready to use. The night before baking, remove the old plastic wrap and replace with fresh wrap (this prevents any condensation from dripping onto the rolls). Defrost overnight, about 10-12 hrs. at room temperature, approximately 67 F. Bake the following morning as directed.\nMake the Dough\nIn the evening: Combine the melted butter and milk in a small bowl. Cool slightly before using.\nAdd the egg, sourdough starter, and sugar to the bowl of a stand mixer fitted with the paddle attachment. Mix to combine. With the machine running, slowly pour in the milk mixture. Add the flour and salt. Continue mixing until a rough, sticky dough forms, about 1 minute. Scrape down the sides of the bowl. Cover with a damp towel and let rest for 30 minutes.\nAfter the dough has rested, switch to the dough hook. Knead on medium-low speed for 6-8 minutes (I use #2 or #3 on my stand mixer). The dough should feel soft, supple and pull away from the sides of the bowl when ready. If it’s too sticky add a small bit of flour.\nBulk Rise\nTransfer the dough to a medium-size bowl coated in butter. Cover with plastic wrap. Let rise overnight until double in size, about 8-12 + hrs. @ 67-68 F, depending on temperature.\nStretch and Fold the Dough (optional step): about 30 minutes- 1 hr. into the bulk rise stretch and fold the dough: grab a portion of the dough and stretch it upward. Fold it over toward the center of the bowl. Give the bowl a 1/4 turn; stretch and fold the dough again. Continue this technique until you’ve come full circle around the bowl (4 folds total). For video guidance, click here. This optional step will increase the overall volume of the rolls and aerate the dough.\nRoll the Dough\nIn the morning: Line a 9-inch springform pan with parchment paper. I like to scrunch the paper into a ball first, open it up, and then line the inside with enough excess to hang over the sides for easy removal. It tends to fit better this way.\nLightly oil and flour your countertop to prevent sticking. Coax the dough out of the bowl. Gently pat into a rough rectangle. Let rest for 10 minutes for easier rolling.\nDust the dough (and your rolling pin) with flour. Roll the dough into a 16 x 12-ish rectangle using a tape measure for accuracy. If the dough resists, let rest for 5-10 minutes and try again.\nMake the Cinnamon-Sugar Filling\nCombine the cinnamon, sugar and flour in a small bowl; set aside. Melt the 28 g (2 tbsp) of butter in a shallow pan or microwave. Once the butter has cooled slightly, brush the entire surface of the dough, including the top, bottom and sides. Sprinkle the dough with the cinnamon-sugar mixture leaving a 1/2-inch border around the edges. Smooth it out with your hands.\nShape & Cut the Dough\nStarting on the long side of the dough (16-inch), roll it into a log pressing down gently as you go. Take your time with this step. The log needs to be tight so the swirls stay in tact. You should end up seam side down. TIP: if the dough starts to get sticky from the heat of your hands, lightly oil or flour your fingertips, take a deep breath and try again.\nCut the dough into 2-inch sections using a oiled knife or bench scraper. I lightly “mark” the dough first to make sure each piece is roughly the same size.\nSecond Rise\nPlace the rolls into the lined pan and let rest for 1- 2 hours, or until the dough puffs up. Alternatively, if you’d like to chill or freeze the rolls, please refer to the “Make-Ahead” option in the Baker’s Schedule at the top of this recipe.\nBake the Cinnamon Rolls\nPreheat oven to 350 F. Bake the dough onto the center rack and bake for 35-40 minutes (check at the 30 minute mark). The tops should turn light golden brown when ready.\nRemove from the oven and cool in the pan for 15 minutes. This helps the butter to absorb back into the dough. Then lift up the rolls, while still on the parchment paper, and transfer to a wire rack.\nMake the Glaze\nWhile the rolls are baking or cooling make the glaze. Add softened butter, whipped cream cheese and sifted powdered sugar to the bowl of a stand mixer. Beat until smooth, thinning out the consistency with a little milk as needed. The ingredients must be soft and at room temperature for best results.\nTo serve, top the rolls with some of the glaze or lightly dust with powdered sugar. These rolls are best enjoyed slightly warm on the same day they are baked.",
            self.harvester_class.instructions(),
        )
