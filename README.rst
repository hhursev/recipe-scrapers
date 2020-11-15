.. image:: https://img.shields.io/pypi/v/recipe-scrapers.svg?
    :target: https://pypi.org/project/recipe-scrapers/
    :alt: Version
.. image:: https://travis-ci.com/hhursev/recipe-scrapers.svg?branch=master
    :target: https://travis-ci.com/hhursev/recipe-scrapers
    :alt: Travis
.. image:: https://coveralls.io/repos/hhursev/recipe-scraper/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/hhursev/recipe-scraper?branch=master
    :alt: Coveralls
.. image:: https://img.shields.io/github/license/hhursev/recipe-scrapers?
    :target: https://github.com/hhursev/recipe-scrapers/blob/master/LICENSE
    :alt: License
.. image:: https://img.shields.io/github/stars/hhursev/recipe-scrapers?style=social
    :target: https://github.com/hhursev/recipe-scrapers/
    :alt: Github
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Black formatted
.. image:: https://pepy.tech/badge/recipe-scrapers
    :target: https://pepy.tech/project/recipe-scrapers
    :alt: Downloads

------


A simple web scraping tool for recipe sites.

.. code:: shell

    pip install recipe-scrapers

then:

.. code:: python

    from recipe_scrapers import scrape_me

    # give the url as a string, it can be url from any site listed below
    scraper = scrape_me('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')

    # Q: What if the recipe site I want to extract information from is not listed below?
    # A: You can give it a try with the wild_mode option! If there is Schema/Recipe available it will work just fine.
    scraper = scrape_me('https://www.feastingathome.com/tomato-risotto/', wild_mode=True)

    scraper.title()
    scraper.total_time()
    scraper.yields()
    scraper.ingredients()
    scraper.instructions()
    scraper.image()
    scraper.host()
    scraper.links()


Note: ``scraper.links()`` returns a list of dictionaries containing all of the <a> tag attributes. The attribute names are the dictionary keys.

Scrapers available for:
-----------------------

