import contextlib
from typing import Optional

from ._abstract import AbstractScraper
from ._exceptions import NoSchemaFoundInWildMode, WebsiteNotImplementedError
from ._factory import SchemaScraperFactory
from ._utils import get_host_name
from .abril import Abril
from .acouplecooks import ACoupleCooks
from .afghankitchenrecipes import AfghanKitchenRecipes
from .akispetretzikis import AkisPetretzikis
from .allrecipes import AllRecipes
from .alltomat import AllTomat
from .altonbrown import AltonBrown
from .amazingribs import AmazingRibs
from .ambitiouskitchen import AmbitiousKitchen
from .archanaskitchen import ArchanasKitchen
from .atelierdeschefs import AtelierDesChefs
from .averiecooks import AverieCooks
from .bakingmischeif import BakingMischeif
from .bakingsense import BakingSense
from .bbcfood import BBCFood
from .bbcgoodfood import BBCGoodFood
from .bettybossi import BettyBossi
from .bettycrocker import BettyCrocker
from .bigoven import BigOven
from .blueapron import BlueApron
from .bodybuilding import Bodybuilding
from .bonappetit import BonAppetit
from .bowlofdelicious import BowlOfDelicious
from .budgetbytes import BudgetBytes
from .castironketo import CastIronKeto
from .cdkitchen import CdKitchen
from .chefkoch import Chefkoch
from .closetcooking import ClosetCooking
from .comidinhasdochef import ComidinhasDoChef
from .cookeatshare import CookEatShare
from .cookieandkate import CookieAndKate
from .cookingcircle import CookingCircle
from .cookinglight import CookingLight
from .cookpad import CookPad
from .cookstr import Cookstr
from .copykat import CopyKat
from .countryliving import CountryLiving
from .cucchiaio import Cucchiaio
from .cuisineaz import CuisineAZ
from .cybercook import Cybercook
from .davidlebovitz import DavidLebovitz
from .delish import Delish
from .ditchthecarbs import DitchTheCarbs
from .domesticateme import DomesticateMe
from .downshiftology import Downshiftology
from .dr import Dr
from .eatingbirdfood import EatingBirdFood
from .eatingwell import EatingWell
from .eatsmarter import Eatsmarter
from .eatwhattonight import EatWhatTonight
from .epicurious import Epicurious
from .ethanchlebowski import EthanChlebowski
from .farmhousedelivery import FarmhouseDelivery
from .fifteenspatulas import FifteenSpatulas
from .finedininglovers import FineDiningLovers
from .fitmencook import FitMenCook
from .food import Food
from .food52 import Food52
from .foodandwine import FoodAndWine
from .foodnetwork import FoodNetwork
from .foodrepublic import FoodRepublic
from .forksoverknives import ForksOverKnives
from .franzoesischkochen import FranzoesischKochen
from .fredriksfikaallas import FredriksFikaAllas
from .g750g import G750g
from .geniuskitchen import GeniusKitchen
from .giallozafferano import GialloZafferano
from .gimmesomeoven import GimmeSomeOven
from .globo import Globo
from .gonnawantseconds import GonnaWantSeconds
from .goustojson import GoustoJson
from .greatbritishchefs import GreatBritishChefs
from .halfbakedharvest import HalfBakedHarvest
from .hassenchef import Hassanchef
from .headbangerskitchen import HeadbangersKitchen
from .heb import HEB
from .heinzbrasil import HeinzBrasil
from .hellofresh import HelloFresh
from .homechef import HomeChef
from .hostthetoast import Hostthetoast
from .hundredandonecookbooks import HundredAndOneCookbooks
from .ig import IG
from .imworthy import ImWorthy
from .indianhealthyrecipes import IndianHealthyRecipes
from .innit import Innit
from .inspiralized import Inspiralized
from .jamieoliver import JamieOliver
from .jimcooksfoodgood import JimCooksFoodGood
from .joyfoodsunshine import Joyfoodsunshine
from .justataste import JustATaste
from .justbento import JustBento
from .justonecookbook import JustOneCookbook
from .kennymcgovern import KennyMcGovern
from .kingarthur import KingArthur
from .kitchenstories import KitchenStories
from .kochbar import Kochbar
from .koket import Koket
from .kptncook import KptnCook
from .kuchniadomowa import KuchniaDomowa
from .kwestiasmaku import KwestiaSmaku
from .latelierderoxane import LAtelierDeRoxane
from .lecker import Lecker
from .lecremedelacrumb import LeCremeDeLaCrumb
from .lekkerensimpel import LekkerEnSimpel
from .littlespicejar import LittleSpiceJar
from .livelytable import LivelyTable
from .lovingitvegan import Lovingitvegan
from .madensverden import MadensVerden
from .madewithlau import MadeWithLau
from .marleyspoon import MarleySpoon
from .marmiton import Marmiton
from .marthastewart import MarthaStewart
from .matprat import Matprat
from .meljoulwan import Meljoulwan
from .melskitchencafe import MelsKitchenCafe
from .mindmegette import Mindmegette
from .minimalistbaker import Minimalistbaker
from .misya import Misya
from .mobkitchen import MobKitchen
from .momswithcrockpots import MomsWithCrockPots
from .monsieurcuisine import MonsieurCuisine
from .motherthyme import MotherThyme
from .mybakingaddiction import MyBakingAddiction
from .mykitchen101 import MyKitchen101
from .mykitchen101en import MyKitchen101en
from .myrecipes import MyRecipes
from .nhshealthierfamilies import NHSHealthierFamilies
from .nihhealthyeating import NIHHealthyEating
from .nourishedbynutrition import NourishedByNutrition
from .nutritionbynathalie import NutritionByNathalie
from .nytimes import NYTimes
from .ohsheglows import OhSheGlows
from .onehundredonecookbooks import OneHundredOneCookBooks
from .paleorunningmomma import PaleoRunningMomma
from .panelinha import Panelinha
from .paninihappy import PaniniHappy
from .pingodoce import PingoDoce
from .popsugar import PopSugar
from .practicalselfreliance import PracticalSelfReliance
from .primaledgehealth import PrimalEdgeHealth
from .przepisy import Przepisy
from .purelypope import PurelyPope
from .purplecarrot import PurpleCarrot
from .rachlmansfield import RachlMansfield
from .rainbowplantlife import RainbowPlantLife
from .realfoodtesco import RealFoodTesco
from .realsimple import RealSimple
from .recipetineats import RecipeTinEats
from .redhousespice import RedHouseSpice
from .reishunger import Reishunger
from .rezeptwelt import Rezeptwelt
from .sallysbakingaddiction import SallysBakingAddiction
from .sallysblog import SallysBlog
from .saveur import Saveur
from .seriouseats import SeriousEats
from .simplyquinoa import SimplyQuinoa
from .simplyrecipes import SimplyRecipes
from .simplywhisked import SimplyWhisked
from .skinnytaste import SkinnyTaste
from .southernliving import SouthernLiving
from .spendwithpennies import SpendWithPennies
from .springlane import Springlane
from .steamykitchen import SteamyKitchen
from .streetkitchen import StreetKitchen
from .sunbasket import SunBasket
from .sundpaabudget import SundPaaBudget
from .sweetcsdesigns import SweetCsDesigns
from .sweetpeasandsaffron import SweetPeasAndSaffron
from .tasteofhome import TasteOfHome
from .tastesbetterfromscratch import TastesBetterFromScratch
from .tastesoflizzyt import TastesOfLizzyT
from .tasty import Tasty
from .tastykitchen import TastyKitchen
from .theclevercarrot import TheCleverCarrot
from .thehappyfoodie import TheHappyFoodie
from .thekitchenmagpie import TheKitchenMagPie
from .thekitchn import TheKitchn
from .thenutritiouskitchen import TheNutritiousKitchen
from .thepioneerwoman import ThePioneerWoman
from .thespruceeats import TheSpruceEats
from .thevintagemixer import TheVintageMixer
from .thewoksoflife import Thewoksoflife
from .timesofindia import TimesOfIndia
from .tineno import TineNo
from .tudogostoso import TudoGostoso
from .twopeasandtheirpod import TwoPeasAndTheirPod
from .usdamyplate import USDAMyPlate
from .valdemarsro import Valdemarsro
from .vanillaandbean import VanillaAndBean
from .vegolosi import Vegolosi
from .vegrecipesofindia import VegRecipesOfIndia
from .watchwhatueat import WatchWhatUEat
from .whatsgabycooking import WhatsGabyCooking
from .wholefoods import WholeFoods
from .wikicookbook import WikiCookbook
from .woolworths import Woolworths
from .woop import Woop
from .yemek import Yemek
from .yummly import Yummly
from .zeitwochenmarkt import ZeitWochenmarkt
from .zenbelly import ZenBelly

