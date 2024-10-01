from __future__ import annotations

__all__ = (
    "AbstractScraper",
    "ElementNotFoundInHtml",
    "FieldNotProvidedByWebsiteException",
    "NoSchemaFoundInWildMode",
    "RecipeSchemaNotFound",
    "StaticValueException",
    "WebsiteNotImplementedError",
    "scrape_html",
)

import warnings

try:
    # requests is an optional dependency; we can provide better error messages
    # when we know that it's unavailable before a user attempts a web request
    import requests
except ImportError as e:
    requests_import_error: Exception | None = e
else:
    requests_import_error = None

from ._abstract import HEADERS, AbstractScraper
from ._exceptions import (
    ElementNotFoundInHtml,
    FieldNotProvidedByWebsiteException,
    NoSchemaFoundInWildMode,
    RecipeSchemaNotFound,
    StaticValueException,
    WebsiteNotImplementedError,
)
from ._factory import SchemaScraperFactory
from ._utils import get_host_name
from .aberlehome import AberleHome
from .abril import Abril
from .abuelascounter import AbuelasCounter
from .acouplecooks import ACoupleCooks
from .addapinch import AddAPinch
from .afghankitchenrecipes import AfghanKitchenRecipes
from .aflavorjournal import AFlavorJournal
from .akispetretzikis import AkisPetretzikis
from .albertheijn import AlbertHeijn
from .aldi import Aldi
from .alexandracooks import AlexandraCooks
from .alittlebityummy import ALittleBitYummy
from .allrecipes import AllRecipes
from .allthehealthythings import AllTheHealthyThings
from .alltomat import AllTomat
from .altonbrown import AltonBrown
from .amazingribs import AmazingRibs
from .ambitiouskitchen import AmbitiousKitchen
from .americastestkitchen import AmericasTestKitchen
from .archanaskitchen import ArchanasKitchen
from .argiro import Argiro
from .arla import Arla
from .atelierdeschefs import AtelierDesChefs
from .averiecooks import AverieCooks
from .bakels import Bakels
from .bakingmischief import BakingMischief
from .bakingsense import BakingSense
from .barefeetinthekitchen import BarefeetInTheKitchen
from .barefootcontessa import BareFootContessa
from .bbcfood import BBCFood
from .bbcgoodfood import BBCGoodFood
from .bestrecipes import BestRecipes
from .bettybossi import BettyBossi
from .bettycrocker import BettyCrocker
from .biancazapatka import BiancaZapatka
from .bigoven import BigOven
from .blueapron import BlueApron
from .bluejeanchef import BlueJeanChef
from .bodybuilding import Bodybuilding
from .bonappetit import BonAppetit
from .bongeats import BongEats
from .bowlofdelicious import BowlOfDelicious
from .breadtopia import Breadtopia
from .briceletbaklava import BricelEtBaklava
from .budgetbytes import BudgetBytes
from .cafedelites import CafeDelites
from .carlsbadcravings import CarlsBadCravings
from .castironketo import CastIronKeto
from .cdkitchen import CdKitchen
from .celebratingsweets import CelebratingSweets
from .chefkoch import Chefkoch
from .chefnini import Chefnini
from .chefsavvy import ChefSavvy
from .closetcooking import ClosetCooking
from .comidinhasdochef import ComidinhasDoChef
from .cookeatshare import CookEatShare
from .cookieandkate import CookieAndKate
from .cookingcircle import CookingCircle
from .cookinglight import CookingLight
from .cookpad import CookPad
from .cookscountry import CooksCountry
from .cooksillustrated import CooksIllustrated
from .cooktalk import CookTalk
from .copykat import CopyKat
from .costco import Costco
from .countryliving import CountryLiving
from .creativecanning import CreativeCanning
from .cucchiaio import Cucchiaio
from .cuisineaz import CuisineAZ
from .cybercook import Cybercook
from .damndelicious import DamnDelicious
from .davidlebovitz import DavidLebovitz
from .delish import Delish
from .dinneratthezoo import DinnerAtTheZoo
from .dinnerthendessert import DinnerThenDessert
from .dishnz import Dishnz
from .dobruchutaktualitysk import DobruChutAktualitySK
from .domesticateme import DomesticateMe
from .donalskehan import DonalSkehan
from .downshiftology import Downshiftology
from .dr import Dr
from .eatingbirdfood import EatingBirdFood
from .eatingwell import EatingWell
from .eatliverun import EatLiveRun
from .eatsmarter import Eatsmarter
from .eatthismuch import EatThisMuch
from .eattolerant import EatTolerant
from .eatwell101 import EatWell101
from .eatwhattonight import EatWhatTonight
from .elavegan import ElaVegan
from .emmikochteinfach import EmmiKochtEinfach
from .epicurious import Epicurious
from .errenskitchen import ErrensKitchen
from .ethanchlebowski import EthanChlebowski
from .evolvingtable import EvolvingTable
from .familyfoodonthetable import FamilyfoodOnTheTable
from .farmhousedelivery import FarmhouseDelivery
from .farmhouseonboone import FarmhouseOnBoone
from .fattoincasadabenedetta import FattoInCasaDaBenedetta
from .felixkitchen import FelixKitchen
from .fifteengram import FifteenGram
from .fifteenspatulas import FifteenSpatulas
from .finedininglovers import FineDiningLovers
from .fitmencook import FitMenCook
from .fitslowcookerqueen import FitSlowCookerQueen
from .food import Food
from .food52 import Food52
from .foodandwine import FoodAndWine
from .foodfidelity import FoodFidelity
from .foodnetwork import FoodNetwork
from .foodrepublic import FoodRepublic
from .forksoverknives import ForksOverKnives
from .forktospoon import ForkToSpoon
from .franzoesischkochen import FranzoesischKochen
from .g750g import G750g
from .gesundaktiv import GesundAktiv
from .giallozafferano import GialloZafferano
from .gimmesomeoven import GimmeSomeOven
from .globo import Globo
from .glutenfreeonashoestring import GlutenFreeOnAShoeString
from .godt import Godt
from .gonnawantseconds import GonnaWantSeconds
from .goodfooddiscoveries import GoodFoodDiscoveries
from .goodhousekeeping import GoodHousekeeping
from .gourmettraveller import GourmetTraveller
from .grandfrais import GrandFrais
from .greatbritishchefs import GreatBritishChefs
from .grimgrains import GrimGrains
from .grouprecipes import GroupRecipes
from .halfbakedharvest import HalfBakedHarvest
from .handletheheat import HandleTheHeat
from .hassanchef import HassanChef
from .headbangerskitchen import HeadbangersKitchen
from .heatherchristo import HeatherChristo
from .heb import HEB
from .hellofresh import HelloFresh
from .hersheyland import HersheyLand
from .homechef import HomeChef
from .hostthetoast import Hostthetoast
from .ica import Ica
from .ig import IG
from .imworthy import ImWorthy
from .inbloombakery import InBloomBakery
from .indianhealthyrecipes import IndianHealthyRecipes
from .ingoodflavor import InGoodFlavor
from .innit import Innit
from .insanelygoodrecipes import InsanelyGoodRecipes
from .inspiralized import Inspiralized
from .izzycooking import IzzyCooking
from .jamieoliver import JamieOliver
from .jimcooksfoodgood import JimCooksFoodGood
from .jocooks import JoCooks
from .joshuaweissman import JoshuaWeissman
from .joyfoodsunshine import Joyfoodsunshine
from .joythebaker import JoyTheBaker
from .juliegoodwin import JulieGoodwin
from .justataste import JustATaste
from .justbento import JustBento
from .justonecookbook import JustOneCookbook
from .kalejunkie import KaleJunkie
from .kennymcgovern import KennyMcGovern
from .keukenliefdenl import KeukenLiefdeNL
from .kingarthur import KingArthur
from .kitchenaidaustralia import KitchenAidAustralia
from .kitchendreaming import KitchenDreaming
from .kitchensanctuary import KitchenSanctuary
from .kitchenstories import KitchenStories
from .kochbar import Kochbar
from .kochbucher import Kochbucher
from .koket import Koket
from .kristineskitchenblog import KristinesKitchenBlog
from .kuchniadomowa import KuchniaDomowa
from .kuchynalidla import KuchynaLidla
from .kwestiasmaku import KwestiaSmaku
from .latelierderoxane import LAtelierDeRoxane
from .leanandgreenrecipes import LeanAndGreenRecipes
from .lecker import Lecker
from .lecremedelacrumb import LeCremeDeLaCrumb
from .leitesculinaria import LeitesCulinaria
from .lekkerensimpel import LekkerEnSimpel
from .leukerecepten import Leukerecepten
from .lifestyleofafoodie import LifestyleOfAFoodie
from .littlespicejar import LittleSpiceJar
from .littlesunnykitchen import LittleSunnyKitchen
from .livelytable import LivelyTable
from .lovingitvegan import Lovingitvegan
from .maangchi import Maangchi
from .madensverden import MadensVerden
from .madsvin import Madsvin
from .marmiton import Marmiton
from .marthastewart import MarthaStewart
from .matprat import Matprat
from .mccormick import McCormick
from .meljoulwan import Meljoulwan
from .melskitchencafe import MelsKitchenCafe
from .miljuschka import Miljuschka
from .mindmegette import Mindmegette
from .minimalistbaker import Minimalistbaker
from .ministryofcurry import MinistryOfCurry
from .misya import Misya
from .mob import Mob
from .mobkitchen import MobKitchen
from .modernhoney import ModernHoney
from .momontimeout import MomOnTimeout
from .momswithcrockpots import MomsWithCrockPots
from .motherthyme import MotherThyme
from .moulinex import Moulinex
from .mundodereceitasbimby import MundoDeReceitasBimby
from .mybakingaddiction import MyBakingAddiction
from .myjewishlearning import MyJewishLearning
from .mykitchen101 import MyKitchen101
from .mykitchen101en import MyKitchen101en
from .mykoreankitchen import MyKoreanKitchen
from .myrecipes import MyRecipes
from .myvegetarianroots import MyVegetarianRoots
from .nhshealthierfamilies import NHSHealthierFamilies
from .nibbledish import NibbleDish
from .nihhealthyeating import NIHHealthyEating
from .norecipes import NoRecipes
from .nosalty import NoSalty
from .notenoughcinnamon import NotEnoughCinnamon
from .nourishedbynutrition import NourishedByNutrition
from .nrkmat import NRKMat
from .number2pencil import Number2Pencil
from .nutritionbynathalie import NutritionByNathalie
from .nutritionfacts import NutritionFacts
from .nytimes import NYTimes
from .ohsheglows import OhSheGlows
from .omnivorescookbook import OmnivoresCookbook
from .onceuponachef import OnceUponAChef
from .onehundredonecookbooks import OneHundredOneCookBooks
from .onesweetappetite import OneSweetAppetite
from .ottolenghibooks import OttolenghiBooks
from .owenhan import OwenHan
from .paleorunningmomma import PaleoRunningMomma
from .panelinha import Panelinha
from .paninihappy import PaniniHappy
from .peelwithzeal import PeelWithZeal
from .persnicketyplates import PersnicketyPlates
from .pickuplimes import PickUpLimes
from .pinchofyum import PinchOfYum
from .pingodoce import PingoDoce
from .pinkowlkitchen import PinkOwlKitchen
from .platingpixels import PlatingPixels
from .plowingthroughlife import PlowingThroughLife
from .popsugar import PopSugar
from .potatorolls import PotatoRolls
from .practicalselfreliance import PracticalSelfReliance
from .pressureluckcooking import PressureLuckCooking
from .primaledgehealth import PrimalEdgeHealth
from .projectgezond import ProjectGezond
from .przepisy import Przepisy
from .purelypope import PurelyPope
from .purplecarrot import PurpleCarrot
from .rachlmansfield import RachlMansfield
from .rainbowplantlife import RainbowPlantLife
from .realfoodtesco import RealFoodTesco
from .realsimple import RealSimple
from .receitasnestlebr import ReceitasNestleBR
from .recept import Recept
from .receptyprevas import ReceptyPreVas
from .recipegirl import RecipeGirl
from .reciperunner import RecipeRunner
from .recipetineats import RecipeTinEats
from .redhousespice import RedHouseSpice
from .reishunger import Reishunger
from .rezeptwelt import Rezeptwelt
from .ricetta import Ricetta
from .ricetteperbimby import RicettePerBimby
from .rosannapansino import RosannaPansino
from .rutgerbakt import RutgerBakt
from .saboresajinomoto import SaboresAjinomoto
from .sallysbakingaddiction import SallysBakingAddiction
from .sallysblog import SallysBlog
from .saltpepperskillet import SaltPepperSkillet
from .sandwhichtribunal import SandwhichTribunal
from .saveur import Saveur
from .savorynothings import SavoryNothings
from .seriouseats import SeriousEats
from .simpleveganista import SimpleVeganista
from .simplycookit import SimplyCookit
from .simplyquinoa import SimplyQuinoa
from .simplyrecipes import SimplyRecipes
from .simplywhisked import SimplyWhisked
from .skinnytaste import SkinnyTaste
from .smulweb import Smulweb
from .sobors import SoBors
from .southerncastiron import SouthernCastIron
from .southernliving import SouthernLiving
from .spendwithpennies import SpendWithPennies
from .springlane import Springlane
from .staysnatched import StaySnatched
from .steamykitchen import SteamyKitchen
from .streetkitchen import StreetKitchen
from .strongrfastr import StrongrFastr
from .sunbasket import SunBasket
from .sundpaabudget import SundPaaBudget
from .sunset import Sunset
from .sweetcsdesigns import SweetCsDesigns
from .sweetpeasandsaffron import SweetPeasAndSaffron
from .tasteatlas import TasteAtlas
from .tasteau import TasteAU
from .tasteofhome import TasteOfHome
from .tastesbetterfromscratch import TastesBetterFromScratch
from .tastesoflizzyt import TastesOfLizzyT
from .tasty import Tasty
from .tastykitchen import TastyKitchen
from .theclevercarrot import TheCleverCarrot
from .thecookierookie import TheCookieRookie
from .thecookingguy import TheCookingGuy
from .theexpertguides import TheExpertGuides
from .theglutenfreeaustrian import TheGlutenFreeAustrian
from .thehappyfoodie import TheHappyFoodie
from .thekitchencommunity import TheKitchenCommunity
from .thekitchenmagpie import TheKitchenMagPie
from .thekitchn import TheKitchn
from .theloopywhisk import TheLoopyWhisk
from .themagicalslowcooker import TheMagicalSlowCooker
from .themodernproper import TheModernProper
from .thepalatablelife import ThePalatableLife
from .thepioneerwoman import ThePioneerWoman
from .therecipecritic import Therecipecritic
from .thesaltymarshmallow import TheSaltyMarshmallow
from .thespruceeats import TheSpruceEats
from .thevintagemixer import TheVintageMixer
from .thewoksoflife import Thewoksoflife
from .thinlicious import Thinlicious
from .tidymom import TidyMom
from .timesofindia import TimesOfIndia
from .tineno import TineNo
from .tofoo import Tofoo
from .tudogostoso import TudoGostoso
from .twopeasandtheirpod import TwoPeasAndTheirPod
from .uitpaulineskeukennl import UitPaulinesKeukenNL
from .unsophisticook import Unsophisticook
from .usapears import USAPears
from .usdamyplate import USDAMyPlate
from .valdemarsro import Valdemarsro
from .vanillaandbean import VanillaAndBean
from .varechapravdask import VarechaPravdaSK
from .vegetarbloggen import Vegetarbloggen
from .vegolosi import Vegolosi
from .vegrecipesofindia import VegRecipesOfIndia
from .waitrose import Waitrose
from .watchwhatueat import WatchWhatUEat
from .wearenotmartha import WeAreNotMartha
from .weightwatchers import WeightWatchers
from .weightwatcherspublic import WeightWatchersPublic
from .wellplated import WellPlated
from .whatsgabycooking import WhatsGabyCooking
from .whole30 import Whole30
from .wholefoods import WholeFoods
from .wikicookbook import WikiCookbook
from .williamssonoma import WilliamsSonoma
from .womensweeklyfood import WomensWeeklyFood
from .woop import Woop
from .yemek import Yemek
from .yummly import Yummly
from .zaubertopf import ZauberTopf
from .zeitwochenmarkt import ZeitWochenmarkt
from .zenbelly import ZenBelly

