.. image:: https://img.shields.io/github/stars/hhursev/recipe-scrapers?style=social
    :target: https://github.com/hhursev/recipe-scrapers/
    :alt: Github
.. image:: https://img.shields.io/pypi/v/recipe-scrapers.svg?
    :target: https://pypi.org/project/recipe-scrapers/
    :alt: Version
.. image:: https://img.shields.io/pypi/pyversions/recipe-scrapers
    :target: https://pypi.org/project/recipe-scrapers/
    :alt: PyPI - Python Version
.. image:: https://pepy.tech/badge/recipe-scrapers
    :target: https://pepy.tech/project/recipe-scrapers
    :alt: Downloads
.. image:: https://github.com/hhursev/recipe-scrapers/workflows/unittests/badge.svg?branch=main
    :target: https://github.com/hhursev/recipe-scrapers/actions/
    :alt: GitHub Actions Unittests
.. image:: https://coveralls.io/repos/hhursev/recipe-scraper/badge.svg?branch=main&service=github
    :target: https://coveralls.io/github/hhursev/recipe-scraper?branch=main
    :alt: Coveralls
.. image:: https://img.shields.io/github/license/hhursev/recipe-scrapers?
    :target: https://github.com/hhursev/recipe-scrapers/blob/main/LICENSE
    :alt: License
.. image:: https://app.codacy.com/project/badge/Grade/3ee8da77aaa3475a8085ca22287dea89
    :target: https://app.codacy.com/gh/hhursev/recipe-scrapers/dashboard
    :alt: Codacy Badge


------


A simple scraping tool for recipe webpages.


Netiquette
----------

If you're using this library to collect large numbers of recipes from the web, please use the software responsibly and try to avoid creating high volumes of network traffic.

Python's standard library provides a ``robots.txt`` `parser <https://docs.python.org/3/library/urllib.robotparser.html>`_ that may be helpful to automatically follow common instructions specified by websites for web crawlers.

Another parser option -- particularly if you find that many web requests from ``urllib.robotparser`` are blocked -- is the `robotexclusionrulesparser <https://pypi.org/project/robotexclusionrulesparser/>`_ library.


Getting Started
---------------

Start by using `Python's built-in package installer <https://docs.python.org/3/installing/index.html>`_, ``pip``, to install the library:

.. code:: shell

    python -m pip install recipe-scrapers

This should produce output about the installation process, with the final line reading: ``Successfully installed recipe-scrapers-<version-number>``.

To learn what the library can do, you can open a `Python interpreter session <https://docs.python.org/3/tutorial/interpreter.html>`_, and then begin typing -- and/or modifying -- the statements below (on the lines containing the ``>>>`` prompt):

.. code:: pycon

    Python 4.0.4 (main, Oct 26 1985, 09:00:32) [GCC 22.3.4] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from recipe_scrapers import scrape_html
    >>> url = "https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/"
    >>> name = input('What is your name, burger seeker?\n')
    >>> html = requests.get(url, headers={"User-Agent": f"Burger Seeker {name}"}).content
    >>> scraper = scrape_html(html, org_url=url)
    >>> help(scraper)

Some Python HTTP clients that you can use to retrieve HTML include `requests`_, `httpx`_, and the `urllib.request module`_ included in Python's standard library.  Please refer to their documentation to find out what options (timeout configuration, proxy support, etc) are available.

.. _requests: https://pypi.org/project/requests/

.. _httpx: https://pypi.org/project/httpx/

.. _urllib.request module: https://docs.python.org/3/library/urllib.request.html


Scrapers available for:
-----------------------

- `https://101cookbooks.com/ <https://101cookbooks.com/>`_
- `https://15gram.be <https://15gram.be>`_
- `https://www.750g.com <https://www.750g.com>`_
- `https://aberlehome.com/ <https://aberlehome.com>`_
- `https://abuelascounter.com/ <https://abuelascounter.com>`_
- `https://www.acouplecooks.com <https://acouplecooks.com/>`_
- `https://addapinch.com/ <https://addapinch.com/>`_
- `http://www.afghankitchenrecipes.com/ <http://www.afghankitchenrecipes.com/>`_
- `https://aflavorjournal.com/ <https://aflavorjournal.com/>`_
- `https://ah.nl/ <https://ah.nl/>`_
- `https://akispetretzikis.com/ <https://akispetretzikis.com/>`_
- `https://aldi.com.au/ <https://aldi.com.au/>`_
- `https://alexandracooks.com/ <https://alexandracooks.com/>`_
- `https://alittlebityummy.com/ <https://alittlebityummy.com/>`_
- `https://allrecipes.com/ <https://allrecipes.com/>`_
- `https://allthehealthythings.com/ <https://allthehealthythings.com/>`_
- `https://alltommat.se/ <https://alltommat.se/>`_
- `https://altonbrown.com/ <https://altonbrown.com/>`_
- `https://amazingribs.com/ <https://amazingribs.com/>`_
- `https://ambitiouskitchen.com/ <https://ambitiouskitchen.com>`_
- `https://archanaskitchen.com/ <https://archanaskitchen.com/>`_
- `https://www.argiro.gr/ <https://www.argiro.gr/>`_
- `https://www.arla.se/ <https://www.arla.se/>`_
- `https://www.atelierdeschefs.fr/ <https://www.atelierdeschefs.fr/>`_
- `https://averiecooks.com/ <https://www.averiecooks.com/>`_
- `https://www.bakels.com.au/ <https://www.bakels.com.au/>`_
    - `.co.uk <https://bakels.co.uk/>`_