SCRAPERS = {
    ACoupleCooks.host(): ACoupleCooks,
    Abril.host(): Abril,
    AfghanKitchenRecipes.host(): AfghanKitchenRecipes,
    AkisPetretzikis.host(): AkisPetretzikis,
    AllRecipes.host(): AllRecipes,
    AllTomat.host(): AllTomat,
    AltonBrown.host(): AltonBrown,
    AmazingRibs.host(): AmazingRibs,
    AmbitiousKitchen.host(): AmbitiousKitchen,
    ArchanasKitchen.host(): ArchanasKitchen,
    AtelierDesChefs.host(): AtelierDesChefs,
    AverieCooks.host(): AverieCooks,
    BBCFood.host(): BBCFood,
    BBCFood.host(domain="co.uk"): BBCFood,
    BBCGoodFood.host(): BBCGoodFood,
    BakingSense.host(): BakingSense,
    BakingMischeif.host(): BakingMischeif,
    BettyBossi.host(): BettyBossi,
    BettyCrocker.host(): BettyCrocker,
    BigOven.host(): BigOven,
    BlueApron.host(): BlueApron,
    Bodybuilding.host(): Bodybuilding,
    BonAppetit.host(): BonAppetit,
    BowlOfDelicious.host(): BowlOfDelicious,
    BudgetBytes.host(): BudgetBytes,
    CastIronKeto.host(): CastIronKeto,
    CdKitchen.host(): CdKitchen,
    Chefkoch.host(): Chefkoch,
    ClosetCooking.host(): ClosetCooking,
    ComidinhasDoChef.host(): ComidinhasDoChef,
    CookEatShare.host(): CookEatShare,
    CookPad.host(): CookPad,
    CookieAndKate.host(): CookieAndKate,
    CookingCircle.host(): CookingCircle,
    CookingLight.host(): CookingLight,
    Cookstr.host(): Cookstr,
    CopyKat.host(): CopyKat,
    CountryLiving.host(): CountryLiving,
    Cucchiaio.host(): Cucchiaio,
    CuisineAZ.host(): CuisineAZ,
    Cybercook.host(): Cybercook,
    DavidLebovitz.host(): DavidLebovitz,
    Delish.host(): Delish,
    DitchTheCarbs.host(): DitchTheCarbs,
    DomesticateMe.host(): DomesticateMe,
    Downshiftology.host(): Downshiftology,
    Dr.host(): Dr,
    EatWhatTonight.host(): EatWhatTonight,
    EatingBirdFood.host(): EatingBirdFood,
    EatingWell.host(): EatingWell,
    Eatsmarter.host(): Eatsmarter,
    Eatsmarter.host(domain="de"): Eatsmarter,
    Epicurious.host(): Epicurious,
    EthanChlebowski.host(): EthanChlebowski,
    FarmhouseDelivery.host(): FarmhouseDelivery,
    FifteenSpatulas.host(): FifteenSpatulas,
    FineDiningLovers.host(): FineDiningLovers,
    FitMenCook.host(): FitMenCook,
    Food.host(): Food,
    Food52.host(): Food52,
    FoodAndWine.host(): FoodAndWine,
    FoodNetwork.host(): FoodNetwork,
    FoodRepublic.host(): FoodRepublic,
    ForksOverKnives.host(): ForksOverKnives,
    FranzoesischKochen.host(): FranzoesischKochen,
    FredriksFikaAllas.host(): FredriksFikaAllas,
    G750g.host(): G750g,
    GeniusKitchen.host(): GeniusKitchen,
    GialloZafferano.host(): GialloZafferano,
    GimmeSomeOven.host(): GimmeSomeOven,
    Globo.host(): Globo,
    GonnaWantSeconds.host(): GonnaWantSeconds,
    GoustoJson.host(): GoustoJson,
    GreatBritishChefs.host(): GreatBritishChefs,
    HEB.host(): HEB,
    HalfBakedHarvest.host(): HalfBakedHarvest,
    Hassanchef.host(): Hassanchef,
    HeadbangersKitchen.host(): HeadbangersKitchen,
    HeinzBrasil.host(): HeinzBrasil,
    HelloFresh.host(): HelloFresh,
    HelloFresh.host(domain="co.uk"): HelloFresh,
    HelloFresh.host(domain="de"): HelloFresh,
    HelloFresh.host(domain="fr"): HelloFresh,
    HelloFresh.host(domain="nl"): HelloFresh,
    HomeChef.host(): HomeChef,
    Hostthetoast.host(): Hostthetoast,
    HundredAndOneCookbooks.host(): HundredAndOneCookbooks,
    ImWorthy.host(): ImWorthy,
    IG.host(): IG,
    IndianHealthyRecipes.host(): IndianHealthyRecipes,
    Innit.host(): Innit,
    Inspiralized.host(): Inspiralized,
    JamieOliver.host(): JamieOliver,
    JimCooksFoodGood.host(): JimCooksFoodGood,
    Joyfoodsunshine.host(): Joyfoodsunshine,
    JustATaste.host(): JustATaste,
    JustBento.host(): JustBento,
    JustOneCookbook.host(): JustOneCookbook,
    KennyMcGovern.host(): KennyMcGovern,
    KingArthur.host(): KingArthur,
    KitchenStories.host(): KitchenStories,
    Kochbar.host(): Kochbar,
    Koket.host(): Koket,
    KptnCook.host(): KptnCook,
    KptnCook.host(subdomain="sharing"): KptnCook,
    KuchniaDomowa.host(): KuchniaDomowa,
    KwestiaSmaku.host(): KwestiaSmaku,
    LAtelierDeRoxane.host(): LAtelierDeRoxane,
    LeCremeDeLaCrumb.host(): LeCremeDeLaCrumb,
    Lecker.host(): Lecker,
    LekkerEnSimpel.host(): LekkerEnSimpel,
    LittleSpiceJar.host(): LittleSpiceJar,
    LivelyTable.host(): LivelyTable,
    Lovingitvegan.host(): Lovingitvegan,
    MadensVerden.host(): MadensVerden,
    MadeWithLau.host(): MadeWithLau,
    MarleySpoon.host(): MarleySpoon,
    MarleySpoon.host(domain="de"): MarleySpoon,
    MarleySpoon.host(domain="com.au"): MarleySpoon,
    MarleySpoon.host(domain="be"): MarleySpoon,
    MarleySpoon.host(domain="nl"): MarleySpoon,
    MarleySpoon.host(domain="at"): MarleySpoon,
    MarleySpoon.host(domain="se"): MarleySpoon,
    Marmiton.host(): Marmiton,
    MarthaStewart.host(): MarthaStewart,
    Matprat.host(): Matprat,
    Meljoulwan.host(): Meljoulwan,
    MelsKitchenCafe.host(): MelsKitchenCafe,
    Mindmegette.host(): Mindmegette,
    Minimalistbaker.host(): Minimalistbaker,
    Misya.host(): Misya,
    MobKitchen.host(): MobKitchen,
    MomsWithCrockPots.host(): MomsWithCrockPots,
    MonsieurCuisine.host(): MonsieurCuisine,
    MotherThyme.host(): MotherThyme,
    MyBakingAddiction.host(): MyBakingAddiction,
    MyKitchen101.host(): MyKitchen101,
    MyKitchen101en.host(): MyKitchen101en,
    MyRecipes.host(): MyRecipes,
    NHSHealthierFamilies.host(): NHSHealthierFamilies,
    NIHHealthyEating.host(): NIHHealthyEating,
    NYTimes.host(): NYTimes,
    NourishedByNutrition.host(): NourishedByNutrition,
    NutritionByNathalie.host(): NutritionByNathalie,
    OhSheGlows.host(): OhSheGlows,
    OneHundredOneCookBooks.host(): OneHundredOneCookBooks,
    PaleoRunningMomma.host(): PaleoRunningMomma,
    Panelinha.host(): Panelinha,
    PaniniHappy.host(): PaniniHappy,
    PingoDoce.host(): PingoDoce,
    PopSugar.host(): PopSugar,
    PracticalSelfReliance.host(): PracticalSelfReliance,
    PrimalEdgeHealth.host(): PrimalEdgeHealth,
    Przepisy.host(): Przepisy,
    PurelyPope.host(): PurelyPope,
    PurpleCarrot.host(): PurpleCarrot,
    RachlMansfield.host(): RachlMansfield,
    RainbowPlantLife.host(): RainbowPlantLife,
    RealFoodTesco.host(): RealFoodTesco,
    RealSimple.host(): RealSimple,
    RealFoodTesco.host(): RealFoodTesco,
    RecipeTinEats.host(): RecipeTinEats,
    RedHouseSpice.host(): RedHouseSpice,
    Reishunger.host(): Reishunger,
    Rezeptwelt.host(): Rezeptwelt,
    SallysBakingAddiction.host(): SallysBakingAddiction,
    SallysBlog.host(): SallysBlog,
    Saveur.host(): Saveur,
    SeriousEats.host(): SeriousEats,
    SimplyQuinoa.host(): SimplyQuinoa,
    SimplyRecipes.host(): SimplyRecipes,
    SimplyWhisked.host(): SimplyWhisked,
    SkinnyTaste.host(): SkinnyTaste,
    SouthernLiving.host(): SouthernLiving,
    SpendWithPennies.host(): SpendWithPennies,
    Springlane.host(): Springlane,
    SteamyKitchen.host(): SteamyKitchen,
    StreetKitchen.host(): StreetKitchen,
    SunBasket.host(): SunBasket,
    SundPaaBudget.host(): SundPaaBudget,
    SweetCsDesigns.host(): SweetCsDesigns,
    SweetPeasAndSaffron.host(): SweetPeasAndSaffron,
    TasteOfHome.host(): TasteOfHome,
    TastesBetterFromScratch.host(): TastesBetterFromScratch,
    TastesOfLizzyT.host(): TastesOfLizzyT,
    Tasty.host(): Tasty,
    TastyKitchen.host(): TastyKitchen,
    TheCleverCarrot.host(): TheCleverCarrot,
    TheHappyFoodie.host(): TheHappyFoodie,
    TheKitchenMagPie.host(): TheKitchenMagPie,
    TheKitchn.host(): TheKitchn,
    TheNutritiousKitchen.host(): TheNutritiousKitchen,
    ThePioneerWoman.host(): ThePioneerWoman,
    TheSpruceEats.host(): TheSpruceEats,
    TheVintageMixer.host(): TheVintageMixer,
    Thewoksoflife.host(): Thewoksoflife,
    TimesOfIndia.host(): TimesOfIndia,
    TineNo.host(): TineNo,
    TudoGostoso.host(): TudoGostoso,
    TwoPeasAndTheirPod.host(): TwoPeasAndTheirPod,
    USDAMyPlate.host(): USDAMyPlate,
    Valdemarsro.host(): Valdemarsro,
    VanillaAndBean.host(): VanillaAndBean,
    VegRecipesOfIndia.host(): VegRecipesOfIndia,
    Vegolosi.host(): Vegolosi,
    WatchWhatUEat.host(): WatchWhatUEat,
    WhatsGabyCooking.host(): WhatsGabyCooking,
    WholeFoods.host(): WholeFoods,
    WholeFoods.host(domain="co.uk"): WholeFoods,
    Woop.host(): Woop,
    WikiCookbook.host(): WikiCookbook,
    Woolworths.host(): Woolworths,
    Yemek.host(): Yemek,
    Yummly.host(): Yummly,
    ZeitWochenmarkt.host(): ZeitWochenmarkt,
    ZenBelly.host(): ZenBelly,
}


