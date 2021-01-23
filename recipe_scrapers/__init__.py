import inspect
from tld import get_tld

from ._factory import SchemaScraperFactory
from ._utils import get_host_name
from .abril import Abril
from .allrecipes import AllRecipes
from .amazingribs import AmazingRibs
from .ambitiouskitchen import AmbitiousKitchen
from .acouplecooks import ACoupleCooks
from .archanaskitchen import ArchanasKitchen
from .atelierdeschefs import AtelierDesChefs
from .averiecooks import AverieCooks
from .bakingmischeif import BakingMischeif
from .bbcfood import BBCFood
from .bbcgoodfood import BBCGoodFood
from .bettycrocker import BettyCrocker
from .blueapron import BlueApron
from .bonappetit import BonAppetit
from .bowlofdelicious import BowlOfDelicious
from .budgetbytes import BudgetBytes
from .cdkitchen import CdKitchen
from .chefkoch import Chefkoch
from .closetcooking import ClosetCooking
from .cookeatshare import CookEatShare
from .cookieandkate import CookieAndKate
from .cookpad import CookPad
from .cookstr import Cookstr
from .copykat import CopyKat
from .countryliving import CountryLiving
from .cuisineaz import CuisineAZ
from .cybercook import Cybercook
from .delish import Delish
from .domesticateme import DomesticateMe
from .downshiftology import Downshiftology
from .dr import Dr
from .eatingbirdfood import EatingBirdFood
from .eatsmarter import Eatsmarter
from .eatwhattonight import EatWhatTonight
from .epicurious import Epicurious
from .farmhousedelivery import FarmhouseDelivery
from .fifteenspatulas import FifteenSpatulas
from .finedininglovers import FineDiningLovers
from .fitmencook import FitMenCook
from .food import Food
from .foodandwine import FoodAndWine
from .foodnetwork import FoodNetwork
from .foodrepublic import FoodRepublic
from .g750g import G750g
from .geniuskitchen import GeniusKitchen
from .giallozafferano import GialloZafferano
from .gimmesomeoven import GimmeSomeOven
from .globo import Globo
from .gonnawantseconds import GonnaWantSeconds
from .gousto import Gousto
from .greatbritishchefs import GreatBritishChefs
from .halfbakedharvest import HalfBakedHarvest
from .hassenchef import Hassanchef
from .heb import HEB
from .heinzbrasil import HeinzBrasil
from .hellofresh import HelloFresh
from .hostthetoast import Hostthetoast
from .hundredandonecookbooks import HundredAndOneCookbooks
from .ig import IG
from .innit import Innit
from .inspiralized import Inspiralized
from .jamieoliver import JamieOliver
from .justbento import JustBento
from .kennymcgovern import KennyMcGovern
from .kingarthur import KingArthur
from .kochbar import Kochbar
from .kuchniadomowa import KuchniaDomowa
from .littlespicejar import LittleSpiceJar
from .livelytable import LivelyTable
from .lecremedelacrumb import LeCremeDeLaCrumb
from .lovingitvegan import Lovingitvegan
from .marmiton import Marmiton
from .matprat import Matprat
from .melskitchencafe import MelsKitchenCafe
from .mindmegette import Mindmegette
from .minimalistbaker import Minimalistbaker
from .misya import Misya
from .momswithcrockpots import MomsWithCrockPots
from .motherthyme import MotherThyme
from .mybakingaddiction import MyBakingAddiction
from .myrecipes import MyRecipes
from .nihhealthyeating import NIHHealthyEating
from .nourishedbynutrition import NourishedByNutrition
from .nutritionbynathalie import NutritionByNathalie
from .nytimes import NYTimes
from .ohsheglows import OhSheGlows
from .onehundredonecookbooks import OneHundredOneCookBooks
from .paleorunningmomma import PaleoRunningMomma
from .panelinha import Panelinha
from .paninihappy import PaniniHappy
from .popsugar import PopSugar
from .przepisy import Przepisy
from .purelypope import PurelyPope
from .purplecarrot import PurpleCarrot
from .rachlmansfield import RachlMansfield
from .realsimple import RealSimple
from .recipietineats import RecipieTinEats
from .seriouseats import SeriousEats
from .simplyquinoa import SimplyQuinoa
from .simplyrecipes import SimplyRecipes
from .simplywhisked import SimplyWhisked
from .skinnytaste import SkinnyTaste
from .southernliving import SouthernLiving
from .spendwithpennies import SpendWithPennies
from .spruceeats import SpruceEats
from .steamykitchen import SteamyKitchen
from .streetkitchen import StreetKitchen
from .sunbasket import SunBasket
from .sweetpeasandsaffron import SweetPeasAndSaffron
from .tastesoflizzyt import TastesOfLizzyT
from .tasteofhome import TasteOfHome
from .tasty import Tasty
from .tastykitchen import TastyKitchen
from .thehappyfoodie import TheHappyFoodie
from .thekitchn import TheKitchn
from .thenutritiouskitchen import TheNutritiousKitchen
from .thepioneerwoman import ThePioneerWoman
from .thespruceeats import TheSpruceEats
from .thevintagemixer import TheVintageMixer
from .thewoksoflife import Thewoksoflife
from .tineno import TineNo
from .tudogostoso import TudoGostoso
from .twopeasandtheirpod import TwoPeasAndTheirPod
from .vanillaandbean import VanillaAndBean
from .vegolosi import Vegolosi
from .vegrecipesofindia import VegRecipesOfIndia
from .watchwhatueat import WatchWhatUEat
from .whatsgabycooking import WhatsGabyCooking
from .wholefoods import WholeFoods
from .wikicookbook import WikiCookbook
from .yummly import Yummly