- `https://baking-sense.com/ <https://baking-sense.com/>`_
- `https://bakingmischief.com/ <https://bakingmischief.com/>`_
- `https://barefeetinthekitchen.com/ <https://barefeetinthekitchen.com/>`_
- `https://barefootcontessa.com/ <https://barefootcontessa.com>`_
- `https://bbc.com/ <https://bbc.com/food/recipes>`_
    - `.co.uk <https://bbc.co.uk/food/recipes>`__
- `https://bbcgoodfood.com/ <https://bbcgoodfood.com>`_
- `https://bestrecipes.com.au/ <https://bestrecipes.com.au>`_
- `https://bettybossi.ch/ <https://bettybossi.ch>`_
- `https://bettycrocker.com/ <https://bettycrocker.com>`_
- `https://biancazapatka.com/ <https://biancazapatka.com>`_
- `https://bigoven.com/ <https://bigoven.com>`_
- `https://blueapron.com/ <https://blueapron.com>`_
- `https://bluejeanchef.com/ <https://bluejeanchef.com/>`_
- `https://www.bodybuilding.com/ <https://www.bodybuilding.com/>`_
- `https://bonappetit.com/ <https://bonappetit.com>`_
- `https://bongeats.com/ <https://bongeats.com/>`_
- `https://books.ottolenghi.co.uk <https://books.ottolenghi.co.uk/>`_ (*)
- `https://bowlofdelicious.com/ <https://bowlofdelicious.com/>`_
- `https://breadtopia.com/ <https://breadtopia.com/>`_
- `https://briceletbaklava.ch/ <https://briceletbaklava.ch/>`_
- `https://budgetbytes.com/ <https://budgetbytes.com>`_
- `https://cafedelites.com/ <https://cafedelites.com/>`_
- `https://carlsbadcravings.com/ <https://carlsbadcravings.com/>`_
- `https://castironketo.net/ <https://castironketo.net/>`_
- `https://cdkitchen.com/ <https://cdkitchen.com/>`_
- `https://celebratingsweets.com/ <https://celebratingsweets.com/>`_
- `https://chefkoch.de/ <https://chefkoch.de>`_
- `https://www.chefnini.com/ <https://www.chefnini.com/>`_
- `https://chefsavvy.com/ <https://chefsavvy.com/>`_
- `https://claudia.abril.com.br/ <https://claudia.abril.com.br>`_
- `https://closetcooking.com/ <https://closetcooking.com>`_
- `https://comidinhasdochef.com/ <https://comidinhasdochef.com/>`_
- `https://cook-talk.com/ <https://cook-talk.com/>`_
- `https://cookeatshare.com/ <https://cookeatshare.com/>`_
- `https://cookieandkate.com/ <https://cookieandkate.com/>`_
- `https://cooking.nytimes.com/ <https://cooking.nytimes.com>`_
- `https://cookingcircle.com/ <https://cookingcircle.com/>`_
- `https://cookinglight.com/ <https://cookinglight.com/>`_
- `https://cookpad.com/ <https://cookpad.com/>`_
- `https://www.coop.se/ <https://www.coop.se/>`_
- `https://copykat.com/ <https://copykat.com>`_
- `https://www.costco.com/ <https://www.costco.com>`_
- `https://countryliving.com/ <https://countryliving.com>`_
- `https://creativecanning.com/ <https://creativecanning.com>`_
- `https://cucchiaio.it/ <https://cucchiaio.it>`_
- `https://cuisineaz.com/ <https://cuisineaz.com>`_
- `https://cybercook.com.br/ <https://cybercook.com.br/>`_
- `https://damndelicious.net/ <https://damndelicious.net/>`_
- `https://www.davidlebovitz.com/ <https://www.davidlebovitz.com/>`_
- `https://delish.com/ <https://delish.com>`_
- `https://dinneratthezoo.com/ <https://dinneratthezoo.com>`_
- `https://dinnerthendessert.com/ <https://dinnerthendessert.com/>`_
- `https://dish.co.nz/ <https://dish.co.nz>`_
- `https://dobruchut.aktuality.sk/ <https://dobruchut.aktuality.sk>`_
- `https://domesticate-me.com/ <https://domesticate-me.com/>`_
- `https://donalskehan.com/ <https://donalskehan.com/>`_
- `https://downshiftology.com/ <https://downshiftology.com/>`_
- `https://www.dr.dk/ <https://www.dr.dk/>`_
- `https://www.eatingbirdfood.com/ <https://www.eatingbirdfood.com>`_
- `https://www.eatingwell.com/ <https://www.eatingwell.com>`_
- `https://www.eatliverun.com/ <https://www.eatliverun.com/>`_
- `https://eatsmarter.com/ <https://eatsmarter.com/>`_
    - `.de <https://eatsmarter.de/>`__
