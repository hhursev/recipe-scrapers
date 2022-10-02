from recipe_scrapers.finedininglovers import FineDiningLovers
from tests import ScraperTest


class TestFineDiningLoversScraper(ScraperTest):

    scraper_class = FineDiningLovers

    @property
    def test_file_name(self):
        return "{}_3".format(self.scraper_class.__name__.lower())

    def test_host(self):
        self.assertEqual("finedininglovers.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.finedininglovers.com/article/black-forest-cake-recipe",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "The Ultimate Black Forest Cake Recipe"
        )

    def test_total_time(self):
        self.assertEqual(None, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual(None, self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "The black forest cake or gateau, a classic German cake synonymous with the 1980s, is derived from the traditional German dessert of schwartzwalder kirschtorte. This cake is usually made of layers of chocolate sponge, with whipped cream, maraschino cherries and chocolate shavings. It is mainly made with the German clear spirit kirschwasser, a traditional fruit brandy made from dark cherries, which gives the cake its cherry flavour and boozy content.\nWhat are the Ingredients for a German Black Forest Cake?\n500 g sour cherries\n150 g caster sugar\n100 g all purpose flour\n20 g cocoa powder\n450 ml double cream\n150 g butter\n200 g dark maraschino cherries\n50 g powder sugar\n50 g dark chocolate\n4 large eggs\n1 shot glass of kirshwasser or cherry syrup\nHow to Make a German Black Forest Cake\nFirst, sift the dry ingredients, the flour and the cocoa powder together in a bowl. Then, using a mixer with the whisk attachment, combine the caster sugar, the softened butter and the eggs until thick and foamy. Tip in the flour and cocoa mix and turn gently over until combined. Tip the mixture into three greased, loose-bottomed cake tins and bake in the oven until the sponge has risen and is firm, yet springy. Cool completely on a wire rack.\nFor the Cherry Compote\nFor this you may use a cherry pie filling, but better to use fresh cherries. Heat the dark cherries and cherry juice in a small pot with a little powdered sugar and, if desired, a squeeze of lemon juice. Reduce and allow to thicken. Take off the heat and add the shot of kirschwasser or cherry brandy.\nBuild the cake with the chocolate cake layers, alternating with the fresh cream, beaten until firm and standing in peaks, drizzled with the compote. Finish the tops of the cake with the remaining whipped cream for a fresh whipped cream frosting and cherries on top. Sprinkle liberally with dark chocolate shavings.\n\n\n\n\n\n\n\n\nWhy is it called a Black Forrest Cake?\nContrary to popular opinion, a Black Forest gateaux does not come from the German mountain range in Bavaria, but rather from the cherry fruit brandy that it is made with. In Germany in order to be officially called a Black Forest cake, it must contain kirschwasser.\nTry this easy step-by-step recipe for a Classic German Black Forest Cake\n",
            self.harvester_class.instructions(),
        )

    def test_image(self):
        return self.assertEqual(
            "https://www.finedininglovers.com/sites/g/files/xknfdk626/files/styles/open_graph_image/public/2021-03/german_dark_forest_cake_%C2%A9iStock.jpg?itok=afnz-p6c",
            self.harvester_class.image(),
        )
