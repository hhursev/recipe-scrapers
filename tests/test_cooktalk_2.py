# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.cooktalk import CookTalk
from tests import ScraperTest


class TestCookTalkScraper(ScraperTest):
    scraper_class = CookTalk
    test_file_name = "cooktalk_2"

    def test_host(self):
        self.assertEqual("cook-talk.com", self.harvester_class.host())

    def canonical_url(self):
        self.assertEqual("https://cook-talk.com/?p=10440", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Гаспадыня", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Шоколадные маффины с крим-чизом", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Выпечка", self.harvester_class.category())

    def test_image(self):
        self.assertEqual(
            "https://cook-talk.com/archive/wp-content/uploads/2020/02/62.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        ingredients = [
            "140 г муки",
            "150 г сахара",
            "30 г алкализованного какао-порошка",
            "1/4 ч. л. соли",
            "1 ч. л. разрыхлителя",
            "180 мл теплой воды (около 38 °С)",
            "80 мл растительного масла",
            "2 ст. л. темного рома",
            "200 г полусладких шоколадных чипсов или мелко разломанного шоколада",
            "240 г сливочного сыра (крим-чиза)",
            "1 желток",
            "3 ст. л. сахара",
            "щепотка соли",
        ]
        self.assertEqual(ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "140 г муки",
                        "150 г сахара",
                        "30 г алкализованного какао-порошка",
                        "1/4 ч. л. соли",
                        "1 ч. л. разрыхлителя",
                        "180 мл теплой воды (около 38 °С)",
                        "80 мл растительного масла",
                        "2 ст. л. темного рома",
                        "200 г полусладких шоколадных чипсов или мелко разломанного шоколада",
                    ],
                    purpose=None,
                ),
                IngredientGroup(
                    ingredients=[
                        "240 г сливочного сыра (крим-чиза)",
                        "1 желток",
                        "3 ст. л. сахара",
                        "щепотка соли",
                    ],
                    purpose="— Начинка —",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        expected_instructions = (
            "Нагреть духовку до 180 °С. Форму для маффинов на 12 штук или мини-маффинов на 24 штуки смазать маслом и присыпать мукой.\n"
            "Просеять вместе муку, разрыхлитель, соль и какао.\n"
            "Смешать сахар, воду, растительное масло и ром.\n"
            "Соединить сухие ингредиенты и жидкие и быстро перемешать только до однородности. Тесто будет комковатым - это нормально. Вмешать в тесто шоколад.\n"
            "Для начинки взбить крим-чиз, сахар и соль одну минуту на низкой скорости, затем еще две минуты на средне-высокой. Соскрести начинку со стенок миски, добавить желток и взбить на средней скорости еще 30 минут. Как следует перемешать лопаткой.\n"
            "Выкладывать по неполной столовой ложке теста в каждую емкость, затем по чайной ложке с верхом начинки и снова по неполной столовой ложке теста.\n"
            "Выпекать посередине духовки около 12-20 минут (в зависимости от размера емкостей) или пока деревянная палочка, вставленная в центр маффина, не выйдет почти сухой.\n"
            "Остудить в форме 10 минут, затем перевернуть на решетку.\n"
            "Источник: I’m Dreaming of a Chocolate Christmas by Marcel Desaulniers"
        )
        actual_instructions = self.harvester_class.instructions()
        self.assertEqual(expected_instructions, actual_instructions)

    def test_description(self):
        self.assertEqual(
            "Плотные, насыщенные, слегка влажные маффины с контрастирующим вкусом шоколада и сливочного сыра.",
            self.harvester_class.description(),
        )

    def test_language(self):
        self.assertEqual("ru-RU", self.harvester_class.language())