- `https://eatthismuch.com/ <https://eatthismuch.com/>`_
- `https://eattolerant.de/ <https://eattolerant.de/>`_
- `https://www.eatwell101.com <https://www.eatwell101.com>`_
- `https://eatwhattonight.com/ <https://eatwhattonight.com/>`_
- `https://elavegan.com/ <https://elavegan.com/>`_
- `https://emmikochteinfach.de/ <https://emmikochteinfach.de/>`_
- `https://en.wikibooks.org/ <https://en.wikibooks.org>`_
- `https://epicurious.com/ <https://epicurious.com>`_
- `https://www.errenskitchen.com/ <https://www.errenskitchen.com/>`_
- `https://ethanchlebowski.com/ <https://ethanchlebowski.com>`_
- `https://www.evolvingtable.com/ <https://www.evolvingtable.com/>`_
- `https://www.familyfoodonthetable.com/ <https://www.familyfoodonthetable.com/>`_
- `https://www.farmhouseonboone.com/ <https://www.farmhouseonboone.com/>`_
- `https://www.fattoincasadabenedetta.it/ <https://www.fattoincasadabenedetta.it/>`_
- `https://felix.kitchen <https://felix.kitchen>`_
- `https://fifteenspatulas.com/ <https://www.fifteenspatulas.com/>`_
- `https://finedininglovers.com/ <https://www.finedininglovers.com>`_
- `https://fitmencook.com/ <https://www.fitmencook.com>`_
- `https://fitslowcookerqueen.com <https://fitslowcookerqueen.com/>`_
- `https://food.com/ <https://www.food.com>`_
- `https://food52.com/ <https://www.food52.com>`_
- `https://foodandwine.com/ <https://www.foodandwine.com>`_
- `https://foodfidelity.com/ <https://foodfidelity.com>`_
- `https://foodnetwork.co.uk/ <https://www.foodnetwork.co.uk>`_
    - `.com <https://www.foodnetwork.com>`__
- `https://foodrepublic.com/ <https://foodrepublic.com>`_
- `https://www.forksoverknives.com/ <https://www.forksoverknives.com/>`_
- `https://forktospoon.com/ <https://forktospoon.com/>`_
- `https://franzoesischkochen.de/ <https://franzoesischkochen.de/>`_
- `https://www.gesund-aktiv.com/ <https://www.gesund-aktiv.com>`_
- `https://gimmesomeoven.com/ <https://www.gimmesomeoven.com/>`_
- `https://glutenfreeonashoestring.com/ <https://glutenfreeonashoestring.com/>`_
- `https://godt.no/ <https://godt.no/>`_
- `https://gonnawantseconds.com/ <https://gonnawantseconds.com>`_
- `https://goodfooddiscoveries.com/ <https://goodfooddiscoveries.com/>`_
- `https://goodhousekeeping.com/ <https://www.goodhousekeeping.com/>`_
- `https://gourmettraveller.com.au/ <https://gourmettraveller.com.au>`_
- `https://gousto.co.uk/ <https://gousto.co.uk>`_
- `https://www.grandfrais.com/ <https://www.grandfrais.com>`_
- `https://greatbritishchefs.com/ <https://greatbritishchefs.com>`_
- `https://grimgrains.com/ <https://grimgrains.com>`_
- `http://www.grouprecipes.com/ <http://www.grouprecipes.com/>`_
- `https://halfbakedharvest.com/ <https://www.halfbakedharvest.com/>`_
- `https://handletheheat.com/ <https://handletheheat.com/>`_
- `https://www.hassanchef.com/ <https://www.hassanchef.com/>`_
- `https://headbangerskitchen.com/ <https://www.headbangerskitchen.com/>`_
- `https://healthyeating.nhlbi.nih.gov/ <https://healthyeating.nhlbi.nih.gov>`_
- `https://heatherchristo.com/ <https://heatherchristo.com/>`_
- `https://www.heb.com/ <https://www.heb.com/recipe/landing>`_
- `https://hellofresh.com/ <https://hellofresh.com>`_
    - `.at <https://www.hellofresh.at/>`__, `.be <https://www.hellofresh.be/>`__, `.ca <https://www.hellofresh.ca/>`__, `.ch <https://www.hellofresh.ch/>`__, `.co.nz <https://www.hellofresh.co.nz/>`__, `.co.uk <https://hellofresh.co.uk>`__, `.com.au <https://www.hellofresh.com.au/>`__, `.de <https://www.hellofresh.de/>`__, `.dk <https://www.hellofresh.dk/>`__, `.es <https://www.hellofresh.es/>`__, `.fr <https://www.hellofresh.fr/>`__, `.ie <https://www.hellofresh.ie/>`__, `.it <https://www.hellofresh.it/>`__, `.lu <https://www.hellofresh.lu/>`__, `.nl <https://www.hellofresh.nl/>`__, `.no <https://www.hellofresh.no/>`__, `.se <https://www.hellofresh.se/>`__