- `https://www.750g.com <https://www.750g.com>`_
- `https://www.acouplecooks.com <https://acouplecooks.com/>`_
- `https://allrecipes.com/ <https://allrecipes.com/>`_
- `https://ambitiouskitchen.com/ <https://ambitiouskitchen.com>`_
- `https://archanaskitchen.com/ <https://archanaskitchen.com/>`_
- `https://averiecooks.com/ <https://www.averiecooks.com/>`_
- `https://bbc.com/ <https://bbc.com/food/recipes>`_
- `https://bbc.co.uk/ <http://bbc.co.uk/food/recipes>`_
- `https://bbcgoodfood.com/ <https://bbcgoodfood.com>`_
- `https://bettycrocker.com/ <https://bettycrocker.com>`_
- `https://bonappetit.com/ <https://bonappetit.com>`_
- `https://bowlofdelicious.com/ <https://bowlofdelicious.com/>`_
- `https://budgetbytes.com/ <https://budgetbytes.com>`_
- `https://chefkoch.de/ <https://chefkoch.de>`_
- `https://closetcooking.com/ <https://closetcooking.com>`_
- `https://cookieandkate.com/ <https://cookieandkate.com/>`_
- `https://cookpad.com/ <https://cookpad.com/>`_
- `https://cookstr.com/ <https://cookstr.com>`_
- `https://copykat.com/ <https://copykat.com>`_
- `https://countryliving.com/ <https://countryliving.com>`_
- `https://cuisineaz.com/ <https://cuisineaz.com>`_
- `https://cybercook.com.br/ <https://cybercook.com.br/>`_
- `https://delish.com/ <https://delish.com>`_
- `https://domesticate-me.com/ <https://domesticate-me.com/>`_
- `https://eatsmarter.com/ <https://eatsmarter.com/>`_
- `https://eatsmarter.de/ <https://eatsmarter.de/>`_
- `https://eatwhattonight.com/ <https://eatwhattonight.com/>`_
- `https://epicurious.com/ <https://epicurious.com>`_
- `https://recipes.farmhousedelivery.com/ <https://recipes.farmhousedelivery.com/>`_
- `https://fifteenspatulas.com/ <https://www.fifteenspatulas.com/>`_
- `https://finedininglovers.com/ <https://www.finedininglovers.com>`_
- `https://fitmencook.com/ <https://www.fitmencook.com>`_
- `https://food.com/ <https://www.food.com>`_
- `https://foodnetwork.com/ <https://www.foodnetwork.com>`_
- `https://foodrepublic.com/ <https://foodrepublic.com>`_
- `https://geniuskitchen.com/ <https://geniuskitchen.com>`_
- `https://giallozafferano.it/ <https://giallozafferano.it>`_
- `https://gimmesomeoven.com/ <https://www.gimmesomeoven.com/>`_
- `https://gonnawantseconds.com/ <https://gonnawantseconds.com>`_
- `https://gousto.co.uk/ <https://gousto.co.uk>`_
- `https://greatbritishchefs.com/ <https://greatbritishchefs.com>`_
- `https://halfbakedharvest.com/ <https://www.halfbakedharvest.com/>`_
- `https://www.hassanchef.com/ <https://www.hassanchef.com/>`_
- `https://www.heb.com/ <https://www.heb.com/recipe/landing>`_
- `https://heinzbrasil.com.br/ <https://heinzbrasil.com.br>`_
- `https://hellofresh.com/ <https://hellofresh.com>`_
- `https://hellofresh.co.uk/ <https://hellofresh.co.uk>`_
- `https://www.hellofresh.de/ <https://www.hellofresh.de/>`_
- `https://hostthetoast.com/ <https://hostthetoast.com/>`_
- `https://101cookbooks.com/ <https://101cookbooks.com/>`_
- `https://receitas.ig.com.br/ <https://receitas.ig.com.br>`_
- `https://inspiralized.com/ <https://inspiralized.com>`_
- `https://jamieoliver.com/ <https://jamieoliver.com>`_
- `https://justbento.com/ <https://justbento.com>`_
- `https://kennymcgovern.com/ <https://kennymcgovern.com>`_
- `https://www.kingarthurbaking.com <https://www.kingarthurbaking.com>`_
- `https://kochbar.de/ <https://kochbar.de>`_
- `https://kuchnia-domowa.pl/ <https://www.kuchnia-domowa.pl/>`_
- `http://livelytable.com/ <http://livelytable.com/>`_
- `https://lovingitvegan.com/ <https://lovingitvegan.com/>`_
- `https://lecremedelacrumb.com/ <https://lecremedelacrumb.com/>`_
- `https://marmiton.org/ <https://marmiton.org/>`_
- `https://matprat.no/ <https://matprat.no/>`_
- `http://mindmegette.hu/ <http://mindmegette.hu/>`_
- `https://minimalistbaker.com/ <https://minimalistbaker.com/>`_
- `https://misya.info/ <https://misya.info>`_
- `https://momswithcrockpots.com/ <https://momswithcrockpots.com>`_
- `http://motherthyme.com/ <http://motherthyme.com/>`_
- `https://mybakingaddiction.com/ <https://mybakingaddiction.com>`_
- `https://myrecipes.com/ <https://myrecipes.com>`_
- `https://healthyeating.nhlbi.nih.gov/ <https://healthyeating.nhlbi.nih.gov>`_
- `https://nourishedbynutrition.com/ <https://nourishedbynutrition.com/>`_
- `https://nutritionbynathalie.com/blog <https://nutritionbynathalie.com/blog>`_
- `https://cooking.nytimes.com/ <https://cooking.nytimes.com>`_
- `https://ohsheglows.com/ <https://ohsheglows.com>`_
- `https://www.panelinha.com.br/ <https://www.panelinha.com.br>`_
- `https://paninihappy.com/ <https://paninihappy.com>`_
- `https://przepisy.pl/ <https://przepisy.pl>`_
- `https://purelypope.com/ <https://purelypope.com>`_
- `https://realsimple.com/ <https://www.realsimple.com>`_
- `https://seriouseats.com/ <https://seriouseats.com>`_
- `https://simplyquinoa.com/ <https://simplyquinoa.com>`_
- `https://simplyrecipes.com/ <https://simplyrecipes.co>`_
- `https://simplywhisked.com/ <https://simplywhisked.com>`_
- `https://skinnytaste.com/ <https://www.skinnytaste.com>`_
- `https://southernliving.com/ <https://southernliving.com/>`_
- `https://spendwithpennies.com/ <https://spendwithpennies.com/>`_
- `https://steamykitchen.com/ <https://steamykitchen.com>`_
- `https://sunbasket.com/ <https://sunbasket.com>`_
- `https://tastesoflizzyt.com <https://tastesoflizzyt.com>`_
- `https://tasteofhome.com <https://tasteofhome.com>`_
- `https://tasty.co <https://tasty.co>`_
- `https://tastykitchen.com/ <https://tastykitchen.com>`_
- `https://thehappyfoodie.co.uk/ <https://thehappyfoodie.co.uk>`_
- `https://thekitchn.com/ <https://thekitchn.com/>`_
- `https://thenutritiouskitchen.co/ <https://thenutritiouskitchen.co/>`_
- `https://thepioneerwoman.com/ <https://thepioneerwoman.com>`_
- `https://thespruceeats.com/ <https://thespruceeats.com/>`_
- `https://thevintagemixer.com/ <https://thevintagemixer.com>`_
- `https://thewoksoflife.com/ <https://thewoksoflife.com/>`_
- `https://tine.no/ <https://tine.no>`_
- `https://tudogostoso.com.br/ <https://www.tudogostoso.com.br/>`_
- `https://twopeasandtheirpod.com/ <http://twopeasandtheirpod.com>`_
- `https://vegolosi.it/ <https://vegolosi.it>`_
- `https://watchwhatueat.com/ <https://watchwhatueat.com/>`_
- `https://whatsgabycooking.com/ <https://whatsgabycooking.com>`_
- `https://en.wikibooks.org/ <https://en.wikibooks.org>`_
- `https://yummly.com/ <https://yummly.com>`_


