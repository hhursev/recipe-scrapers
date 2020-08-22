import inspect
import re
from tldextract import TLDExtract

from .allrecipes import AllRecipes
from .acouplecooks import ACoupleCooks
from .archanaskitchen import ArchanasKitchen
from .averiecooks import AverieCooks
from .bbcfood import BBCFood
from .bbcgoodfood import BBCGoodFood
from .bettycrocker import BettyCrocker
from .bonappetit import BonAppetit
from .bowlofdelicious import BowlOfDelicious
from .budgetbytes import BudgetBytes
from .closetcooking import ClosetCooking
from .cookieandkate import CookieAndKate
from .cookpad import CookPad
from .cookstr import Cookstr
from .copykat import CopyKat
from .countryliving import CountryLiving
from .cybercook import Cybercook
from .delish import Delish
from .epicurious import Epicurious
from .fifteenspatulas import FifteenSpatulas
from .finedininglovers import FineDiningLovers
from .fitmencook import FitMenCook
from .food import Food
from .foodnetwork import FoodNetwork
from .foodrepublic import FoodRepublic
from .geniuskitchen import GeniusKitchen
from .giallozafferano import GialloZafferano
from .gimmesomeoven import GimmeSomeOven
from .gonnawantseconds import GonnaWantSeconds
from .gousto import Gousto
from .greatbritishchefs import GreatBritishChefs
from .halfbakedharvest import HalfBakedHarvest
from .heinzbrasil import HeinzBrasil
from .hellofresh import HelloFresh
from .hostthetoast import Hostthetoast
from .hundredandonecookbooks import HundredAndOneCookbooks
from .ig import IG
from .inspiralized import Inspiralized
from .jamieoliver import JamieOliver
from .justbento import JustBento
from .kennymcgovern import KennyMcGovern
from .kochbar import Kochbar
from .lecremedelacrumb import LeCremeDeLaCrumb
from .lovingitvegan import Lovingitvegan
from .marmiton import Marmiton
from .matprat import Matprat
from .mindmegette import Mindmegette
from .minimalistbaker import Minimalistbaker
from .misya import Misya
from .momswithcrockpots import MomsWithCrockPots
from .motherthyme import MotherThyme
from .mybakingaddiction import MyBakingAddiction
from .myrecipes import MyRecipes
from .nihhealthyeating import NIHHealthyEating
from .nytimes import NYTimes
from .ohsheglows import OhSheGlows
from .panelinha import Panelinha
from .paninihappy import PaniniHappy
from .przepisy import Przepisy
from .realsimple import RealSimple
from .seriouseats import SeriousEats
from .simplyquinoa import SimplyQuinoa
from .simplyrecipes import SimplyRecipes
from .skinnytaste import SkinnyTaste
from .southernliving import SouthernLiving
from .spendwithpennies import SpendWithPennies
from .steamykitchen import SteamyKitchen
from .tastesoflizzyt import TastesOfLizzyT
from .tasteofhome import TasteOfHome
from .tasty import Tasty
from .tastykitchen import TastyKitchen
from .thehappyfoodie import TheHappyFoodie
from .thekitchn import TheKitchn
from .thepioneerwoman import ThePioneerWoman
from .thespruceeats import TheSpruceEats
from .thevintagemixer import TheVintageMixer
from .thewoksoflife import Thewoksoflife
from .tineno import TineNo
from .tudogostoso import TudoGostoso
from .twopeasandtheirpod import TwoPeasAndTheirPod
from .vegolosi import Vegolosi
from .watchwhatueat import WatchWhatUEat
from .whatsgabycooking import WhatsGabyCooking
from .wikicookbook import WikiCookbook
from .yummly import Yummly