- `https://www.hersheyland.com/ <https://www.hersheyland.com/>`_
- `https://www.homechef.com/ <https://www.homechef.com/>`_
- `https://hostthetoast.com/ <https://hostthetoast.com/>`_
- `https://www.ica.se/ <https://www.ica.se/>`_
- `https://www.im-worthy.com/ <https://www.im-worthy.com>`_
- `https://inbloombakery.com/ <https://inbloombakery.com/>`_
- `https://indianhealthyrecipes.com <https://www.indianhealthyrecipes.com>`_
- `https://ingoodflavor.com <https://www.ingoodflavor.com>`_
- `https://www.innit.com/ <https://www.innit.com/>`_
- `https://insanelygoodrecipes.com <https://insanelygoodrecipes.com/>`_
- `https://inspiralized.com/ <https://inspiralized.com>`_
- `https://izzycooking.com/ <https://izzycooking.com/>`_
- `https://jamieoliver.com/ <https://jamieoliver.com>`_
- `https://jimcooksfoodgood.com/ <https://jimcooksfoodgood.com/>`_
- `https://www.jocooks.com/ <https://www.jocooks.com>`_
- `https://joshuaweissman.com/ <https://joshuaweissman.com/>`_
- `https://joyfoodsunshine.com/ <https://joyfoodsunshine.com>`_
- `https://joythebaker.com/ <https://joythebaker.com>`_
- `https://juliegoodwin.com.au/ <https://juliegoodwin.com.au>`_
- `https://justataste.com/ <https://justataste.com>`_
- `https://justbento.com/ <https://justbento.com>`_
- `https://www.justonecookbook.com/ <https://www.justonecookbook.com>`_
- `https://kalejunkie.com/ <https://kalejunkie.com/>`_
- `https://kennymcgovern.com/ <https://kennymcgovern.com>`_
- `https://keukenliefde.nl/ <https://keukenliefde.nl>`_
- `https://www.kingarthurbaking.com <https://www.kingarthurbaking.com>`_
- `https://kitchenaid.com.au/ <https://kitchenaid.com.au/blogs/kitchenthusiast/tagged/blog-category-recipes>`_
- `https://www.kitchendreaming.com <https://www.kitchendreaming.com>`_
- `https://www.kitchensanctuary.com/ <https://www.kitchensanctuary.com>`_
- `https://www.kitchenstories.com/ <https://www.kitchenstories.com>`_
- `https://kochbar.de/ <https://kochbar.de>`_
- `https://kochbucher.com/ <https://kochbucher.com/>`_
- `http://koket.se/ <http://koket.se>`_
- `https://kristineskitchenblog.com/ <https://kristineskitchenblog.com>`_
- `https://kuchnia-domowa.pl/ <https://www.kuchnia-domowa.pl/>`_
- `https://kuchynalidla.sk/ <https://www.kuchynalidla.sk/>`_
- `https://www.kwestiasmaku.com/ <https://www.kwestiasmaku.com/>`_
- `https://www.latelierderoxane.com <https://www.latelierderoxane.com/blog/recettes/>`_
- `https://leanandgreenrecipes.net <https://leanandgreenrecipes.net>`_
- `https://www.lecker.de <https://www.lecker.de/rezepte>`_
- `https://lecremedelacrumb.com/ <https://lecremedelacrumb.com/>`_
- `https://leitesculinaria.com <https://leitesculinaria.com>`_
- `https://lekkerensimpel.com <https://lekkerensimpel.com>`_
- `https://leukerecepten.nl/ <https://www.leukerecepten.nl>`_
- `https://lifestyleofafoodie.com <https://lifestyleofafoodie.com>`_
- `https://littlespicejar.com/ <https://littlespicejar.com>`_
- `https://littlesunnykitchen.com/ <https://littlesunnykitchen.com>`_
- `http://livelytable.com/ <http://livelytable.com/>`_
- `https://lovingitvegan.com/ <https://lovingitvegan.com/>`_
- `https://www.maangchi.com <https://www.maangchi.com>`_
- `https://madensverden.dk/ <https://madensverden.dk/>`_
- `https://www.madewithlau.com/ <https://www.madewithlau.com/>`_
- `https://madsvin.com/ <https://madsvin.com/>`_
- `https://marleyspoon.com/ <https://marleyspoon.com/>`_
    - `.at <https://marleyspoon.at/>`__, `.be <https://marleyspoon.be/>`__, `.com.au <https://marleyspoon.com.au/>`__, `.de <https://marleyspoon.de/>`__, `.nl <https://marleyspoon.nl/>`__, `.se <https://marleyspoon.se/>`__