SCRAPERS = {
    Abril.host(): Abril,
    ACoupleCooks.host(): ACoupleCooks,
    AllRecipes.host(): AllRecipes,
    AmazingRibs.host(): AmazingRibs,
    AmbitiousKitchen.host(): AmbitiousKitchen,
    ArchanasKitchen.host(): ArchanasKitchen,
    AtelierDesChefs.host(): AtelierDesChefs,
    AverieCooks.host(): AverieCooks,
    BBCFood.host(): BBCFood,
    BBCFood.host(domain="co.uk"): BBCFood,
    BBCGoodFood.host(): BBCGoodFood,
    BakingMischeif.host(): BakingMischeif,
    BettyCrocker.host(): BettyCrocker,
    BlueApron.host(): BlueApron,
    BonAppetit.host(): BonAppetit,
    BowlOfDelicious.host(): BowlOfDelicious,
    BudgetBytes.host(): BudgetBytes,
    CdKitchen.host(): CdKitchen,
    Chefkoch.host(): Chefkoch,
    ClosetCooking.host(): ClosetCooking,
    CookEatShare.host(): CookEatShare,
    CookieAndKate.host(): CookieAndKate,
    CookPad.host(): CookPad,
    Cookstr.host(): Cookstr,
    CopyKat.host(): CopyKat,
    CountryLiving.host(): CountryLiving,
    CuisineAZ.host(): CuisineAZ,
    Cybercook.host(): Cybercook,
    Delish.host(): Delish,
    DomesticateMe.host(): DomesticateMe,
    Downshiftology.host(): Downshiftology,
    Dr.host(): Dr,
    EatingBirdFood.host(): EatingBirdFood,
    Eatsmarter.host(): Eatsmarter,
    Eatsmarter.host(domain="de"): Eatsmarter,
    EatWhatTonight.host(): EatWhatTonight,
    Epicurious.host(): Epicurious,
    FarmhouseDelivery.host(): FarmhouseDelivery,
    FifteenSpatulas.host(): FifteenSpatulas,
    FineDiningLovers.host(): FineDiningLovers,
    FitMenCook.host(): FitMenCook,
    Food.host(): Food,
    FoodAndWine.host(): FoodAndWine,
    FoodNetwork.host(): FoodNetwork,
    FoodRepublic.host(): FoodRepublic,
    G750g.host(): G750g,
    GeniusKitchen.host(): GeniusKitchen,
    GialloZafferano.host(): GialloZafferano,
    GimmeSomeOven.host(): GimmeSomeOven,
    Globo.host(): Globo,
    GonnaWantSeconds.host(): GonnaWantSeconds,
    Gousto.host(): Gousto,
    GreatBritishChefs.host(): GreatBritishChefs,
    HalfBakedHarvest.host(): HalfBakedHarvest,
    Hassanchef.host(): Hassanchef,
    HEB.host(): HEB,
    HeinzBrasil.host(): HeinzBrasil,
    HelloFresh.host(): HelloFresh,
    HelloFresh.host(domain="co.uk"): HelloFresh,
    HelloFresh.host(domain="de"): HelloFresh,
    Hostthetoast.host(): Hostthetoast,
    HundredAndOneCookbooks.host(): HundredAndOneCookbooks,
    IG.host(): IG,
    Innit.host(): Innit,
    Inspiralized.host(): Inspiralized,
    JamieOliver.host(): JamieOliver,
    JustBento.host(): JustBento,
    KennyMcGovern.host(): KennyMcGovern,
    KingArthur.host(): KingArthur,
    Kochbar.host(): Kochbar,
    KuchniaDomowa.host(): KuchniaDomowa,
    LittleSpiceJar.host(): LittleSpiceJar,
    LivelyTable.host(): LivelyTable,
    LeCremeDeLaCrumb.host(): LeCremeDeLaCrumb,
    Lovingitvegan.host(): Lovingitvegan,
    OneHundredOneCookBooks.host(): OneHundredOneCookBooks,
    PaleoRunningMomma.host(): PaleoRunningMomma,
    RachlMansfield.host(): RachlMansfield,
    SpruceEats.host(): SpruceEats,
    TheKitchn.host(): TheKitchn,
    TheNutritiousKitchen.host(): TheNutritiousKitchen,
    Marmiton.host(): Marmiton,
    Matprat.host(): Matprat,
    MelsKitchenCafe.host(): MelsKitchenCafe,
    Mindmegette.host(): Mindmegette,
    Minimalistbaker.host(): Minimalistbaker,
    Misya.host(): Misya,
    MomsWithCrockPots.host(): MomsWithCrockPots,
    MotherThyme.host(): MotherThyme,
    MyBakingAddiction.host(): MyBakingAddiction,
    MyRecipes.host(): MyRecipes,
    NIHHealthyEating.host(): NIHHealthyEating,
    NourishedByNutrition.host(): NourishedByNutrition,
    NutritionByNathalie.host(): NutritionByNathalie,
    NYTimes.host(): NYTimes,
    OhSheGlows.host(): OhSheGlows,
    Panelinha.host(): Panelinha,
    PaniniHappy.host(): PaniniHappy,
    PopSugar.host(): PopSugar,
    Przepisy.host(): Przepisy,
    PurelyPope.host(): PurelyPope,
    PurpleCarrot.host(): PurpleCarrot,
    RealSimple.host(): RealSimple,
    RecipieTinEats.host(): RecipieTinEats,
    SeriousEats.host(): SeriousEats,
    SimplyQuinoa.host(): SimplyQuinoa,
    SimplyRecipes.host(): SimplyRecipes,
    SimplyWhisked.host(): SimplyWhisked,
    SkinnyTaste.host(): SkinnyTaste,
    SouthernLiving.host(): SouthernLiving,
    SpendWithPennies.host(): SpendWithPennies,
    SteamyKitchen.host(): SteamyKitchen,
    StreetKitchen.host(): StreetKitchen,
    SunBasket.host(): SunBasket,
    SweetPeasAndSaffron.host(): SweetPeasAndSaffron,
    TastesOfLizzyT.host(): TastesOfLizzyT,
    TasteOfHome.host(): TasteOfHome,
    Tasty.host(): Tasty,
    TastyKitchen.host(): TastyKitchen,
    TheHappyFoodie.host(): TheHappyFoodie,
    ThePioneerWoman.host(): ThePioneerWoman,
    TheSpruceEats.host(): TheSpruceEats,
    TheVintageMixer.host(): TheVintageMixer,
    Thewoksoflife.host(): Thewoksoflife,
    TineNo.host(): TineNo,
    TudoGostoso.host(): TudoGostoso,
    TwoPeasAndTheirPod.host(): TwoPeasAndTheirPod,
    VanillaAndBean.host(): VanillaAndBean,
    VegRecipesOfIndia.host(): VegRecipesOfIndia,
    Vegolosi.host(): Vegolosi,
    WatchWhatUEat.host(): WatchWhatUEat,
    WhatsGabyCooking.host(): WhatsGabyCooking,
    WholeFoods.host(): WholeFoods,
    WholeFoods.host(domain="co.uk"): WholeFoods,
    WikiCookbook.host(): WikiCookbook,
    Yummly.host(): Yummly,
}