SCRAPERS = {
    ACoupleCooks.host(): ACoupleCooks,
    AFlavorJournal.host(): AFlavorJournal,
    ALittleBitYummy.host(): ALittleBitYummy,
    AberleHome.host(): AberleHome,
    Abril.host(): Abril,
    AbuelasCounter.host(): AbuelasCounter,
    AddAPinch.host(): AddAPinch,
    AfghanKitchenRecipes.host(): AfghanKitchenRecipes,
    AkisPetretzikis.host(): AkisPetretzikis,
    AlbertHeijn.host(): AlbertHeijn,
    Aldi.host(): Aldi,
    AlexandraCooks.host(): AlexandraCooks,
    AllRecipes.host(): AllRecipes,
    AllTheHealthyThings.host(): AllTheHealthyThings,
    AllTomat.host(): AllTomat,
    AltonBrown.host(): AltonBrown,
    AmazingRibs.host(): AmazingRibs,
    AmbitiousKitchen.host(): AmbitiousKitchen,
    AmericasTestKitchen.host(): AmericasTestKitchen,
    ArchanasKitchen.host(): ArchanasKitchen,
    Argiro.host(): Argiro,
    Arla.host(): Arla,
    AtelierDesChefs.host(): AtelierDesChefs,
    AverieCooks.host(): AverieCooks,
    BBCFood.host(): BBCFood,
    BBCFood.host(domain="co.uk"): BBCFood,
    BBCGoodFood.host(): BBCGoodFood,
    Bakels.host(): Bakels,
    Bakels.host(domain="co.uk"): Bakels,
    BakingSense.host(): BakingSense,
    BakingMischief.host(): BakingMischief,
    BareFootContessa.host(): BareFootContessa,
    BarefeetInTheKitchen.host(): BarefeetInTheKitchen,
    BestRecipes.host(): BestRecipes,
    BettyBossi.host(): BettyBossi,
    BettyCrocker.host(): BettyCrocker,
    BiancaZapatka.host(): BiancaZapatka,
    BigOven.host(): BigOven,
    BlueApron.host(): BlueApron,
    BlueJeanChef.host(): BlueJeanChef,
    Bodybuilding.host(): Bodybuilding,
    BonAppetit.host(): BonAppetit,
    BowlOfDelicious.host(): BowlOfDelicious,
    BongEats.host(): BongEats,
    Breadtopia.host(): Breadtopia,
    BricelEtBaklava.host(): BricelEtBaklava,
    BudgetBytes.host(): BudgetBytes,
    CafeDelites.host(): CafeDelites,
    CarlsBadCravings.host(): CarlsBadCravings,
    CastIronKeto.host(): CastIronKeto,
    CdKitchen.host(): CdKitchen,
    CelebratingSweets.host(): CelebratingSweets,
    ChefSavvy.host(): ChefSavvy,
    Chefkoch.host(): Chefkoch,
    Chefnini.host(): Chefnini,
    ClosetCooking.host(): ClosetCooking,
    ComidinhasDoChef.host(): ComidinhasDoChef,
    CookEatShare.host(): CookEatShare,
    CookPad.host(): CookPad,
    CookTalk.host(): CookTalk,
    CookieAndKate.host(): CookieAndKate,
    CookingCircle.host(): CookingCircle,
    CookingLight.host(): CookingLight,
    CooksCountry.host(): CooksCountry,
    CooksIllustrated.host(): CooksIllustrated,
    CopyKat.host(): CopyKat,
    Costco.host(): Costco,
    CountryLiving.host(): CountryLiving,
    CreativeCanning.host(): CreativeCanning,
    Cucchiaio.host(): Cucchiaio,
    CuisineAZ.host(): CuisineAZ,
    Cybercook.host(): Cybercook,
    DamnDelicious.host(): DamnDelicious,
    DavidLebovitz.host(): DavidLebovitz,
    Delish.host(): Delish,
    DinnerAtTheZoo.host(): DinnerAtTheZoo,
    DinnerThenDessert.host(): DinnerThenDessert,
    Dishnz.host(): Dishnz,
    DobruChutAktualitySK.host(): DobruChutAktualitySK,
    DonalSkehan.host(): DonalSkehan,
    EatLiveRun.host(): EatLiveRun,
    EatThisMuch.host(): EatThisMuch,
    ElaVegan.host(): ElaVegan,
    EvolvingTable.host(): EvolvingTable,
    FamilyfoodOnTheTable.host(): FamilyfoodOnTheTable,
    FifteenGram.host(): FifteenGram,
    FitSlowCookerQueen.host(): FitSlowCookerQueen,
    GlutenFreeOnAShoeString.host(): GlutenFreeOnAShoeString,
    GourmetTraveller.host(): GourmetTraveller,
    GrandFrais.host(): GrandFrais,
    HeatherChristo.host(): HeatherChristo,
    InBloomBakery.host(): InBloomBakery,
    InGoodFlavor.host(): InGoodFlavor,
    JoCooks.host(): JoCooks,
    JoshuaWeissman.host(): JoshuaWeissman,
    JoyTheBaker.host(): JoyTheBaker,
    KaleJunkie.host(): KaleJunkie,
    KitchenAidAustralia.host(): KitchenAidAustralia,
    KitchenDreaming.host(): KitchenDreaming,
    KristinesKitchenBlog.host(): KristinesKitchenBlog,
    KuchynaLidla.host(): KuchynaLidla,
    LittleSunnyKitchen.host(): LittleSunnyKitchen,
    LeitesCulinaria.host(): LeitesCulinaria,
    McCormick.host(): McCormick,
    Miljuschka.host(): Miljuschka,
    ModernHoney.host(): ModernHoney,
    MomOnTimeout.host(): MomOnTimeout,
    Moulinex.host(): Moulinex,
    MundoDeReceitasBimby.host(): MundoDeReceitasBimby,
    MyJewishLearning.host(): MyJewishLearning,
    MyKoreanKitchen.host(): MyKoreanKitchen,
    MyVegetarianRoots.host(): MyVegetarianRoots,
    NotEnoughCinnamon.host(): NotEnoughCinnamon,
    NutritionFacts.host(): NutritionFacts,
    OneSweetAppetite.host(): OneSweetAppetite,
    OttolenghiBooks.host(): OttolenghiBooks,
    PeelWithZeal.host(): PeelWithZeal,
    PinchOfYum.host(): PinchOfYum,
    PotatoRolls.host(): PotatoRolls,
    Recept.host(): Recept,
    ReceptyPreVas.host(): ReceptyPreVas,
    RecipeGirl.host(): RecipeGirl,
    RicettePerBimby.host(): RicettePerBimby,
    SandwhichTribunal.host(): SandwhichTribunal,
    SavoryNothings.host(): SavoryNothings,
    StrongrFastr.host(): StrongrFastr,
    TasteAtlas.host(): TasteAtlas,
    TheCookieRookie.host(): TheCookieRookie,
    TheCookingGuy.host(): TheCookingGuy,
    TheGlutenFreeAustrian.host(): TheGlutenFreeAustrian,
    TheLoopyWhisk.host(): TheLoopyWhisk,
    ThePalatableLife.host(): ThePalatableLife,
    TheSaltyMarshmallow.host(): TheSaltyMarshmallow,
    Thinlicious.host(): Thinlicious,
    DomesticateMe.host(): DomesticateMe,
    Downshiftology.host(): Downshiftology,
    Dr.host(): Dr,
    EatWell101.host(): EatWell101,
    EatWhatTonight.host(): EatWhatTonight,
    EatingBirdFood.host(): EatingBirdFood,
    EatingWell.host(): EatingWell,
    Eatsmarter.host(): Eatsmarter,
    Eatsmarter.host(domain="de"): Eatsmarter,
    EatTolerant.host(): EatTolerant,
    EmmiKochtEinfach.host(): EmmiKochtEinfach,
    Epicurious.host(): Epicurious,
    ErrensKitchen.host(): ErrensKitchen,
    EthanChlebowski.host(): EthanChlebowski,
    FarmhouseDelivery.host(): FarmhouseDelivery,
    FarmhouseOnBoone.host(): FarmhouseOnBoone,
    FattoInCasaDaBenedetta.host(): FattoInCasaDaBenedetta,
    FelixKitchen.host(): FelixKitchen,
    FifteenSpatulas.host(): FifteenSpatulas,
    FineDiningLovers.host(): FineDiningLovers,
    FitMenCook.host(): FitMenCook,
    Food.host(): Food,
    Food52.host(): Food52,
    FoodAndWine.host(): FoodAndWine,
    FoodFidelity.host(): FoodFidelity,
    FoodNetwork.host(): FoodNetwork,
    FoodNetwork.host(domain="com"): FoodNetwork,
    FoodRepublic.host(): FoodRepublic,
    ForkToSpoon.host(): ForkToSpoon,
    ForksOverKnives.host(): ForksOverKnives,
    FranzoesischKochen.host(): FranzoesischKochen,
    G750g.host(): G750g,
    GialloZafferano.host(): GialloZafferano,
    GimmeSomeOven.host(): GimmeSomeOven,
    Globo.host(): Globo,
    Godt.host(): Godt,
    GonnaWantSeconds.host(): GonnaWantSeconds,
    GoodFoodDiscoveries.host(): GoodFoodDiscoveries,
    GoodHousekeeping.host(): GoodHousekeeping,
    GreatBritishChefs.host(): GreatBritishChefs,
    GrimGrains.host(): GrimGrains,
    GroupRecipes.host(): GroupRecipes,
    HEB.host(): HEB,
    HalfBakedHarvest.host(): HalfBakedHarvest,
    HandleTheHeat.host(): HandleTheHeat,
    HassanChef.host(): HassanChef,
    HeadbangersKitchen.host(): HeadbangersKitchen,
    HelloFresh.host(): HelloFresh,
    HelloFresh.host(domain="at"): HelloFresh,
    HelloFresh.host(domain="be"): HelloFresh,
    HelloFresh.host(domain="ca"): HelloFresh,
    HelloFresh.host(domain="ch"): HelloFresh,
    HelloFresh.host(domain="co.nz"): HelloFresh,
    HelloFresh.host(domain="co.uk"): HelloFresh,
    HelloFresh.host(domain="com.au"): HelloFresh,
    HelloFresh.host(domain="de"): HelloFresh,
    HelloFresh.host(domain="dk"): HelloFresh,
    HelloFresh.host(domain="es"): HelloFresh,
    HelloFresh.host(domain="fr"): HelloFresh,
    HelloFresh.host(domain="ie"): HelloFresh,
    HelloFresh.host(domain="it"): HelloFresh,
    HelloFresh.host(domain="lu"): HelloFresh,
    HelloFresh.host(domain="nl"): HelloFresh,
    HelloFresh.host(domain="no"): HelloFresh,
    HelloFresh.host(domain="se"): HelloFresh,
    HersheyLand.host(): HersheyLand,
    HomeChef.host(): HomeChef,
    Hostthetoast.host(): Hostthetoast,
    Ica.host(): Ica,
    ImWorthy.host(): ImWorthy,
    IG.host(): IG,
    IndianHealthyRecipes.host(): IndianHealthyRecipes,
    Innit.host(): Innit,
    InsanelyGoodRecipes.host(): InsanelyGoodRecipes,
    Inspiralized.host(): Inspiralized,
    IzzyCooking.host(): IzzyCooking,
    JamieOliver.host(): JamieOliver,
    JimCooksFoodGood.host(): JimCooksFoodGood,
    Joyfoodsunshine.host(): Joyfoodsunshine,
    JulieGoodwin.host(): JulieGoodwin,
    JustATaste.host(): JustATaste,
    JustBento.host(): JustBento,
    JustOneCookbook.host(): JustOneCookbook,
    KennyMcGovern.host(): KennyMcGovern,
    KeukenLiefdeNL.host(): KeukenLiefdeNL,
    KingArthur.host(): KingArthur,
    KitchenStories.host(): KitchenStories,
    KitchenSanctuary.host(): KitchenSanctuary,
    Kochbar.host(): Kochbar,
    Kochbucher.host(): Kochbucher,
    Koket.host(): Koket,
    KuchniaDomowa.host(): KuchniaDomowa,
    KwestiaSmaku.host(): KwestiaSmaku,
    LAtelierDeRoxane.host(): LAtelierDeRoxane,
    LeCremeDeLaCrumb.host(): LeCremeDeLaCrumb,
    LeanAndGreenRecipes.host(): LeanAndGreenRecipes,
    Lecker.host(): Lecker,
    LekkerEnSimpel.host(): LekkerEnSimpel,
    Leukerecepten.host(): Leukerecepten,
    LifestyleOfAFoodie.host(): LifestyleOfAFoodie,
    LittleSpiceJar.host(): LittleSpiceJar,
    LivelyTable.host(): LivelyTable,
    Lovingitvegan.host(): Lovingitvegan,
    Maangchi.host(): Maangchi,
    MadensVerden.host(): MadensVerden,
    Madsvin.host(): Madsvin,
    Marmiton.host(): Marmiton,
    MarthaStewart.host(): MarthaStewart,
    Matprat.host(): Matprat,
    Meljoulwan.host(): Meljoulwan,
    MelsKitchenCafe.host(): MelsKitchenCafe,
    Mindmegette.host(): Mindmegette,
    Minimalistbaker.host(): Minimalistbaker,
    MinistryOfCurry.host(): MinistryOfCurry,
    Misya.host(): Misya,
    Mob.host(): Mob,
    MobKitchen.host(): MobKitchen,
    MomsWithCrockPots.host(): MomsWithCrockPots,
    MotherThyme.host(): MotherThyme,
    MyBakingAddiction.host(): MyBakingAddiction,
    MyKitchen101.host(): MyKitchen101,
    MyKitchen101en.host(): MyKitchen101en,
    MyRecipes.host(): MyRecipes,
    NRKMat.host(): NRKMat,
    NibbleDish.host(): NibbleDish,
    NHSHealthierFamilies.host(): NHSHealthierFamilies,
    NIHHealthyEating.host(): NIHHealthyEating,
    NYTimes.host(): NYTimes,
    NoRecipes.host(): NoRecipes,
    NoSalty.host(): NoSalty,
    NourishedByNutrition.host(): NourishedByNutrition,
    Number2Pencil.host(): Number2Pencil,
    NutritionByNathalie.host(): NutritionByNathalie,
    OhSheGlows.host(): OhSheGlows,
    OmnivoresCookbook.host(): OmnivoresCookbook,
    OnceUponAChef.host(): OnceUponAChef,
    OneHundredOneCookBooks.host(): OneHundredOneCookBooks,
    OwenHan.host(): OwenHan,
    PaleoRunningMomma.host(): PaleoRunningMomma,
    Panelinha.host(): Panelinha,
    PaniniHappy.host(): PaniniHappy,
    PersnicketyPlates.host(): PersnicketyPlates,
    PickUpLimes.host(): PickUpLimes,
    PingoDoce.host(): PingoDoce,
    PinkOwlKitchen.host(): PinkOwlKitchen,
    PlatingPixels.host(): PlatingPixels,
    PlowingThroughLife.host(): PlowingThroughLife,
    PopSugar.host(): PopSugar,
    PracticalSelfReliance.host(): PracticalSelfReliance,
    PressureLuckCooking.host(): PressureLuckCooking,
    PrimalEdgeHealth.host(): PrimalEdgeHealth,
    ProjectGezond.host(): ProjectGezond,
    Przepisy.host(): Przepisy,
    PurelyPope.host(): PurelyPope,
    PurpleCarrot.host(): PurpleCarrot,
    RachlMansfield.host(): RachlMansfield,
    RainbowPlantLife.host(): RainbowPlantLife,
    RealFoodTesco.host(): RealFoodTesco,
    RealSimple.host(): RealSimple,
    RealFoodTesco.host(): RealFoodTesco,
    ReceitasNestleBR.host(): ReceitasNestleBR,
    RecipeRunner.host(): RecipeRunner,
    RecipeTinEats.host(): RecipeTinEats,
    RedHouseSpice.host(): RedHouseSpice,
    Reishunger.host(): Reishunger,
    Rezeptwelt.host(): Rezeptwelt,
    Ricetta.host(): Ricetta,
    RosannaPansino.host(): RosannaPansino,
    RutgerBakt.host(): RutgerBakt,
    SaboresAjinomoto.host(): SaboresAjinomoto,
    SallysBakingAddiction.host(): SallysBakingAddiction,
    SallysBlog.host(): SallysBlog,
    SaltPepperSkillet.host(): SaltPepperSkillet,
    Saveur.host(): Saveur,
    SeriousEats.host(): SeriousEats,
    SimpleVeganista.host(): SimpleVeganista,
    SimplyCookit.host(): SimplyCookit,
    SimplyQuinoa.host(): SimplyQuinoa,
    SimplyRecipes.host(): SimplyRecipes,
    SimplyWhisked.host(): SimplyWhisked,
    SkinnyTaste.host(): SkinnyTaste,
    Smulweb.host(): Smulweb,
    SoBors.host(): SoBors,
    SouthernCastIron.host(): SouthernCastIron,
    SouthernLiving.host(): SouthernLiving,
    SpendWithPennies.host(): SpendWithPennies,
    Springlane.host(): Springlane,
    StaySnatched.host(): StaySnatched,
    SteamyKitchen.host(): SteamyKitchen,
    StreetKitchen.host(): StreetKitchen,
    SunBasket.host(): SunBasket,
    SundPaaBudget.host(): SundPaaBudget,
    Sunset.host(): Sunset,
    SweetCsDesigns.host(): SweetCsDesigns,
    SweetPeasAndSaffron.host(): SweetPeasAndSaffron,
    TasteAU.host(): TasteAU,
    TasteOfHome.host(): TasteOfHome,
    TastesBetterFromScratch.host(): TastesBetterFromScratch,
    TastesOfLizzyT.host(): TastesOfLizzyT,
    Tasty.host(): Tasty,
    TastyKitchen.host(): TastyKitchen,
    TheCleverCarrot.host(): TheCleverCarrot,
    TheExpertGuides.host(): TheExpertGuides,
    TheHappyFoodie.host(): TheHappyFoodie,
    TheKitchenCommunity.host(): TheKitchenCommunity,
    TheKitchenMagPie.host(): TheKitchenMagPie,
    TheKitchn.host(): TheKitchn,
    TheMagicalSlowCooker.host(): TheMagicalSlowCooker,
    TheModernProper.host(): TheModernProper,
    ThePioneerWoman.host(): ThePioneerWoman,
    TheSpruceEats.host(): TheSpruceEats,
    TheVintageMixer.host(): TheVintageMixer,
    Therecipecritic.host(): Therecipecritic,
    Thewoksoflife.host(): Thewoksoflife,
    TidyMom.host(): TidyMom,
    TimesOfIndia.host(): TimesOfIndia,
    TineNo.host(): TineNo,
    Tofoo.host(): Tofoo,
    TudoGostoso.host(): TudoGostoso,
    TwoPeasAndTheirPod.host(): TwoPeasAndTheirPod,
    USAPears.host(): USAPears,
    USDAMyPlate.host(): USDAMyPlate,
    Unsophisticook.host(): Unsophisticook,
    Valdemarsro.host(): Valdemarsro,
    VanillaAndBean.host(): VanillaAndBean,
    VarechaPravdaSK.host(): VarechaPravdaSK,
    VegRecipesOfIndia.host(): VegRecipesOfIndia,
    Vegetarbloggen.host(): Vegetarbloggen,
    Vegolosi.host(): Vegolosi,
    Waitrose.host(): Waitrose,
    WatchWhatUEat.host(): WatchWhatUEat,
    WeAreNotMartha.host(): WeAreNotMartha,
    WeightWatchers.host(): WeightWatchers,
    WeightWatchersPublic.host(): WeightWatchersPublic,
    WellPlated.host(): WellPlated,
    WhatsGabyCooking.host(): WhatsGabyCooking,
    Whole30.host(): Whole30,
    WholeFoods.host(): WholeFoods,
    WholeFoods.host(domain="co.uk"): WholeFoods,
    WilliamsSonoma.host(): WilliamsSonoma,
    WomensWeeklyFood.host(): WomensWeeklyFood,
    Woop.host(): Woop,
    WikiCookbook.host(): WikiCookbook,
    Yemek.host(): Yemek,
    Yummly.host(): Yummly,
    ZauberTopf.host(): ZauberTopf,
    ZeitWochenmarkt.host(): ZeitWochenmarkt,
    ZenBelly.host(): ZenBelly,
    GesundAktiv.host(): GesundAktiv,
    UitPaulinesKeukenNL.host(): UitPaulinesKeukenNL,
}