- `https://marmiton.org/ <https://marmiton.org/>`_
- `https://www.marthastewart.com/ <https://www.marthastewart.com/>`_
- `https://matprat.no/ <https://matprat.no/>`_
- `https://www.mccormick.com/ <https://www.mccormick.com/>`_
- `https://meljoulwan.com/ <https://meljoulwan.com/>`_
- `https://www.melskitchencafe.com/ <https://www.melskitchencafe.com/>`_
- `https://www.miljuschka.nl/ <https://www.miljuschka.nl/>`_
- `http://mindmegette.hu/ <http://mindmegette.hu/>`_
- `https://minimalistbaker.com/ <https://minimalistbaker.com/>`_
- `https://ministryofcurry.com/ <https://ministryofcurry.com/>`_
- `https://misya.info/ <https://misya.info>`_
- `https://www.mob.co.uk/ <https://www.mob.co.uk/>`_
- `https://mobile.kptncook.com/ <https://mobile.kptncook.com/>`_
- `https://mobkitchen.co.uk/ <https://mobkitchen.co.uk/>`_
- `https://www.modernhoney.com/ <https://www.modernhoney.com/>`_
- `https://www.momontimeout.com/ <https://www.momontimeout.com/>`_
- `https://momswithcrockpots.com/ <https://momswithcrockpots.com>`_
- `https://monsieur-cuisine.com/ <https://monsieur-cuisine.com>`_
- `http://motherthyme.com/ <http://motherthyme.com/>`_
- `https://www.moulinex.fr/ <https://www.moulinex.fr/>`_
- `https://www.mundodereceitasbimby.com.pt/ <https://www.mundodereceitasbimby.com.pt/>`_
- `https://mybakingaddiction.com/ <https://mybakingaddiction.com>`_
- `https://myjewishlearning.com/ <https://myjewishlearning.com>`_
- `https://mykitchen101.com/ <https://mykitchen101.com>`_
- `https://mykitchen101en.com/ <https://mykitchen101en.com>`_
- `https://mykoreankitchen.com/ <https://mykoreankitchen.com>`_
- `https://www.myplate.gov/ <https://www.myplate.gov/>`_
- `https://myrecipes.com/ <https://myrecipes.com>`_
- `https://myvegetarianroots.com/ <https://myvegetarianroots.com/>`_
- `https://www.nhs.uk/healthier-families/ <https://www.nhs.uk/healthier-families/>`_
- `https://nibbledish.com/ <https://nibbledish.com>`_
- `https://norecipes.com/ <https://norecipes.com/>`_
- `https://nosalty.hu/ <https://nosalty.hu/>`_
- `https://www.notenoughcinnamon.com/ <https://www.notenoughcinnamon.com/>`_
- `https://nourishedbynutrition.com/ <https://nourishedbynutrition.com/>`_
- `https://www.nrk.no/ <https://www.nrk.no/>`_
- `https://www.number-2-pencil.com/ <https://www.number-2-pencil.com/>`_
- `https://nutritionbynathalie.com/blog <https://nutritionbynathalie.com/blog>`_
- `https://nutritionfacts.org/ <https://nutritionfacts.org/>`_
- `https://ohsheglows.com/ <https://ohsheglows.com>`_
- `https://omnivorescookbook.com <https://omnivorescookbook.com>`_
- `https://www.onceuponachef.com <https://www.onceuponachef.com>`_
- `https://onesweetappetite.com/ <https://onesweetappetite.com>`_
- `https://owen-han.com/ <https://owen-han.com>`_
- `https://www.paleorunningmomma.com/ <https://www.paleorunningmomma.com>`_
- `https://www.panelinha.com.br/ <https://www.panelinha.com.br>`_
- `https://paninihappy.com/ <https://paninihappy.com>`_
- `https://www.peelwithzeal.com/ <https://www.peelwithzeal.com/>`_
- `https://www.persnicketyplates.com/ <https://www.persnicketyplates.com/>`_
- `https://www.pickuplimes.com/ <https://www.pickuplimes.com/>`_
- `https://pinchofyum.com/ <https://pinchofyum.com/>`_
- `https://www.pingodoce.pt/ <https://www.pingodoce.pt>`_
- `https://pinkowlkitchen.com/ <https://pinkowlkitchen.com/>`_
- `https://www.platingpixels.com/ <https://www.platingpixels.com/>`_
- `https://plowingthroughlife.com/ <https://plowingthroughlife.com/>`_
- `https://popsugar.com/ <https://popsugar.com>`_
- `https://potatorolls.com/ <https://potatorolls.com/>`_
- `https://practicalselfreliance.com/ <https://practicalselfreliance.com>`_
- `https://pressureluckcooking.com/ <https://pressureluckcooking.com/>`_
- `https://www.primaledgehealth.com/ <https://www.primaledgehealth.com/>`_
- `https://www.projectgezond.nl/ <https://www.projectgezond.nl/>`_
- `https://przepisy.pl/ <https://przepisy.pl>`_
- `https://purelypope.com/ <https://purelypope.com>`_
- `https://purplecarrot.com/ <https://purplecarrot.com>`_
- `https://rachlmansfield.com/ <https://rachlmansfield.com>`_
- `https://rainbowplantlife.com/ <https://rainbowplantlife.com/>`_
- `https://realfood.tesco.com/ <https://realfood.tesco.com>`_
- `https://realsimple.com/ <https://www.realsimple.com>`_
- `https://receitas.globo.com/ <https://www.receitas.globo.com/>`_
- `https://receitas.ig.com.br/ <https://receitas.ig.com.br>`_
- `https://www.receitasnestle.com.br <https://www.receitasnestle.com.br>`_
- `https://recept.se/ <https://recept.se/>`_
- `https://receptyprevas.sk/ <https://receptyprevas.sk/>`_
- `https://www.recipegirl.com/ <https://www.recipegirl.com/>`_
- `https://reciperunner.com/ <https://www.reciperunner.com>`_
- `https://recipes.farmhousedelivery.com/ <https://recipes.farmhousedelivery.com/>`_
- `https://recipes.timesofindia.com/ <https://recipes.timesofindia.com/>`_
- `https://recipetineats.com/ <https://www.recipetineats.com/>`_
- `https://redhousespice.com/ <https://redhousespice.com/>`_
- `https://reishunger.de/ <https://www.reishunger.de/>`_
- `https://rezeptwelt.de/ <https://rezeptwelt.de>`_
- `https://ricetta.it/ <https://ricetta.it>`_
- `https://ricette.giallozafferano.it/ <https://ricette.giallozafferano.it>`_
- `https://www.ricetteperbimby.it/ <https://www.ricetteperbimby.it/>`_
- `https://rosannapansino.com <https://rosannapansino.com>`_
- `https://rutgerbakt.nl/ <https://rutgerbakt.nl/>`_
- `https://www.saboresajinomoto.com.br/ <https://www.saboresajinomoto.com.br/>`_
- `https://sallys-blog.de <https://sallys-blog.de/>`_
- `https://sallysbakingaddiction.com <https://sallysbakingaddiction.com/>`_
- `https://saltpepperskillet.com/ <https://saltpepperskillet.com/>`_
- `https://sandwichtribunal.com/ <https://sandwichtribunal.com/>`_
- `https://www.saveur.com/ <https://www.saveur.com/>`_
- `https://www.savorynothings.com/ <https://www.savorynothings.com/>`_
- `https://seriouseats.com/ <https://seriouseats.com>`_
- `https://sharing.kptncook.com/ <https://sharing.kptncook.com/>`_
- `https://simple-veganista.com/ <https://simple-veganista.com/>`_
- `https://simply-cookit.com/ <https://simply-cookit.com>`_
- `https://simplyquinoa.com/ <https://simplyquinoa.com>`_
- `https://simplyrecipes.com/ <https://simplyrecipes.com>`_
- `https://simplywhisked.com/ <https://simplywhisked.com>`_
- `https://skinnytaste.com/ <https://www.skinnytaste.com>`_
- `https://smulweb.nl/ <https://smulweb.nl>`_
- `https://sobors.hu/ <https://sobors.hu>`_
- `https://www.southerncastiron.com/ <https://www.southerncastiron.com>`_
- `https://southernliving.com/ <https://southernliving.com/>`_
- `https://spendwithpennies.com/ <https://spendwithpennies.com/>`_
- `https://www.springlane.de <https://www.springlane.de>`_
- `https://www.staysnatched.com/ <https://www.staysnatched.com/>`_
- `https://steamykitchen.com/ <https://steamykitchen.com>`_
- `https://streetkitchen.hu/ <https://streetkitchen.hu>`_
- `https://www.strongrfastr.com <https://www.strongrfastr.com>`_
- `https://sunbasket.com/ <https://sunbasket.com>`_
- `https://sundpaabudget.dk/ <https://sundpaabudget.dk>`_
- `https://www.sunset.com/ <https://www.sunset.com/>`_
- `https://sweetcsdesigns.com/ <https://www.sweetcsdesigns.com/>`_
- `https://sweetpeasandsaffron.com/ <https://sweetpeasandsaffron.com/>`_
- `https://www.taste.com.au/ <https://www.taste.com.au/>`_
- `https://www.tasteatlas.com/ <https://www.tasteatlas.com/>`_
- `https://tasteofhome.com <https://tasteofhome.com>`_
- `https://tastesbetterfromscratch.com <https://tastesbetterfromscratch.com>`_
- `https://tastesoflizzyt.com <https://tastesoflizzyt.com>`_
- `https://tasty.co <https://tasty.co>`_
- `https://tastykitchen.com/ <https://tastykitchen.com>`_
- `https://theclevercarrot.com/ <https://theclevercarrot.com>`_
- `https://www.thecookierookie.com/ <https://www.thecookierookie.com/>`_
- `https://thecookingguy.com/ <https://thecookingguy.com>`_
- `https://theexpertguides.com/ <https://theexpertguides.com>`_
- `https://theglutenfreeaustrian.com/ <https://theglutenfreeaustrian.com/>`_
- `https://thehappyfoodie.co.uk/ <https://thehappyfoodie.co.uk>`_
- `https://thekitchencommunity.org/ <https://thekitchencommunity.org/>`_
- `https://www.thekitchenmagpie.com/ <https://www.thekitchenmagpie.com>`_
- `https://thekitchn.com/ <https://thekitchn.com/>`_
- `https://theloopywhisk.com/ <https://theloopywhisk.com/>`_
- `https://www.themagicalslowcooker.com/ <https://www.themagicalslowcooker.com/>`_
- `https://themodernproper.com/ <https://themodernproper.com/>`_
- `https://www.thepalatablelife.com <https://www.thepalatablelife.com/>`_
- `https://thepioneerwoman.com/ <https://thepioneerwoman.com>`_
- `https://therecipecritic.com/ <https://therecipecritic.com>`_
- `https://thesaltymarshmallow.com/ <https://thesaltymarshmallow.com/>`_
- `https://thespruceeats.com/ <https://thespruceeats.com/>`_
- `https://thevintagemixer.com/ <https://thevintagemixer.com>`_
- `https://thewoksoflife.com/ <https://thewoksoflife.com/>`_
- `https://thinlicious.com/ <https://thinlicious.com/>`_
- `https://tidymom.net <https://tidymom.net>`_
- `https://tine.no/ <https://tine.no>`_
- `https://tofoo.co.uk <https://tofoo.co.uk>`_
- `https://tudogostoso.com.br/ <https://www.tudogostoso.com.br/>`_
- `https://twopeasandtheirpod.com/ <http://twopeasandtheirpod.com>`_
- `https://uitpaulineskeuken.nl/ <https://uitpaulineskeuken.nl>`_
- `https://unsophisticook.com/ <https://unsophisticook.com/>`_
- `https://usapears.org/ <https://usapears.org>`_
- `https://www.valdemarsro.dk/ <https://www.valdemarsro.dk/>`_
- `https://vanillaandbean.com/ <https://vanillaandbean.com>`_
- `https://varecha.pravda.sk/ <https://varecha.pravda.sk>`_
- `https://www.vegetarbloggen.no/ <https://www.vegetarbloggen.no/>`_
- `https://vegolosi.it/ <https://vegolosi.it>`_
- `https://vegrecipesofindia.com/ <https://www.vegrecipesofindia.com/>`_
- `https://www.waitrose.com/ <https://www.waitrose.com/>`_
- `https://watchwhatueat.com/ <https://watchwhatueat.com/>`_
- `https://wearenotmartha.com/ <https://wearenotmartha.com/>`_
- `https://www.weightwatchers.com/ <https://www.weightwatchers.com/>`_ (*)
- `https://www.wellplated.com/ <https://www.wellplated.com/>`_
- `https://whatsgabycooking.com/ <https://whatsgabycooking.com>`_
- `https://whole30.com/ <https://whole30.com/>`_
- `https://www.wholefoodsmarket.com/ <https://www.wholefoodsmarket.com/>`_
    - `.co.uk <https://www.wholefoodsmarket.co.uk/>`__
