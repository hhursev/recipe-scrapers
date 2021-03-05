from recipe_scrapers.cookpad import CookPad
from tests import ScraperTest


class TestCookPadScraper(ScraperTest):

    scraper_class = CookPad

    def test_host(self):
        self.assertEqual("cookpad.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://cookpad.com/recipe/4610651", self.harvester_class.canonical_url()
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "30分で簡単本格バターチキンカレー")

    def test_yields(self):
        self.assertEqual("4人分 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://img.cpcdn.com/recipes/4610651/640x640c/6de3ac788480ce2787e5e39714ef0856?u=6992401&p=1519025894",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "♥鶏モモ肉 500g前後",
                "♥玉ねぎ 2個",
                "♥にんにくチューブ 5cm",
                "♥生姜チューブ 5cm(なくても♡)",
                "♥カレー粉 大さじ1と1/2",
                "♥バター 大さじ2+大さじ3(60g)",
                "＊トマト缶 1缶",
                "＊コンソメ 小さじ1",
                "＊塩 小さじ(1〜)2弱",
                "＊砂糖 小さじ2",
                "＊水 100ml",
                "＊ケチャップ 大さじ1",
                "♥生クリーム 100ml",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "鶏モモ肉 は一口大に、 玉ねぎ は薄切り(orみじん切り)にします♪\nフライパンに バター(大さじ2) を熱し、鶏肉 に 塩胡椒 をふり表面をこんがり焼きます♪\nお鍋に バター(大さじ3) にんにくチューブ 生姜チューブ 玉ねぎ を入れてあめ色になるまでじっくり炒めます♪\nカレー粉 を加えて弱火で3分くらい炒めます♪\n＊ と 鶏肉(油分も) を加えて沸騰したら火が通るまで(10分程)煮ます♪\n仕上げに 生クリーム を加えて混ぜ、温まったらすぐ火を止めます♪ 完成♡♡ 更に仕上げに生クリームをトッピングしました♡\n子供ごはんはこんな感じの盛り付けに♡♥",
            self.harvester_class.instructions(),
        )
