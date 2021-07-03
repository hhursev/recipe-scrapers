from recipe_scrapers.mykitchen101 import MyKitchen101
from tests import ScraperTest


class TestMyKitchen101Scraper(ScraperTest):

    scraper_class = MyKitchen101

    def test_host(self):
        self.assertEqual("mykitchen101.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("清闲廚房 团队", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("古早味迷你烤鸡蛋糕", self.harvester_class.title())

    def test_yields(self):
        self.assertEqual("30 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://mykitchen101.com/wp-content/uploads/2020/11/mini-baked-egg-sponge-cake-mykitchen101-feature1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "4 个 蛋 (A级)",
                "125 克 细砂糖",
                "⅛ 茶匙 细盐",
                "115 克 普通面粉",
                "20 克 玉米淀粉",
                "30 克 溶化牛油",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "1 把烤炉预热至200°C/395°F。\n2 把蛋轻轻打散，加入盐和和糖，打至混合。\n3 把1公升的清水和400毫升的热水(热水炉取出的热水)混合在比搅拌碗大的钢盆以调出约45°C/113°F的温水。\n4 把搅拌碗浸泡在温水里，以中高速把蛋打至浓稠 (约5分钟)。(温馨提示：隔着温水打蛋糊可以缩短打发蛋糊的时间。)\n5 把普通面粉和玉米淀粉混合过筛2次。\n6 慢慢把粉类加入蛋糊里，以低速混合，再用刮刀翻拌至均匀。慢慢加入溶化牛油，用刮刀轻轻翻拌至混合。\n7 把面糊倒入裱花袋里。\n8 把迷你玛芬蛋糕模 (直径 = 4.8 cm，深 = 2.2 cm) 铺上杯子蛋糕纸托，装入面糊直到80%满。\n9 放入已预热的烤炉，以190°C/375°F 烘烤20-22分钟，直到呈金黄色。(温馨提示：不同烤炉的温度不一样，烘烤时间只供参考，可依个自的烤炉调整烘烤的时间。如果第一批烤24个蛋糕，第二批只有6个，那么第二批的烘烤时间可以缩短，只要蛋糕表面呈金黄色就可以了。)\n10 把鸡蛋糕脱模后放在铁架上至冷却。",
            self.harvester_class.instructions(),
        )