- `https://www.williams-sonoma.com/ <https://www.williams-sonoma.com/>`_
- `https://womensweeklyfood.com.au/ <https://womensweeklyfood.com.au/>`_
- `https://woolworths.com.au/shop/recipes <https://www.woolworths.com.au/shop/recipes/>`_
- `https://woop.co.nz/ <https://woop.co.nz/>`_
- `https://yemek.com/ <https://yemek.com>`_
- `https://yummly.com/ <https://yummly.com>`_ (*)
- `https://www.zaubertopf.de <https://www.zaubertopf.de>`_
- `https://zeit.de/ (wochenmarkt) <https://www.zeit.de/zeit-magazin/wochenmarkt/index>`_
- `https://zenbelly.com/ <https://zenbelly.com>`_

(*) offline saved files only


Contribute
----------

If you spot a design change (or something else) that makes the scraper unable to work for a given site - please fire an issue asap.

If you are programmer PRs with fixes are warmly welcomed and acknowledged with a virtual beer. You can find documentation on how to develop scrapers `here <https://github.com/hhursev/recipe-scrapers/blob/main/docs/README.md>`__.


If you want a scraper for a new site added
------------------------------------------

- Open an `Issue <https://github.com/hhursev/recipe-scraper/issues/new>`_ providing us the site name, as well as a recipe link from it.
- You are a developer and want to code the scraper on your own:

  - If `Schema is available <#faq>`_ on the site - `you can go like this. <https://github.com/hhursev/recipe-scrapers/pull/176>`_
  - Otherwise, scrape the HTML - `like this <https://github.com/hhursev/recipe-scrapers/commit/ffee963d04>`_
  - Generating a new scraper class:

    .. code:: shell

        python generate.py <ClassName> <URL>

    - **ClassName**: The name of the new scraper class.
    - **URL**: The URL of an example recipe from the target site. The content will be stored in ``test_data`` to be used with the test class.

    You can find a more detailed guide `here <https://github.com/hhursev/recipe-scrapers/blob/main/docs/how-to-develop-scraper.md>`__.


