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

from urllib.request import urlopen, Request

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
from ._utils import get_host_name
from ._factory import SchemaScraperFactory
from .abeautifulmess import ABeautifulMess
from .aberlehome import AberleHome
from .abril import Abril
from .abuelascounter import AbuelasCounter
from .acouplecooks import ACoupleCooks
from .acozykitchen import ACozyKitchen
from .addapinch import AddAPinch
from .adozensundays import ADozenSundays
from .adrianasbestrecipes import AdrianasBestRecipes
from .afarmgirlsdabbles import AFarmGirlsDabbles
from .afghankitchenrecipes import AfghanKitchenRecipes
from .aflavorjournal import AFlavorJournal
from .ahealthysliceoflife import AHealthySliceOfLife
from .akispetretzikis import AkisPetretzikis
from .albertheijn import AlbertHeijn
from .aldi import Aldi
from .aldinord import AldiNord
from .aldisued import AldiSued
from .aldisuisse import AldiSuisse
from .alexandracooks import AlexandraCooks
from .alisoneroman import AlisoneRoman
from .alittlebityummy import ALittleBitYummy
from .allrecipes import AllRecipes
from .allthehealthythings import AllTheHealthyThings
from .alltommat import AlltOmMat
from .altonbrown import AltonBrown
from .amazingoriental import AmazingOriental
from .amazingribs import AmazingRibs
from .amberskitchencooks import AmbersKitchencooks
from .ambitiouskitchen import AmbitiousKitchen
from .ameessavorydish import AmeesSavoryDish
from .americastestkitchen import AmericasTestKitchen
from .archanaskitchen import ArchanasKitchen
from .argiro import Argiro
from .arla import Arla
from .asweetpeachef import ASweetPeaChef
from .atelierdeschefs import AtelierDesChefs
from .aubreyskitchen import AubreysKitchen
from .averiecooks import AverieCooks
from .bakels import Bakels
from .bakerbynature import BakerByNature
from .bakewithzoha import BakeWithZoha
from .bakingmischief import BakingMischief
from .bakingsense import BakingSense
from .barefeetinthekitchen import BarefeetInTheKitchen
from .barefootcontessa import BareFootContessa
from .barefootinthepines import BarefootInThePines
from .bbcfood import BBCFood
from .bbcgoodfood import BBCGoodFood
from .belleofthekitchen import BelleOfTheKitchen
from .bellyfull import BellyFull
from .bestrecipes import BestRecipes
from .betterfoodguru import BetterFoodGuru
from .bettybossi import BettyBossi
from .bettycrocker import BettyCrocker
from .beyondfrosting import BeyondFrosting
from .biancazapatka import BiancaZapatka
from .bigoven import BigOven
from .billyparisi import BillyParisi
from .bitsofcarey import BitsOfCarey
from .blueapron import BlueApron
from .bluejeanchef import BlueJeanChef
from .bodybuilding import Bodybuilding
from .bofrost import Bofrost
from .bonappetit import BonAppetit
from .bongeats import BongEats
from .bowlofdelicious import BowlOfDelicious
from .breadtopia import Breadtopia
from .briceletbaklava import BricelEtBaklava
from .brokenovenbaking import BrokenOvenBaking
from .budgetbytes import BudgetBytes
from .cafedelites import CafeDelites
from .cakemehometonight import CakeMeHomeTonight
from .cambreabakes import CambreaBakes
from .carlsbadcravings import CarlsBadCravings
from .carriesexperimentalkitchen import CarriesExperimentalKitchen
from .castironketo import CastIronKeto
from .cdkitchen import CdKitchen
from .celebratingsweets import CelebratingSweets
from .chefjackovens import ChefJackOvens
from .chefjeanpierre import ChefJeanPierre
from .chefkoch import Chefkoch
from .chefnini import Chefnini
from .chefsavvy import ChefSavvy
from .chewoutloud import ChewOutLoud
from .cleaneatingkitchen import CleanEatingKitchen
from .closetcooking import ClosetCooking
from .colleenchristensennutrition import ColleenChristensenNutrition
from .comidinhasdochef import ComidinhasDoChef
from .cookedandloved import CookedAndLoved
from .cookieandkate import CookieAndKate
from .cookiesandcups import CookiesAndCups
from .cookingcircle import CookingCircle
from .cookinglight import CookingLight
from .cookinglsl import CookingLSL
from .cookingwithjanica import CookingWithJanica
from .cookomix import Cookomix
from .cookpad import CookPad
from .cooktalk import CookTalk
from .cookwell import CookWell
from .copykat import CopyKat
from .corriecooks import CorrieCooks
from .costco import Costco
from .countryliving import CountryLiving
from .creativecanning import CreativeCanning
from .cucchiaio import Cucchiaio
from .cuisineaz import CuisineAZ
from .cuisinezpourbebe import CuisinezPourBebe
from .culinaryhill import CulinaryHill
from .culy import Culy
from .cybercook import Cybercook
from .dagelijksekost import DagelijkseKost
from .damndelicious import DamnDelicious
from .davidlebovitz import DavidLebovitz
from .deliciouslysprinkled import DeliciouslySprinkled
from .delish import Delish
from .dinneratthezoo import DinnerAtTheZoo
from .dinnerthendessert import DinnerThenDessert
from .dishnz import Dishnz
from .dobruchutaktualitysk import DobruChutAktualitySK
from .domesticateme import DomesticateMe
from .donalskehan import DonalSkehan
from .downshiftology import Downshiftology
from .dr import Dr
from .drizzleanddip import DrizzleAndDip
from .eatingbirdfood import EatingBirdFood
from .eatingeuropean import EatingEuropean
from .eatingonadime import EatingOnADime
from .eatingwell import EatingWell
from .eatliverun import EatLiveRun
from .eatsmarter import Eatsmarter
from .eatthismuch import EatThisMuch
from .eattolerant import EatTolerant
from .eatwell101 import EatWell101
from .eatwhattonight import EatWhatTonight
from .editionslarousse import EditionsLarousse
from .eggsca import EggsCa
from .elavegan import ElaVegan
from .emmikochteinfach import EmmiKochtEinfach
from .epicurious import Epicurious
from .erinliveswhole import ErinLivesWhole
from .erinscozykitchen import ErinsCozyKitchen
from .errenskitchen import ErrensKitchen
from .ethanchlebowski import EthanChlebowski
from .everydaydelicious import EverydayDelicious
from .everydaypie import EverydayPie
from .evolvingtable import EvolvingTable
from .familyfoodonthetable import FamilyfoodOnTheTable
from .farmhousedelivery import FarmhouseDelivery
from .farmhouseonboone import FarmhouseOnBoone
from .farmtojar import FarmToJar
from .fattoincasadabenedetta import FattoInCasaDaBenedetta
from .feastingathome import FeastingAtHome
from .feelgoodfoodie import FeelGoodFoodie
from .felixkitchen import FelixKitchen
from .festligare import Festligare
from .fifteengram import FifteenGram
from .fifteenspatulas import FifteenSpatulas
from .finedininglovers import FineDiningLovers
from .fithealthymacros import FitHealthyMacros
from .fitmencook import FitMenCook
from .fitslowcookerqueen import FitSlowCookerQueen
from .food import Food
from .food52 import Food52
from .foodandwine import FoodAndWine
from .foodbymaria import FoodByMaria
from .foodfidelity import FoodFidelity
from .foodnetwork import FoodNetwork
from .foodrepublic import FoodRepublic
from .forksoverknives import ForksOverKnives
from .forktospoon import ForkToSpoon
from .fortyaprons import FortyAprons
from .franzoesischkochen import FranzoesischKochen
from .g750g import G750g
from .garnishandglaze import GarnishAndGlaze
from .gesundaktiv import GesundAktiv
from .giallozafferano import GialloZafferano
from .gimmesomeoven import GimmeSomeOven
from .globo import Globo
from .gloriousrecipes import GloriousRecipes
from .glutenfreeonashoestring import GlutenFreeOnAShoeString
from .godt import Godt
from .gonnawantseconds import GonnaWantSeconds
from .goodfooddiscoveries import GoodFoodDiscoveries
from .goodhousekeeping import GoodHousekeeping
from .goodstuffrecipes import GoodStuffRecipes
from .gourmettraveller import GourmetTraveller
from .grandfrais import GrandFrais
from .greatbritishchefs import GreatBritishChefs
from .grimgrains import GrimGrains
from .grouprecipes import GroupRecipes
from .halfbakedharvest import HalfBakedHarvest
from .handletheheat import HandleTheHeat
from .hassanchef import HassanChef
from .headbangerskitchen import HeadbangersKitchen
from .healthywithachanceofsprinkles import HealthyWithAChanceOfSprinkles
from .heatherchristo import HeatherChristo
from .heb import HEB
from .hellofresh import HelloFresh
from .hersheyland import HersheyLand
from .hilahcooking import HilahCooking
from .hofer import Hofer
from .homeandplate import HomeAndPlate
from .homechef import HomeChef
from .hostthetoast import Hostthetoast
from .howtofeedaloon import HowToFeedALoon
from .hungryhappens import HungryHappens
from .ica import Ica
from .ig import IG
from .imworthy import ImWorthy
from .inbloombakery import InBloomBakery
from .indianhealthyrecipes import IndianHealthyRecipes
from .ingoodflavor import InGoodFlavor
from .innit import Innit
from .insanelygoodrecipes import InsanelyGoodRecipes
from .inspiralized import Inspiralized
from .inspiredtaste import InspiredTaste
from .iowagirleats import IowaGirlEats
from .irishcentral import IrishCentral
from .itdoesnttastelikechicken import ItDoesntTasteLikeChicken
from .itsnotaboutnutrition import ItsNotAboutNutrition
from .izzycooking import IzzyCooking
from .jamieoliver import JamieOliver
from .jennycancook import JennyCanCook
from .jimcooksfoodgood import JimCooksFoodGood
from .jocooks import JoCooks
from .joshuaweissman import JoshuaWeissman
from .joyfoodsunshine import Joyfoodsunshine
from .joythebaker import JoyTheBaker
from .juliegoodwin import JulieGoodwin
from .jumbo import Jumbo
from .justalittlebitofbacon import JustALittleBitOfBacon
from .justataste import JustATaste
from .justbento import JustBento
from .justinesnacks import JustineSnacks
from .justonecookbook import JustOneCookbook
from .kalejunkie import KaleJunkie
from .kellyscleankitchen import KellysCleanKitchen
from .kennymcgovern import KennyMcGovern
from .keukenliefdenl import KeukenLiefdeNL
from .kfoods import KFoods
from .kiddokitchen import KiddoKitchen
from .kikkoman import Kikkoman
from .kingarthur import KingArthur
from .kitchenaidaustralia import KitchenAidAustralia
from .kitchendivas import KitchenDivas
from .kitchendreaming import KitchenDreaming
from .kitchensanctuary import KitchenSanctuary
from .kitchenstories import KitchenStories
from .kochbar import Kochbar
from .kochbucher import Kochbucher
from .koket import Koket
from .kookjij import KookJij
from .kristineskitchenblog import KristinesKitchenBlog
from .krollskorner import KrollsKorner
from .kuchniadomowa import KuchniaDomowa
from .kuchynalidla import KuchynaLidla
from .kwestiasmaku import KwestiaSmaku
from .lacucinaitaliana import LaCucinaItaliana
from .lanascooking import LanasCooking
from .latelierderoxane import LAtelierDeRoxane
from .lazycatkitchen import LazyCatKitchen
from .leanandgreenrecipes import LeanAndGreenRecipes
from .lecker import Lecker
from .leckerschmecker import LeckerSchmecker
from .lecremedelacrumb import LeCremeDeLaCrumb
from .leitesculinaria import LeitesCulinaria
from .lekkerensimpel import LekkerEnSimpel
from .leukerecepten import Leukerecepten
from .lidiasitaly import LidiasItaly
from .lifestyleofafoodie import LifestyleOfAFoodie
from .littleferrarokitchen import LittleFerraroKitchen
from .littlespicejar import LittleSpiceJar
from .littlesunnykitchen import LittleSunnyKitchen
from .livelytable import LivelyTable
from .lmld import Lmld
from .lolascocina import LolasCocina
from .loveandlemons import LoveAndLemons
from .lovefood import LoveFood
from .lovingitvegan import Lovingitvegan
from .maangchi import Maangchi
from .madamecuisine import MadameCuisine
from .madensverden import MadensVerden
from .madsvin import Madsvin
from .magimix import Magimix
from .makeitdairyfree import MakeItDairyFree
from .marmiton import Marmiton
from .marthastewart import MarthaStewart
from .matprat import Matprat
from .mccormick import McCormick
from .mealprepmanual import MealPrepManual
from .meganvskitchen import MeganVsKitchen
from .meljoulwan import Meljoulwan
from .mellisaknorris import MellisaKNorris
from .melloschourico import MellosChourico
from .melskitchencafe import MelsKitchenCafe
from .migusto import Migusto
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
from .myriadrecipes import MyriadRecipes
from .myvegetarianroots import MyVegetarianRoots
from .natashaskitchen import NatashasKitchen
from .naturallyella import NaturallyElla
from .ndr import Ndr
from .netacooks import NetaCooks
from .nhshealthierfamilies import NHSHealthierFamilies
from .nibbledish import NibbleDish
from .nihhealthyeating import NIHHealthyEating
from .ninjatestkitchen import NinjaTestKitchen
from .noracooks import NoraCooks
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
from .ohsweetbasil import OhSweetBasil
from .okokorecepten import OkokoRecepten
from .omnivorescookbook import OmnivoresCookbook
from .onceuponachef import OnceUponAChef
from .onehundredonecookbooks import OneHundredOneCookBooks
from .onesweetappetite import OneSweetAppetite
from .organicallyaddison import OrganicallyAddison
from .ottolenghibooks import OttolenghiBooks
from .ourbestbites import OurBestBites
from .owenhan import OwenHan
from .paleorunningmomma import PaleoRunningMomma
from .panelinha import Panelinha
from .paninihappy import PaniniHappy
from .panlasangpinoy import PanlasangPinoy
from .peelwithzeal import PeelWithZeal
from .persnicketyplates import PersnicketyPlates
from .pickuplimes import PickUpLimes
from .picnic import Picnic
from .piesandplots import PiesAndPlots
from .pilipinasrecipes import PilipinasRecipes
from .pinchofyum import PinchOfYum
from .pingodoce import PingoDoce
from .pinkowlkitchen import PinkOwlKitchen
from .platingpixels import PlatingPixels
from .plowingthroughlife import PlowingThroughLife
from .polishfoodies import PolishFoodies
from .poppycooks import PoppyCooks
from .popsugar import PopSugar
from .potatorolls import PotatoRolls
from .practicalselfreliance import PracticalSelfReliance
from .preppykitchen import PreppyKitchen
from .pressureluckcooking import PressureLuckCooking
from .primaledgehealth import PrimalEdgeHealth
from .projectgezond import ProjectGezond
from .przepisy import Przepisy
from .purelypope import PurelyPope
from .purplecarrot import PurpleCarrot
from .quakeroats import QuakerOats
from .quitoque import QuiToque
from .rachlmansfield import RachlMansfield
from .rainbowplantlife import RainbowPlantLife
from .realfoodtesco import RealFoodTesco
from .realfoodwell import RealFoodWell
from .realmomnutrition import RealMomNutrition
from .realsimple import RealSimple
from .receitasnestlebr import ReceitasNestleBR
from .recept import Recept
from .receptiindex import ReceptiIndex
from .receptyprevas import ReceptyPreVas
from .recetteplus import RecettePlus
from .recipegirl import RecipeGirl
from .recipeland import RecipeLand
from .reciperunner import RecipeRunner
from .recipetineats import RecipeTinEats
from .redhousespice import RedHouseSpice
from .reishunger import Reishunger
from .rewe import Rewe
from .rezeptwelt import Rezeptwelt
from .ricetta import Ricetta
from .ricetteperbimby import RicettePerBimby
from .rosannapansino import RosannaPansino
from .rutgerbakt import RutgerBakt
from .saboresajinomoto import SaboresAjinomoto
from .sallysbakingaddiction import SallysBakingAddiction
from .sallysblog import SallysBlog
from .saltpepperskillet import SaltPepperSkillet
from .samsungfood import SamsungFood
from .sandwhichtribunal import SandwhichTribunal
from .saveur import Saveur
from .savoringthegood import SavoringTheGood
from .savorynothings import SavoryNothings
from .savvysavingcouple import SavvySavingCouple
from .schoolofwok import SchoolOfWok
from .scrambledandscrumptious import ScrambledAndScrumptious
from .scrummylane import ScrummyLane
from .seriouseats import SeriousEats
from .sharkninja import SharkNinja
from .shelikesfood import SheLikesFood
from .simplegreensmoothies import SimpleGreenSmoothies
from .simplehomeedit import SimpleHomeEdit
from .simpleveganista import SimpleVeganista
from .simplycookit import SimplyCookit
from .simplyquinoa import SimplyQuinoa
from .simplyrecipes import SimplyRecipes
from .simplywhisked import SimplyWhisked
from .sipandfeast import SipAndFeast
from .sizzlefish import SizzleFish
from .sizzlingeats import SizzlingEats
from .skinnytaste import SkinnyTaste
from .smalltownwoman import SmallTownWoman
from .smulweb import Smulweb
from .sobors import SoBors
from .southerncastiron import SouthernCastIron
from .southernliving import SouthernLiving
from .spainonafork import SpainOnAFork
from .spendwithpennies import SpendWithPennies
from .spicysouthernkitchen import SpicySouthernKitchen
from .spisbedre import SpisBedre
from .springlane import Springlane
from .stacyling import StacyLing
from .staysnatched import StaySnatched
from .steamykitchen import SteamyKitchen
from .streetkitchen import StreetKitchen
from .strongrfastr import StrongrFastr
from .sudachirecipes import SudachiRecipes
from .sugarhero import SugarHero
from .sunbasket import SunBasket
from .sundpaabudget import SundPaaBudget
from .sunset import Sunset
from .sweetcsdesigns import SweetCsDesigns
from .sweetpeasandsaffron import SweetPeasAndSaffron
from .swissmilk import SwissMilk
from .tableanddish import TableAndDish
from .tasteatlas import TasteAtlas
from .tasteau import TasteAU
from .tasteofhome import TasteOfHome
from .tastesbetterfromscratch import TastesBetterFromScratch
from .tastesoflizzyt import TastesOfLizzyT
from .tastinghistory import TastingHistory
from .tasty import Tasty
from .tastykitchen import TastyKitchen
from .tastyoven import TastyOven
from .tatyanaseverydayfood import TatyanasEverydayFood
from .thealmondeater import TheAlmondEater
from .thebigmansworld import TheBigMansWorld
from .theclevercarrot import TheCleverCarrot
from .thecookierookie import TheCookieRookie
from .thecookingguy import TheCookingGuy
from .thefirstmess import TheFirstMess
from .thefoodietakesflight import TheFoodieTakesFlight
from .theglutenfreeaustrian import TheGlutenFreeAustrian
from .thehappyfoodie import TheHappyFoodie
from .theicecreamconfectionals import TheIceCreamConfectionals
from .thekitchencommunity import TheKitchenCommunity
from .thekitchenmagpie import TheKitchenMagPie
from .thekitchn import TheKitchn
from .theloopywhisk import TheLoopyWhisk
from .themagicalslowcooker import TheMagicalSlowCooker
from .themediterranedish import TheMediterraneDish
from .themodernproper import TheModernProper
from .theoldwomanandthesea import TheOldWomanAndTheSea
from .thepalatablelife import ThePalatableLife
from .thepioneerwoman import ThePioneerWoman
from .theplantbasedschool import ThePlantBasedSchool
from .therecipecritic import TheRecipeCritic
from .thesaltymarshmallow import TheSaltyMarshmallow
from .thespicetrain import TheSpiceTrain
from .thespruceeats import TheSpruceEats
from .thesuburbansoapbox import TheSuburbanSoapBox
from .thevintagemixer import TheVintageMixer
from .thewoksoflife import Thewoksoflife
from .thinlicious import Thinlicious
from .thishealthytable import ThisHealthyTable
from .tidymom import TidyMom
from .timesofindia import TimesOfIndia
from .tineno import TineNo
from .tofoo import Tofoo
from .toriavey import ToriAvey
from .tudogostoso import TudoGostoso
from .twentyfourkitchen import TwentyFourKitchen
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
from .veroniquecloutier import VeroniqueCloutier
from .waitrose import Waitrose
from .watchwhatueat import WatchWhatUEat
from .wdr import WDR
from .wearenotmartha import WeAreNotMartha
from .wedishitup import WeDishItUp
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
from .wyseguide import WyseGuide
from .xiachufang import Xiachufang
from .yamasa import Yamasa
from .yemek import Yemek
from .yummly import Yummly
from .zaubertopf import ZauberTopf
from .zeitwochenmarkt import ZeitWochenmarkt
from .zenbelly import ZenBelly
from .zestfulkitchen import ZestfulKitchen