def scrape_me(url_path, **options):
    host_name = get_host_name(url_path)

    try:
        scraper = SCRAPERS[host_name]
    except KeyError:
        if not options.get("wild_mode", False):
            raise WebsiteNotImplementedError(host_name)
        else:
            options.pop("wild_mode")
            wild_scraper = SchemaScraperFactory.generate(url_path, **options)
            if not wild_scraper.schema.data:
                raise NoSchemaFoundInWildMode(url_path)
            return wild_scraper

    return scraper(url_path, **options)


def scrape_html(html: str, org_url: Optional[str] = None, **options) -> AbstractScraper:
    """
    takes a string of html and returns a scraper object. if the org_url is specified
    then the scraper will use that url to resolve a defined scraper, otherwise it will
    fall back to wild mode. If no schema is found in wild mode then a
    NoSchemaFoundInWildMode exception will be raised.

    Args:
        html (str): raw HTML in text form
        org_url (Optional[str], optional): Original URL of the HTML. Defaults to None.

    Raises:
        NoSchemaFoundInWildMode: If no schema is found in wild mode.

    Returns:
        AbstractScraper:
    """

    host_name = get_host_name(org_url) if org_url is not None else None

    scraper = None
    if host_name:
        with contextlib.suppress(KeyError):
            scraper = SCRAPERS[host_name]

    if not scraper:
        wild_scraper = SchemaScraperFactory.generate(url=org_url, html=html, **options)

        if not wild_scraper.schema.data:
            raise NoSchemaFoundInWildMode(org_url)

        return wild_scraper

    return scraper(url=org_url, html=html, **options)


__all__ = ["scrape_me", "scrape_html"]
name = "recipe_scrapers"