For Devs / Contribute
---------------------

Assuming you have ``>=python3.9`` installed, navigate to the directory where you want this project to live in and drop these lines

.. code:: shell

    git clone git@github.com:hhursev/recipe-scrapers.git &&
    cd recipe-scrapers &&
    python -m venv .venv &&
    source .venv/bin/activate &&
    python -m pip install --upgrade pip &&
    pip install -r requirements-dev.txt &&
    pip install pre-commit &&
    pre-commit install &&
    python -m unittest

In case you want to run a single unittest for a newly developed scraper

.. code:: shell

    python -m unittest -k <test_file_name>


FAQ
---
**What if the recipe site I want to extract information from is not listed above?**

You can give it a try with the ``wild_mode`` option!

If there is Schema/Recipe available it will work just fine.

.. code:: python

    url = 'https://www.feastingathome.com/tomato-risotto/'
    name = input('What is your name, risotto sampler?\n')
    html = requests.get(url, headers={"User-Agent": f"Risotto Sampler {name}"}).content
    scraper = scrape_html(html, org_url=url, wild_mode=True)

    scraper.host()
    scraper.title()
    scraper.total_time()
    scraper.image()
    scraper.ingredients()
    scraper.ingredient_groups()
    scraper.instructions()
    scraper.instructions_list()
    scraper.yields()
    scraper.to_json()
    scraper.links()
    scraper.nutrients()  # not always available
    scraper.canonical_url()  # not always available
    scraper.equipment()  # not always available
    scraper.cooking_method()  # not always available
    scraper.keywords()  # not always available
    scraper.dietary_restrictions() # not always available

Notes:

- ``scraper.links()`` returns a list of dictionaries containing all of the <a> tag attributes. The attribute names are the dictionary keys.


**How do I know if a website has a Recipe Schema?**

Run in python shell:

.. code:: pycon

    Python 4.0.4 (main, Oct 26 1985, 09:00:32) [GCC 22.3.4] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from recipe_scrapers import scrape_html
    >>> scraper = scrape_html(html=None, org_url='<url of a recipe from the site>', online=True, wild_mode=True)
    >>> # if no error is raised - there's schema available:
    >>> scraper.title()
    >>> scraper.instructions()  # etc.


Special thanks to:
------------------

All the `contributors that helped improving <https://github.com/hhursev/recipe-scrapers/graphs/contributors>`_  the package. You are awesome!

.. image:: https://contrib.rocks/image?repo=hhursev/recipe-scrapers
   :target: https://github.com/hhursev/recipe-scrapers/graphs/contributors


Extra:
------
| You want to gather recipes data?
| You have an idea you want to implement?
| Check out `our "Share a project" wall <https://github.com/hhursev/recipe-scrapers/issues/9>`_ - it may save you time and spark ideas!