SCRAPERS = {
    ABeautifulMess.host(): ABeautifulMess,
    AberleHome.host(): AberleHome,
    Abril.host(): Abril,
    AbuelasCounter.host(): AbuelasCounter,
    ACoupleCooks.host(): ACoupleCooks,
    ACozyKitchen.host(): ACozyKitchen,
    AddAPinch.host(): AddAPinch,
    ADozenSundays.host(): ADozenSundays,
    AdrianasBestRecipes.host(): AdrianasBestRecipes,
    AFarmGirlsDabbles.host(): AFarmGirlsDabbles,
    AfghanKitchenRecipes.host(): AfghanKitchenRecipes,
    AFlavorJournal.host(): AFlavorJournal,
    AHealthySliceOfLife.host(): AHealthySliceOfLife,
    AkisPetretzikis.host(): AkisPetretzikis,
    AlbertHeijn.host(): AlbertHeijn,
    AlbertHeijn.host(domain="ah.be"): AlbertHeijn,
    Aldi.host(): Aldi,
    AldiNord.host(): AldiNord,
    AldiNord.host(domain="aldi.es"): AldiNord,
    AldiNord.host(domain="aldi.fr"): AldiNord,
    AldiNord.host(domain="aldi.lu"): AldiNord,
    AldiNord.host(domain="aldi.nl"): AldiNord,
    AldiNord.host(domain="aldi.pl"): AldiNord,
    AldiNord.host(domain="aldi.pt"): AldiNord,
    AldiSued.host(): AldiSued,
    AldiSued.host(domain="aldi.hu"): AldiSued,
    AldiSued.host(domain="aldi.it"): AldiSued,
    AldiSuisse.host(): AldiSuisse,
    AlexandraCooks.host(): AlexandraCooks,
    AlisoneRoman.host(): AlisoneRoman,
    ALittleBitYummy.host(): ALittleBitYummy,
    AllRecipes.host(): AllRecipes,
    AllTheHealthyThings.host(): AllTheHealthyThings,
    AlltOmMat.host(): AlltOmMat,
    AltonBrown.host(): AltonBrown,
    AmazingOriental.host(): AmazingOriental,
    AmazingRibs.host(): AmazingRibs,
    AmbersKitchencooks.host(): AmbersKitchencooks,
    AmbitiousKitchen.host(): AmbitiousKitchen,
    AmeesSavoryDish.host(): AmeesSavoryDish,
    AmericasTestKitchen.host(): AmericasTestKitchen,
    ArchanasKitchen.host(): ArchanasKitchen,
    Argiro.host(): Argiro,
    Arla.host(): Arla,
    ASweetPeaChef.host(): ASweetPeaChef,
    AtelierDesChefs.host(): AtelierDesChefs,
    AubreysKitchen.host(): AubreysKitchen,
    AverieCooks.host(): AverieCooks,
    Bakels.host(): Bakels,
    Bakels.host(domain="co.uk"): Bakels,
    BakerByNature.host(): BakerByNature,
    BakeWithZoha.host(): BakeWithZoha,
    BakingMischief.host(): BakingMischief,
    BakingSense.host(): BakingSense,
    BarefeetInTheKitchen.host(): BarefeetInTheKitchen,
    BareFootContessa.host(): BareFootContessa,
    BarefootInThePines.host(): BarefootInThePines,
    BBCFood.host(): BBCFood,
    BBCFood.host(domain="co.uk"): BBCFood,
    BBCGoodFood.host(): BBCGoodFood,
    BelleOfTheKitchen.host(): BelleOfTheKitchen,
    BellyFull.host(): BellyFull,
    BestRecipes.host(): BestRecipes,
    BetterFoodGuru.host(): BetterFoodGuru,
    BettyBossi.host(): BettyBossi,
    BettyCrocker.host(): BettyCrocker,
    BeyondFrosting.host(): BeyondFrosting,
    BiancaZapatka.host(): BiancaZapatka,
    BigOven.host(): BigOven,
    BillyParisi.host(): BillyParisi,
    BitsOfCarey.host(): BitsOfCarey,
    BlueApron.host(): BlueApron,
    BlueJeanChef.host(): BlueJeanChef,
    Bodybuilding.host(): Bodybuilding,
    Bofrost.host(): Bofrost,
    BonAppetit.host(): BonAppetit,
    BongEats.host(): BongEats,
    BowlOfDelicious.host(): BowlOfDelicious,
    Breadtopia.host(): Breadtopia,
    BricelEtBaklava.host(): BricelEtBaklava,
    BrokenOvenBaking.host(): BrokenOvenBaking,
    BudgetBytes.host(): BudgetBytes,
    CafeDelites.host(): CafeDelites,
    CakeMeHomeTonight.host(): CakeMeHomeTonight,
    CambreaBakes.host(): CambreaBakes,
    CarlsBadCravings.host(): CarlsBadCravings,
    CarriesExperimentalKitchen.host(): CarriesExperimentalKitchen,
    CastIronKeto.host(): CastIronKeto,
    CdKitchen.host(): CdKitchen,
    CelebratingSweets.host(): CelebratingSweets,
    ChefJackOvens.host(): ChefJackOvens,
    ChefJeanPierre.host(): ChefJeanPierre,
    Chefkoch.host(): Chefkoch,
    Chefnini.host(): Chefnini,
    ChefSavvy.host(): ChefSavvy,
    ChewOutLoud.host(): ChewOutLoud,
    CleanEatingKitchen.host(): CleanEatingKitchen,
    ClosetCooking.host(): ClosetCooking,
    ColleenChristensenNutrition.host(): ColleenChristensenNutrition,
    ComidinhasDoChef.host(): ComidinhasDoChef,
    CookedAndLoved.host(): CookedAndLoved,
    CookieAndKate.host(): CookieAndKate,
    CookiesAndCups.host(): CookiesAndCups,
    CookingCircle.host(): CookingCircle,
    CookingLight.host(): CookingLight,
    CookingLSL.host(): CookingLSL,
    CookingWithJanica.host(): CookingWithJanica,
    Cookomix.host(): Cookomix,
    CookPad.host(): CookPad,
    CookTalk.host(): CookTalk,
    CookWell.host(): CookWell,
    CopyKat.host(): CopyKat,
    CorrieCooks.host(): CorrieCooks,
    Costco.host(): Costco,
    CountryLiving.host(): CountryLiving,
    CreativeCanning.host(): CreativeCanning,
    Cucchiaio.host(): Cucchiaio,
    CuisineAZ.host(): CuisineAZ,
    CuisinezPourBebe.host(): CuisinezPourBebe,
    CulinaryHill.host(): CulinaryHill,
    Culy.host(): Culy,
    Cybercook.host(): Cybercook,
    DagelijkseKost.host(): DagelijkseKost,
    DamnDelicious.host(): DamnDelicious,
    DavidLebovitz.host(): DavidLebovitz,
    DeliciouslySprinkled.host(): DeliciouslySprinkled,
    Delish.host(): Delish,
    DinnerAtTheZoo.host(): DinnerAtTheZoo,
    DinnerThenDessert.host(): DinnerThenDessert,
    Dishnz.host(): Dishnz,
    DobruChutAktualitySK.host(): DobruChutAktualitySK,
    DomesticateMe.host(): DomesticateMe,
    DonalSkehan.host(): DonalSkehan,
    Downshiftology.host(): Downshiftology,
    Dr.host(): Dr,
    DrizzleAndDip.host(): DrizzleAndDip,
    EatingBirdFood.host(): EatingBirdFood,
    EatingEuropean.host(): EatingEuropean,
    EatingOnADime.host(): EatingOnADime,
    EatingWell.host(): EatingWell,
    EatLiveRun.host(): EatLiveRun,
    Eatsmarter.host(): Eatsmarter,
    Eatsmarter.host(domain="de"): Eatsmarter,
    EatThisMuch.host(): EatThisMuch,
    EatTolerant.host(): EatTolerant,
    EatWell101.host(): EatWell101,
    EatWhatTonight.host(): EatWhatTonight,
    EditionsLarousse.host(): EditionsLarousse,
    EggsCa.host(): EggsCa,
    ElaVegan.host(): ElaVegan,
    EmmiKochtEinfach.host(): EmmiKochtEinfach,
    Epicurious.host(): Epicurious,
    ErinLivesWhole.host(): ErinLivesWhole,
    ErinsCozyKitchen.host(): ErinsCozyKitchen,
    ErrensKitchen.host(): ErrensKitchen,
    EthanChlebowski.host(): EthanChlebowski,
    EverydayDelicious.host(): EverydayDelicious,
    EverydayPie.host(): EverydayPie,
    EvolvingTable.host(): EvolvingTable,
    FamilyfoodOnTheTable.host(): FamilyfoodOnTheTable,
    FarmhouseDelivery.host(): FarmhouseDelivery,
    FarmhouseOnBoone.host(): FarmhouseOnBoone,
    FarmToJar.host(): FarmToJar,
    FattoInCasaDaBenedetta.host(): FattoInCasaDaBenedetta,
    FeastingAtHome.host(): FeastingAtHome,
    FeelGoodFoodie.host(): FeelGoodFoodie,
    FelixKitchen.host(): FelixKitchen,
    Festligare.host(): Festligare,
    FifteenGram.host(): FifteenGram,
    FifteenSpatulas.host(): FifteenSpatulas,
    FineDiningLovers.host(): FineDiningLovers,
    FitHealthyMacros.host(): FitHealthyMacros,
    FitMenCook.host(): FitMenCook,
    FitSlowCookerQueen.host(): FitSlowCookerQueen,
    Food.host(): Food,
    Food52.host(): Food52,
    FoodAndWine.host(): FoodAndWine,
    FoodByMaria.host(): FoodByMaria,
    FoodFidelity.host(): FoodFidelity,
    FoodNetwork.host(): FoodNetwork,
    FoodNetwork.host(domain="com"): FoodNetwork,
    FoodRepublic.host(): FoodRepublic,
    ForksOverKnives.host(): ForksOverKnives,
    ForkToSpoon.host(): ForkToSpoon,
    FortyAprons.host(): FortyAprons,
    FranzoesischKochen.host(): FranzoesischKochen,
    G750g.host(): G750g,
    GarnishAndGlaze.host(): GarnishAndGlaze,
    GesundAktiv.host(): GesundAktiv,
    GialloZafferano.host(): GialloZafferano,
    GimmeSomeOven.host(): GimmeSomeOven,
    Globo.host(): Globo,
    GloriousRecipes.host(): GloriousRecipes,
    GlutenFreeOnAShoeString.host(): GlutenFreeOnAShoeString,
    Godt.host(): Godt,
    GonnaWantSeconds.host(): GonnaWantSeconds,
    GoodFoodDiscoveries.host(): GoodFoodDiscoveries,
    GoodHousekeeping.host(): GoodHousekeeping,
    GoodStuffRecipes.host(): GoodStuffRecipes,
    GourmetTraveller.host(): GourmetTraveller,
    GrandFrais.host(): GrandFrais,
    GreatBritishChefs.host(): GreatBritishChefs,
    GrimGrains.host(): GrimGrains,
    GroupRecipes.host(): GroupRecipes,
    HalfBakedHarvest.host(): HalfBakedHarvest,
    HandleTheHeat.host(): HandleTheHeat,
    HassanChef.host(): HassanChef,
    HeadbangersKitchen.host(): HeadbangersKitchen,
    HealthyWithAChanceOfSprinkles.host(): HealthyWithAChanceOfSprinkles,
    HeatherChristo.host(): HeatherChristo,
    HEB.host(): HEB,
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
    HilahCooking.host(): HilahCooking,
    Hofer.host(): Hofer,
    Hofer.host(domain="hofer.si"): Hofer,
    HomeAndPlate.host(): HomeAndPlate,
    HomeChef.host(): HomeChef,
    Hostthetoast.host(): Hostthetoast,
    HowToFeedALoon.host(): HowToFeedALoon,
    HungryHappens.host(): HungryHappens,
    Ica.host(): Ica,
    IG.host(): IG,
    ImWorthy.host(): ImWorthy,
    InBloomBakery.host(): InBloomBakery,
    IndianHealthyRecipes.host(): IndianHealthyRecipes,
    InGoodFlavor.host(): InGoodFlavor,
    Innit.host(): Innit,
    InsanelyGoodRecipes.host(): InsanelyGoodRecipes,
    Inspiralized.host(): Inspiralized,
    InspiredTaste.host(): InspiredTaste,
    IowaGirlEats.host(): IowaGirlEats,
    IrishCentral.host(): IrishCentral,
    ItDoesntTasteLikeChicken.host(): ItDoesntTasteLikeChicken,
    ItsNotAboutNutrition.host(): ItsNotAboutNutrition,
    IzzyCooking.host(): IzzyCooking,
    JamieOliver.host(): JamieOliver,
    JennyCanCook.host(): JennyCanCook,
    JimCooksFoodGood.host(): JimCooksFoodGood,
    JoCooks.host(): JoCooks,
    JoshuaWeissman.host(): JoshuaWeissman,
    Joyfoodsunshine.host(): Joyfoodsunshine,
    JoyTheBaker.host(): JoyTheBaker,
    JulieGoodwin.host(): JulieGoodwin,
    Jumbo.host(): Jumbo,
    JustALittleBitOfBacon.host(): JustALittleBitOfBacon,
    JustATaste.host(): JustATaste,
    JustBento.host(): JustBento,
    JustineSnacks.host(): JustineSnacks,
    JustOneCookbook.host(): JustOneCookbook,
    KaleJunkie.host(): KaleJunkie,
    KellysCleanKitchen.host(): KellysCleanKitchen,
    KennyMcGovern.host(): KennyMcGovern,
    KeukenLiefdeNL.host(): KeukenLiefdeNL,
    KFoods.host(): KFoods,
    KiddoKitchen.host(): KiddoKitchen,
    Kikkoman.host(): Kikkoman,
    KingArthur.host(): KingArthur,
    KitchenAidAustralia.host(): KitchenAidAustralia,
    KitchenDivas.host(): KitchenDivas,
    KitchenDreaming.host(): KitchenDreaming,
    KitchenSanctuary.host(): KitchenSanctuary,
    KitchenStories.host(): KitchenStories,
    Kochbar.host(): Kochbar,
    Kochbucher.host(): Kochbucher,
    Koket.host(): Koket,
    KookJij.host(): KookJij,
    KristinesKitchenBlog.host(): KristinesKitchenBlog,
    KrollsKorner.host(): KrollsKorner,
    KuchniaDomowa.host(): KuchniaDomowa,
    KuchynaLidla.host(): KuchynaLidla,
    KwestiaSmaku.host(): KwestiaSmaku,
    LaCucinaItaliana.host(): LaCucinaItaliana,
    LaCucinaItaliana.host(domain="com"): LaCucinaItaliana,
    LanasCooking.host(): LanasCooking,
    LAtelierDeRoxane.host(): LAtelierDeRoxane,
    LazyCatKitchen.host(): LazyCatKitchen,
    LeanAndGreenRecipes.host(): LeanAndGreenRecipes,
    Lecker.host(): Lecker,
    LeckerSchmecker.host(): LeckerSchmecker,
    LeCremeDeLaCrumb.host(): LeCremeDeLaCrumb,
    LeitesCulinaria.host(): LeitesCulinaria,
    LekkerEnSimpel.host(): LekkerEnSimpel,
    Leukerecepten.host(): Leukerecepten,
    LidiasItaly.host(): LidiasItaly,
    LifestyleOfAFoodie.host(): LifestyleOfAFoodie,
    LittleFerraroKitchen.host(): LittleFerraroKitchen,
    LittleSpiceJar.host(): LittleSpiceJar,
    LittleSunnyKitchen.host(): LittleSunnyKitchen,
    LivelyTable.host(): LivelyTable,
    Lmld.host(): Lmld,
    LolasCocina.host(): LolasCocina,
    LoveAndLemons.host(): LoveAndLemons,
    LoveFood.host(): LoveFood,
    Lovingitvegan.host(): Lovingitvegan,
    Maangchi.host(): Maangchi,
    MadameCuisine.host(): MadameCuisine,
    MadensVerden.host(): MadensVerden,
    Madsvin.host(): Madsvin,
    Magimix.host(): Magimix,
    MakeItDairyFree.host(): MakeItDairyFree,
    Marmiton.host(): Marmiton,
    MarthaStewart.host(): MarthaStewart,
    Matprat.host(): Matprat,
    McCormick.host(): McCormick,
    MealPrepManual.host(): MealPrepManual,
    MeganVsKitchen.host(): MeganVsKitchen,
    Meljoulwan.host(): Meljoulwan,
    MellisaKNorris.host(): MellisaKNorris,
    MellosChourico.host(): MellosChourico,
    MelsKitchenCafe.host(): MelsKitchenCafe,
    Migusto.host(): Migusto,
    Miljuschka.host(): Miljuschka,
    Mindmegette.host(): Mindmegette,
    Minimalistbaker.host(): Minimalistbaker,
    MinistryOfCurry.host(): MinistryOfCurry,
    Misya.host(): Misya,
    Mob.host(): Mob,
    MobKitchen.host(): MobKitchen,
    ModernHoney.host(): ModernHoney,
    MomOnTimeout.host(): MomOnTimeout,
    MomsWithCrockPots.host(): MomsWithCrockPots,
    MotherThyme.host(): MotherThyme,
    Moulinex.host(): Moulinex,
    MundoDeReceitasBimby.host(): MundoDeReceitasBimby,
    MyBakingAddiction.host(): MyBakingAddiction,
    MyJewishLearning.host(): MyJewishLearning,
    MyKitchen101.host(): MyKitchen101,
    MyKitchen101en.host(): MyKitchen101en,
    MyKoreanKitchen.host(): MyKoreanKitchen,
    MyRecipes.host(): MyRecipes,
    MyriadRecipes.host(): MyriadRecipes,
    MyVegetarianRoots.host(): MyVegetarianRoots,
    NatashasKitchen.host(): NatashasKitchen,
    NaturallyElla.host(): NaturallyElla,
    Ndr.host(): Ndr,
    NetaCooks.host(): NetaCooks,
    NHSHealthierFamilies.host(): NHSHealthierFamilies,
    NibbleDish.host(): NibbleDish,
    NIHHealthyEating.host(): NIHHealthyEating,
    NinjaTestKitchen.host(): NinjaTestKitchen,
    NoraCooks.host(): NoraCooks,
    NoRecipes.host(): NoRecipes,
    NoSalty.host(): NoSalty,
    NotEnoughCinnamon.host(): NotEnoughCinnamon,
    NourishedByNutrition.host(): NourishedByNutrition,
    NRKMat.host(): NRKMat,
    Number2Pencil.host(): Number2Pencil,
    NutritionByNathalie.host(): NutritionByNathalie,
    NutritionFacts.host(): NutritionFacts,
    NYTimes.host(): NYTimes,
    OhSheGlows.host(): OhSheGlows,
    OhSweetBasil.host(): OhSweetBasil,
    OkokoRecepten.host(): OkokoRecepten,
    OmnivoresCookbook.host(): OmnivoresCookbook,
    OnceUponAChef.host(): OnceUponAChef,
    OneHundredOneCookBooks.host(): OneHundredOneCookBooks,
    OneSweetAppetite.host(): OneSweetAppetite,
    OrganicallyAddison.host(): OrganicallyAddison,
    OttolenghiBooks.host(): OttolenghiBooks,
    OurBestBites.host(): OurBestBites,
    OwenHan.host(): OwenHan,
    PaleoRunningMomma.host(): PaleoRunningMomma,
    Panelinha.host(): Panelinha,
    PaniniHappy.host(): PaniniHappy,
    PanlasangPinoy.host(): PanlasangPinoy,
    PeelWithZeal.host(): PeelWithZeal,
    PersnicketyPlates.host(): PersnicketyPlates,
    PickUpLimes.host(): PickUpLimes,
    Picnic.host(): Picnic,
    PiesAndPlots.host(): PiesAndPlots,
    PilipinasRecipes.host(): PilipinasRecipes,
    PinchOfYum.host(): PinchOfYum,
    PingoDoce.host(): PingoDoce,
    PinkOwlKitchen.host(): PinkOwlKitchen,
    PlatingPixels.host(): PlatingPixels,
    PlowingThroughLife.host(): PlowingThroughLife,
    PolishFoodies.host(): PolishFoodies,
    PoppyCooks.host(): PoppyCooks,
    PopSugar.host(): PopSugar,
    PotatoRolls.host(): PotatoRolls,
    PracticalSelfReliance.host(): PracticalSelfReliance,
    PreppyKitchen.host(): PreppyKitchen,
    PressureLuckCooking.host(): PressureLuckCooking,
    PrimalEdgeHealth.host(): PrimalEdgeHealth,
    ProjectGezond.host(): ProjectGezond,
    Przepisy.host(): Przepisy,
    PurelyPope.host(): PurelyPope,
    PurpleCarrot.host(): PurpleCarrot,
    QuakerOats.host(): QuakerOats,
    QuiToque.host(): QuiToque,
    RachlMansfield.host(): RachlMansfield,
    RainbowPlantLife.host(): RainbowPlantLife,
    RealFoodTesco.host(): RealFoodTesco,
    RealFoodWell.host(): RealFoodWell,
    RealMomNutrition.host(): RealMomNutrition,
    RealSimple.host(): RealSimple,
    ReceitasNestleBR.host(): ReceitasNestleBR,
    Recept.host(): Recept,
    ReceptiIndex.host(): ReceptiIndex,
    ReceptyPreVas.host(): ReceptyPreVas,
    RecettePlus.host(): RecettePlus,
    RecipeGirl.host(): RecipeGirl,
    RecipeLand.host(): RecipeLand,
    RecipeRunner.host(): RecipeRunner,
    RecipeTinEats.host(): RecipeTinEats,
    RedHouseSpice.host(): RedHouseSpice,
    Reishunger.host(): Reishunger,
    Rewe.host(): Rewe,
    Rezeptwelt.host(): Rezeptwelt,
    Ricetta.host(): Ricetta,
    RicettePerBimby.host(): RicettePerBimby,
    RosannaPansino.host(): RosannaPansino,
    RutgerBakt.host(): RutgerBakt,
    SaboresAjinomoto.host(): SaboresAjinomoto,
    SallysBakingAddiction.host(): SallysBakingAddiction,
    SallysBlog.host(): SallysBlog,
    SaltPepperSkillet.host(): SaltPepperSkillet,
    SamsungFood.host(): SamsungFood,
    SandwhichTribunal.host(): SandwhichTribunal,
    Saveur.host(): Saveur,
    SavoringTheGood.host(): SavoringTheGood,
    SavoryNothings.host(): SavoryNothings,
    SavvySavingCouple.host(): SavvySavingCouple,
    SchoolOfWok.host(): SchoolOfWok,
    ScrambledAndScrumptious.host(): ScrambledAndScrumptious,
    ScrummyLane.host(): ScrummyLane,
    SeriousEats.host(): SeriousEats,
    SharkNinja.host(): SharkNinja,
    SheLikesFood.host(): SheLikesFood,
    SimpleGreenSmoothies.host(): SimpleGreenSmoothies,
    SimpleHomeEdit.host(): SimpleHomeEdit,
    SimpleVeganista.host(): SimpleVeganista,
    SimplyCookit.host(): SimplyCookit,
    SimplyQuinoa.host(): SimplyQuinoa,
    SimplyRecipes.host(): SimplyRecipes,
    SimplyWhisked.host(): SimplyWhisked,
    SipAndFeast.host(): SipAndFeast,
    SizzleFish.host(): SizzleFish,
    SizzlingEats.host(): SizzlingEats,
    SkinnyTaste.host(): SkinnyTaste,
    SmallTownWoman.host(): SmallTownWoman,
    Smulweb.host(): Smulweb,
    SoBors.host(): SoBors,
    SouthernCastIron.host(): SouthernCastIron,
    SouthernLiving.host(): SouthernLiving,
    SpainOnAFork.host(): SpainOnAFork,
    SpendWithPennies.host(): SpendWithPennies,
    SpicySouthernKitchen.host(): SpicySouthernKitchen,
    SpisBedre.host(): SpisBedre,
    Springlane.host(): Springlane,
    StacyLing.host(): StacyLing,
    StaySnatched.host(): StaySnatched,
    SteamyKitchen.host(): SteamyKitchen,
    StreetKitchen.host(): StreetKitchen,
    StrongrFastr.host(): StrongrFastr,
    SudachiRecipes.host(): SudachiRecipes,
    SugarHero.host(): SugarHero,
    SunBasket.host(): SunBasket,
    SundPaaBudget.host(): SundPaaBudget,
    Sunset.host(): Sunset,
    SweetCsDesigns.host(): SweetCsDesigns,
    SweetPeasAndSaffron.host(): SweetPeasAndSaffron,
    SwissMilk.host(): SwissMilk,
    TableAndDish.host(): TableAndDish,
    TasteAtlas.host(): TasteAtlas,
    TasteAU.host(): TasteAU,
    TasteOfHome.host(): TasteOfHome,
    TastesBetterFromScratch.host(): TastesBetterFromScratch,
    TastesOfLizzyT.host(): TastesOfLizzyT,
    TastingHistory.host(): TastingHistory,
    Tasty.host(): Tasty,
    TastyKitchen.host(): TastyKitchen,
    TastyOven.host(): TastyOven,
    TatyanasEverydayFood.host(): TatyanasEverydayFood,
    TheAlmondEater.host(): TheAlmondEater,
    TheBigMansWorld.host(): TheBigMansWorld,
    TheCleverCarrot.host(): TheCleverCarrot,
    TheCookieRookie.host(): TheCookieRookie,
    TheCookingGuy.host(): TheCookingGuy,
    TheFirstMess.host(): TheFirstMess,
    TheFoodieTakesFlight.host(): TheFoodieTakesFlight,
    TheGlutenFreeAustrian.host(): TheGlutenFreeAustrian,
    TheHappyFoodie.host(): TheHappyFoodie,
    TheIceCreamConfectionals.host(): TheIceCreamConfectionals,
    TheKitchenCommunity.host(): TheKitchenCommunity,
    TheKitchenMagPie.host(): TheKitchenMagPie,
    TheKitchn.host(): TheKitchn,
    TheLoopyWhisk.host(): TheLoopyWhisk,
    TheMagicalSlowCooker.host(): TheMagicalSlowCooker,
    TheMediterraneDish.host(): TheMediterraneDish,
    TheModernProper.host(): TheModernProper,
    TheOldWomanAndTheSea.host(): TheOldWomanAndTheSea,
    ThePalatableLife.host(): ThePalatableLife,
    ThePioneerWoman.host(): ThePioneerWoman,
    ThePlantBasedSchool.host(): ThePlantBasedSchool,
    TheRecipeCritic.host(): TheRecipeCritic,
    TheSaltyMarshmallow.host(): TheSaltyMarshmallow,
    TheSpiceTrain.host(): TheSpiceTrain,
    TheSpruceEats.host(): TheSpruceEats,
    TheSuburbanSoapBox.host(): TheSuburbanSoapBox,
    TheVintageMixer.host(): TheVintageMixer,
    Thewoksoflife.host(): Thewoksoflife,
    Thinlicious.host(): Thinlicious,
    ThisHealthyTable.host(): ThisHealthyTable,
    TidyMom.host(): TidyMom,
    TimesOfIndia.host(): TimesOfIndia,
    TineNo.host(): TineNo,
    Tofoo.host(): Tofoo,
    ToriAvey.host(): ToriAvey,
    TudoGostoso.host(): TudoGostoso,
    TwentyFourKitchen.host(): TwentyFourKitchen,
    TwoPeasAndTheirPod.host(): TwoPeasAndTheirPod,
    UitPaulinesKeukenNL.host(): UitPaulinesKeukenNL,
    Unsophisticook.host(): Unsophisticook,
    USAPears.host(): USAPears,
    USDAMyPlate.host(): USDAMyPlate,
    Valdemarsro.host(): Valdemarsro,
    VanillaAndBean.host(): VanillaAndBean,
    VarechaPravdaSK.host(): VarechaPravdaSK,
    Vegetarbloggen.host(): Vegetarbloggen,
    Vegolosi.host(): Vegolosi,
    VegRecipesOfIndia.host(): VegRecipesOfIndia,
    VeroniqueCloutier.host(): VeroniqueCloutier,
    Waitrose.host(): Waitrose,
    WatchWhatUEat.host(): WatchWhatUEat,
    WDR.host(): WDR,
    WeAreNotMartha.host(): WeAreNotMartha,
    WeDishItUp.host(): WeDishItUp,
    WeightWatchers.host(): WeightWatchers,
    WeightWatchersPublic.host(): WeightWatchersPublic,
    WellPlated.host(): WellPlated,
    WhatsGabyCooking.host(): WhatsGabyCooking,
    Whole30.host(): Whole30,
    WholeFoods.host(): WholeFoods,
    WholeFoods.host(domain="co.uk"): WholeFoods,
    WikiCookbook.host(): WikiCookbook,
    WilliamsSonoma.host(): WilliamsSonoma,
    WomensWeeklyFood.host(): WomensWeeklyFood,
    Woop.host(): Woop,
    WyseGuide.host(): WyseGuide,
    Xiachufang.host(): Xiachufang,
    Yamasa.host(): Yamasa,
    Yemek.host(): Yemek,
    Yummly.host(): Yummly,
    ZauberTopf.host(): ZauberTopf,
    ZeitWochenmarkt.host(): ZeitWochenmarkt,
    ZenBelly.host(): ZenBelly,
    ZestfulKitchen.host(): ZestfulKitchen,
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
    best_image: bool | None = None,
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
        best_image (bool | None): whether to prefer the highest-quality image when multiple
            are available. Defaults to the configured setting when not provided.

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
        return SCRAPERS[host_name](html=html, url=org_url, best_image=best_image)

    if supported_only in (None, True):
        msg = (
            f"The website '{host_name}' isn't currently supported by recipe-scrapers!\n"
            "---\n"
            "If you have time to help us out, please report this as a feature \n"
            "request on our bugtracker."
        )
        raise WebsiteNotImplementedError(msg)

    schema_scraper = SchemaScraperFactory.generate(
        html=html, url=org_url, best_image=best_image
    )
    if schema_scraper.schema.data:
        return schema_scraper

    raise NoSchemaFoundInWildMode(org_url)


def scrape_me(url: str) -> AbstractScraper:
    html = urlopen(Request(url, headers=HEADERS)).read().decode("utf-8")
    return scrape_html(html, org_url=url)
