from tests import ScraperTest

from recipe_scrapers.domowewypieki import DomoweWypieki


class TestDomoweWypiekiScraper(ScraperTest):
    scraper_class = DomoweWypieki

    def test_host(self):
        self.assertEqual("domowe-wypieki.pl", self.harvester_class.host())

    def test_title(self):
        self.assertEqual("Tort czekoladowy w stylu number cake z biszkoptu", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(115, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("12 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual("//static.domowe-wypieki.pl/images/content/1232/tort_number_cake_z_biszkoptu.jpg",
                         self.harvester_class.image())

    def test_ingredients(self):
        self.assertCountEqual([
            "2 biszkopty kakaowe (składniki podane na 2 blaty):",
            "8 jajek (rozmiar M), temperatura pokojowa",
            "300 g cukru",
            "240 g mąki pszennej (lub w wersji bezglutenowej: uniwersalnej mąki bezglutenowej)",
            "30 g kakao",
            "Krem czekoladowy:",
            "150 g czekolady gorzkiej, 50% kakao",
            "400 g słodkiej śmietany 30- 36%",
            "400 g serka mascarpone, schłodzonego",
            "2 łyżki cukru pudru",
            "Dekoracja:",
            "kilka świeżych malin",
            "bezy",
            "słodycze: precelki w czekoladzie, paluszki mikado, draże czekoladowe z orzechami",
            "Dodatkowo:",
            "banan",
            "1 łyżka soku z cytryny",
            "kakao do posypania",
        ], self.harvester_class.ingredients())

    def test_instructions(self):
        self.assertEqual(
            "\n".join([
                "Do kremu czekoladowego należy najpierw przygotować ganache: Czekoladę posiekać i przełożyć do wysokiej miski. Śmietanę doprowadzić do zagotowania, od razu ściągnąć z pieca i zalać czekoladę. Odczekać ok. 1- 2 minuty, aby czekolada zmiękła, a następnie wymieszać łyżką, aż czekolada całkowicie się rozpuści i powstanie gładka masa. (Gdyby masa nie była gładka, zmiksować ją bardzo krótko blenderem do uzyskania jednolitej masy). Pozostawić do ostygnięcia, a następnie przykryć np. talerzykiem i wstawić na kilka godzin (ok. 6) lub na noc do lodówki.",
                "Dużą, płaską blachę z piekarnika (o wymiarach ok. 30x 40cm) wyłożyć papierem do pieczenia.",
                "Przygotować pierwszy biszkopt: 120 g mąki i 15 g kakao wymieszać i przesiać. Odstawić na bok. Z 4 jajek oddzielić białka od żółtek. Białka ubić na sztywną pianę. Następnie dodawać stopniowo 150 g cukru. Cały czas miksując, dodawać po kolei po jednym żółtku. Mąkę z kakao dodawać porcjami do masy jajecznej, delikatnie mieszając szpatułką lub łyżką drewnianą, tylko do połączenia się składników.",
                "Gotowe ciasto wyłożyć równomiernie na przygotowanej blasze.",
                "Piec w nagrzanym piekarniku ok. 12 minut w temperaturze 180°C, grzałka góra- dół, do suchego patyczka.",
                "Po upieczeniu, biszkopt z papierem zsunąć na kratkę z piekarnika i pozostawić do całkowitego ostygnięcia.",
                "Przygotować drugi, taki sam biszkopt. Pozostawić do ostygnięcia.",
                "W tym czasie przygotować szablony cyfr. (Można skorzystać z załączonego szablonu podanego we wstępie, wydrukować potrzebne cyfry i wyciąć nożyczkami).",
                "Na blacie kuchennym rozłożyć dwa papiery do pieczenia, na które odwrócić biszkopty (papierem, na którym były pieczone do góry). Papier ostrożnie ściągnąć.",
                "Na biszkopcie rozłożyć wycięte cyfry z papieru i przy pomocy ostrego nożyka wyciąć cyfry z ciasta. Z obu biszkoptów wyciąć po dwie te same cyfry. (Cyfry można wyciąć z dowolnej strony biszkoptu. Jak widzicie na zdjęciach, ja wycięłam cyfry na odwróconym biszkopcie i cyfry również odwróciłam). Niewykorzystane skrawki ciasta odłożyć na bok.",
                "Do schłodzonego ganache dodać schłodzony serek mascarpone i przesiany cukier puder. Całość zmiksować do momentu zgęstnienia kremu. (Nie miksować za długo, aby krem się nie zwarzył).",
                "Krem czekoladowy przełożyć do rękawa cukierniczego z dużą, okrągłą tylką.",
                "Liczbę z biszkoptu ułożyć na desce/ tacce lub prostokątnym podkładzie do ciasta.",
                "Na biszkopt wycisnąć kleksy kremu, robiąc najpierw brzegi, a następnie wypełniając środek.",
                "Banana obrać, pokroić w kostkę, przełożyć do miski i obtoczyć w 1 łyżce soku z cytryny. Kawałki banana wcisnąć delikatnie w krem.",
                "Przykryć cyframi z biszkoptu i wycisnąć resztę kremu. (Kremu może zostać w zależności od użytych cyfr. Nie szkodzi. Proszę go zachować). Tort wstawić do lodówki. (Tort może zostać podany w dzień przygotowania lub na następny dzień).",
                "Z resztek ciasta można zrobić pralinki, albo cake popsy. W tym celu ciasto pokruszyć rękami. Dodać niewykorzystany krem. Do tego dodać ze 2 łyżki kremu orzechowo- czekoladowego typu nutella oraz tyle serka mascarpone lub kremowego, aby powstała masa, która się nie kruszy, ani nie klei do rąk. Z masy formować kulki o średnicy ok. 4cm. Kulki układać na desce wyłożonej papierem do pieczenia. Schłodzić w lodówce, a następnie obtoczyć lub polać roztopioną czekoladą. (Jeśli chcecie zrobić cake pops to proszę przeczytać np. w tym przepisie: \"Czekoladowe cake pops\" jak postępować z patyczkami).",
                "W dzień podania tortu, krem oprószyć kakao i udekorować słodyczami i owocami.",

            ])
            , self.harvester_class.instructions())

    def test_description(self):
        self.assertEqual(
            "Cyfrowy tort z biszkoptu kakaowego przełożonego czekoladowym kremem z serka mascarpone, wzbogaconego o kawałki banana. Udekorowany jest bezami, kupnymi słodyczami i malinami. Tort jest lekki, mocno czekoladowy, nie za słodki i może być również bezglutenowy. Urodzinowy tort, który smakuje małym i dużym gościom.\nPrzepis jest na tort składający się z liczby dwucyfrowej. Możecie skorzystać z podanego przeze mnie szablonu lub wydrukować swoje cyfry, według wybranej czcionki. Moje cyfry są wysokie na 20 cm i na szerokość mieszczą się po dwie na blasze. Z resztek ciasta, pozostałych po wycięciu liczby można zrobić pralinki lub cake pops na patyku.\n>> Kliknij aby pobrać szablon <<",
            self.harvester_class.description(),
        )