class WebsiteNotImplementedError(NotImplementedError):
    """ Error when website is not supported by this library. """

    def __init__(self, domain):
        self.domain = domain

    def __str__(self):
        return f"Website ({self.domain}) is not supported"


class NoSchemaFoundInWildMode(Exception):
    """ Error when wild_mode fails to locate schema at the url """

    def __init__(self, url):
        self.url = url

    def __str__(self):
        return f"No Recipe Schema found at {self.url}"


def get_domain(url):
    url_info = get_tld(url, as_object=True, search_private=False)
    return url_info.fld


def harvest(url, **options):
    domain = get_domain(url)
    if domain not in SCRAPERS:
        raise WebsiteNotImplementedError(domain)

    scraper = SCRAPERS[domain]
    options = {
        option: value
        for option, value in options.items()
        if option in inspect.signature(scraper).parameters
    }
    return scraper(url, **options)


def scrape_me(url_path, **options):
    host_name = (
        get_host_name(url_path) if not options.get("test", False) else "test_wild_mode"
    )

    try:
        scraper = SCRAPERS[host_name]
    except KeyError:
        if options.get("wild_mode", False):
            wild_scraper = SchemaScraperFactory.generate(url_path, **options)
            if not wild_scraper.schema.data:
                raise NoSchemaFoundInWildMode(url_path)
            return wild_scraper
        else:
            raise WebsiteNotImplementedError(host_name)

    return scraper(url_path, **options)


__all__ = ["scrape_me"]
name = "recipe_scrapers"
