import inspect
import re
from tldextract import TLDExtract

from .allrecipes import AllRecipes
from .archanaskitchen import ArchanasKitchen
from .bbcfood import BBCFood
from .bbcgoodfood import BBCGoodFood
from .bettycrocker import BettyCrocker
from .bonappetit import BonAppetit
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
from .finedininglovers import FineDiningLovers
from .fitmencook import FitMenCook
from .food import Food
from .foodnetwork import FoodNetwork
from .foodrepublic import FoodRepublic
from .giallozafferano import GialloZafferano
from .gonnawantseconds import GonnaWantSeconds
from .gousto import Gousto
from .greatbritishchefs import GreatBritishChefs
from .heinzbrasil import HeinzBrasil
from .hellofresh import HelloFresh
from .hundredandonecookbooks import HundredAndOneCookbooks
from .ig import IG
from .inspiralized import Inspiralized
from .jamieoliver import JamieOliver
from .justbento import JustBento
from .kennymcgovern import KennyMcGovern
from .thekitchn import TheKitchn
from .marmiton import Marmiton
from .matprat import Matprat
from .mindmegette import Mindmegette
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
from .southernliving import SouthernLiving
from .steamykitchen import SteamyKitchen
from .tastesoflizzyt import TastesOfLizzyT
from .tastykitchen import TastyKitchen
from .thehappyfoodie import TheHappyFoodie
from .thepioneerwoman import ThePioneerWoman
from .thespruceeats import TheSpruceEats
from .thevintagemixer import TheVintageMixer
from .tineno import TineNo
from .tudogostoso import TudoGostoso
from .twopeasandtheirpod import TwoPeasAndTheirPod
from .vegolosi import Vegolosi
from .whatsgabycooking import WhatsGabyCooking
from .wikicookbook import WikiCookbook
from .yummly import Yummly
from .geniuskitchen import GeniusKitchen

SCRAPERS = {
    AllRecipes.host(): AllRecipes,
    ArchanasKitchen.host(): ArchanasKitchen,
    BBCFood.host(): BBCFood,
    BBCFood.host(domain="co.uk"): BBCFood,
    BBCGoodFood.host(): BBCGoodFood,
    BettyCrocker.host(): BettyCrocker,
    BonAppetit.host(): BonAppetit,
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
    FineDiningLovers.host(): FineDiningLovers,
    FitMenCook.host(): FitMenCook,
    Food.host(): Food,
    FoodNetwork.host(): FoodNetwork,
    FoodRepublic.host(): FoodRepublic,
    GialloZafferano.host(): GialloZafferano,
    GonnaWantSeconds.host(): GonnaWantSeconds,
    Gousto.host(): Gousto,
    GreatBritishChefs.host(): GreatBritishChefs,
    HeinzBrasil.host(): HeinzBrasil,
    HelloFresh.host(): HelloFresh,
    HelloFresh.host(domain="co.uk"): HelloFresh,
    HundredAndOneCookbooks.host(): HundredAndOneCookbooks,
    IG.host(): IG,
    Inspiralized.host(): Inspiralized,
    JamieOliver.host(): JamieOliver,
    JustBento.host(): JustBento,
    TheKitchn.host(): TheKitchn,
    Marmiton.host(): Marmiton,
    Matprat.host(): Matprat,
    Mindmegette.host(): Mindmegette,
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
    SouthernLiving.host(): SouthernLiving,
    SteamyKitchen.host(): SteamyKitchen,
    TastesOfLizzyT.host(): TastesOfLizzyT,
    TastyKitchen.host(): TastyKitchen,
    TheHappyFoodie.host(): TheHappyFoodie,
    ThePioneerWoman.host(): ThePioneerWoman,
    TheSpruceEats.host(): TheSpruceEats,
    TheVintageMixer.host(): TheVintageMixer,
    TineNo.host(): TineNo,
    TudoGostoso.host(): TudoGostoso,
    TwoPeasAndTheirPod.host(): TwoPeasAndTheirPod,
    Vegolosi.host(): Vegolosi,
    WhatsGabyCooking.host(): WhatsGabyCooking,
    WikiCookbook.host(): WikiCookbook,
    Yummly.host(): Yummly,
    GeniusKitchen.host(): GeniusKitchen,
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