SCRAPERS = {
    ACoupleCooks.host(): ACoupleCooks,
    AllRecipes.host(): AllRecipes,
    ArchanasKitchen.host(): ArchanasKitchen,
    AverieCooks.host(): AverieCooks,
    BBCFood.host(): BBCFood,
    BBCFood.host(domain="co.uk"): BBCFood,
    BBCGoodFood.host(): BBCGoodFood,
    BettyCrocker.host(): BettyCrocker,
    BonAppetit.host(): BonAppetit,
    BowlOfDelicious.host(): BowlOfDelicious,
    BudgetBytes.host(): BudgetBytes,
    ClosetCooking.host(): ClosetCooking,
    CookieAndKate.host(): CookieAndKate,
    CookPad.host(): CookPad,
    Cookstr.host(): Cookstr,
    CopyKat.host(): CopyKat,
    CountryLiving.host(): CountryLiving,
    Cybercook.host(): Cybercook,
    Delish.host(): Delish,
    Epicurious.host(): Epicurious,
    FifteenSpatulas.host(): FifteenSpatulas,
    FineDiningLovers.host(): FineDiningLovers,
    FitMenCook.host(): FitMenCook,
    Food.host(): Food,
    FoodNetwork.host(): FoodNetwork,
    FoodRepublic.host(): FoodRepublic,
    GeniusKitchen.host(): GeniusKitchen,
    GialloZafferano.host(): GialloZafferano,
    GimmeSomeOven.host(): GimmeSomeOven,
    GonnaWantSeconds.host(): GonnaWantSeconds,
    Gousto.host(): Gousto,
    GreatBritishChefs.host(): GreatBritishChefs,
    HalfBakedHarvest.host(): HalfBakedHarvest,
    HeinzBrasil.host(): HeinzBrasil,
    HelloFresh.host(): HelloFresh,
    HelloFresh.host(domain="co.uk"): HelloFresh,
    HelloFresh.host(domain="de"): HelloFresh,
    Hostthetoast.host(): Hostthetoast,
    HundredAndOneCookbooks.host(): HundredAndOneCookbooks,
    IG.host(): IG,
    Inspiralized.host(): Inspiralized,
    JamieOliver.host(): JamieOliver,
    JustBento.host(): JustBento,
    KennyMcGovern.host(): KennyMcGovern,
    Kochbar.host(): Kochbar,
    LeCremeDeLaCrumb.host(): LeCremeDeLaCrumb,
    Lovingitvegan.host(): Lovingitvegan,
    TheKitchn.host(): TheKitchn,
    Marmiton.host(): Marmiton,
    Matprat.host(): Matprat,
    Mindmegette.host(): Mindmegette,
    Minimalistbaker.host(): Minimalistbaker,
    Misya.host(): Misya,
    MomsWithCrockPots.host(): MomsWithCrockPots,
    MotherThyme.host(): MotherThyme,
    MyBakingAddiction.host(): MyBakingAddiction,
    MyRecipes.host(): MyRecipes,
    NIHHealthyEating.host(): NIHHealthyEating,
    NYTimes.host(): NYTimes,
    OhSheGlows.host(): OhSheGlows,
    Panelinha.host(): Panelinha,
    PaniniHappy.host(): PaniniHappy,
    Przepisy.host(): Przepisy,
    RealSimple.host(): RealSimple,
    SeriousEats.host(): SeriousEats,
    SimplyQuinoa.host(): SimplyQuinoa,
    SimplyRecipes.host(): SimplyRecipes,
    SkinnyTaste.host(): SkinnyTaste,
    SouthernLiving.host(): SouthernLiving,
    SpendWithPennies.host(): SpendWithPennies,
    SteamyKitchen.host(): SteamyKitchen,
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
    Vegolosi.host(): Vegolosi,
    WatchWhatUEat.host(): WatchWhatUEat,
    WhatsGabyCooking.host(): WhatsGabyCooking,
    WikiCookbook.host(): WikiCookbook,
    Yummly.host(): Yummly,
}


def url_path_to_dict(path):
    pattern = (
        r"^"
        r"((?P<schema>.+?)://)?"
        r"((?P<user>.+?)(:(?P<password>.*?))?@)?"
        r"(?P<host>.*?)"
        r"(:(?P<port>\d+?))?"
        r"(?P<path>/.*?)?"
        r"(?P<query>[?].*?)?"
        r"$"
    )
    regex = re.compile(pattern)
    matches = regex.match(path)
    url_dict = matches.groupdict() if matches is not None else None

    return url_dict


class WebsiteNotImplementedError(NotImplementedError):
    """ Error for when the website is not supported by this library. """

    def __init__(self, domain):
        self.domain = domain

    def __str__(self):
        return "Website ({}) is not supported".format(self.domain)


def get_domain(url):
    tldextract = TLDExtract(suffix_list_urls=None)
    url_info = tldextract(url)
    return "{}.{}".format(url_info.domain, url_info.suffix)


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

    host_name = url_path_to_dict(url_path.replace("://www.", "://"))["host"]

    try:
        scraper = SCRAPERS[host_name]
    except KeyError:
        raise WebsiteNotImplementedError(host_name)

    return scraper(url_path, **options)


__all__ = ["scrape_me"]
name = "recipe_scrapers"