Contribute
----------

Part of the reason I want this open sourced is because if a site makes a design change, the scraper for it should be modified.

If you spot a design change (or something else) that makes the scraper unable to work for a given site - please fire an issue asap.

If you are programmer PRs with fixes are warmly welcomed and acknowledged with a virtual beer.


If you want a scraper for a new site added
------------------------------------------

- Open an `Issue <https://github.com/hhursev/recipe-scraper/issues/new>`_ providing us the site name, as well as a recipe link from it.
- You are a developer and want to code the scraper on your own:

  - If Schema is available on the site - `you can do this <https://github.com/hhursev/recipe-scrapers/pull/176>`_

    - `How do I know if a schema is available on my site? <#faq>`_

  - Otherwise, scrape the HTML - `like this <https://github.com/hhursev/recipe-scrapers/commit/ffee963d04>`_

For Devs / Contribute
---------------------

Assuming you have ``python3`` installed, navigate to the directory where you want this project to live in and drop these lines

.. code:: shell

    git clone git@github.com:hhursev/recipe-scrapers.git &&
    cd recipe-scrapers &&
    python3 -m venv .venv &&
    source .venv/bin/activate &&
    pip install -r requirements-dev.txt &&
    pre-commit install &&
    python -m coverage run -m unittest &&
    python -m coverage report

In case you want to run a single unittest for a newly developed scraper

.. code:: shell

    python -m coverage run -m unittest tests.test_myscraper

FAQ
---
- **How do I know if a website has a Recipe Schema?** Run in python shell:

.. code:: python

    from recipe_scrapers import scrape_me
    scraper = scrape_me('<url of a recipe from the site>', wild_mode=True)
    # if no error is raised - there's schema available:
    scraper.title()
    scraper.instructions()  # etc.


Special thanks to:
------------------

All the `contributors that helped improving <https://github.com/hhursev/recipe-scrapers/graphs/contributors>`_  the package. You are awesome!