def get_supported_urls() -> set[str]:
    return set(SCRAPERS.keys())


def scraper_exists_for(url_path: str) -> bool:
    host_name = get_host_name(url_path)
    return host_name in get_supported_urls()


def scrape_html(
    html: str | None,
    org_url: str,
    *,
    online: bool = False,
    supported_only: bool | None = None,
    wild_mode: bool | None = None,
) -> AbstractScraper:
    """
    Accepts optional HTML and a required URL as input, and returns a scraper object.

    HTML is required unless the 'online' flag is enabled, allowing the library
    to download a current copy of the recipe.

    If the 'supported_only' flag is enabled (the default), then only websites
    that are known to be supported by the library (as determined by their
    domain name) will return scrapers.  When disabled, the library will attempt
    to retrieve generic schema.org recipe metadata from the HTML.

    Args:
        html (str | None): HTML of the recipe webpage.
        org_url (str): URL of the recipe.

    Kwargs:
        online (bool): whether the library may download HTML.
        supported_only (bool | None): whether to restrict to supported domains.
        wild_mode (bool | None): deprecated: whether to attempt scraping unsupported domains.

    Raises:
        ElementNotFoundInHtml: Retrieval of data failed because an HTML element was not found.
        FieldNotProvidedByWebsiteException: This website doesn't seem to provide the requested field.
        NoSchemaFoundInWildMode: When no schema is found for an unsupported domain.
        StaticValueException: Wraps a static/constant value that was not retrieved dynamically.
        WebsiteNotImplementedError: When the recipe URL does not match any supported domains.

    Returns:
        AbstractScraper: a scraper instance implementing AbstractScraper for the requested website.
    """
    if wild_mode is not None:
        msg = "The 'wild_mode' parameter is deprecated and may be removed in future."
        if wild_mode is True:
            msg += "\n\n"
            msg += "Please pass 'supported_only=False' instead for similar behaviour."
        warnings.warn(msg, category=DeprecationWarning)

    if online:
        msg = "The 'online' parameter is deprecated and will be removed in future."
        msg += "\n\n"
        msg += "Please use an HTTP client (such as 'requests' or 'httpx') to "
        msg += "retrieve the recipe's HTML from the URL instead."
        warnings.warn(msg, category=DeprecationWarning)

    if supported_only is not None and wild_mode is not None:
        msg = "Please provide either 'supported_only' or 'wild_mode', but not both."
        raise ValueError(msg)
    elif supported_only is None and wild_mode is not None:
        supported_only = not bool(wild_mode)  # wild: true -> supported_only: false

    if html is None and online is True:
        if requests_import_error is not None:
            msg = (
                "Unable to import the 'requests' library for use when recipe-scrapers \n"
                "is operating online.\n"
                "Did you install using 'pip install recipe-scrapers[online]'?"
            )
            raise ImportError(msg) from requests_import_error

        try:
            html = requests.get(url=org_url, headers=HEADERS).text
        except Exception as e:
            raise Exception(f"Failed to retrieve HTML content from {org_url}.") from e

    if html is None and online is False:
        msg = (
            "No HTML input was provided to scrape from, and none can be retrieved from \n"
            "the web because the 'online' flag is false."
        )
        raise ValueError(msg)

    host_name = get_host_name(org_url)
    if host_name in SCRAPERS:
        return SCRAPERS[host_name](html=html, url=org_url)

    if supported_only in (None, True):
        msg = (
            f"The website '{host_name}' isn't currently supported by recipe-scrapers!\n"
            "---\n"
            "If you have time to help us out, please report this as a feature \n"
            "request on our bugtracker."
        )
        raise WebsiteNotImplementedError(msg)

    schema_scraper = SchemaScraperFactory.generate(html=html, url=org_url)
    if schema_scraper.schema.data:
        return schema_scraper

    raise NoSchemaFoundInWildMode(org_url)
