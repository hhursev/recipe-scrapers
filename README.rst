.. image:: https://img.shields.io/pypi/v/recipe-scrapers.svg?
    :target: https://pypi.org/project/recipe-scrapers/
    :alt: Version
.. image:: https://travis-ci.org/hhursev/recipe-scrapers.svg?branch=master
    :target: https://travis-ci.org/hhursev/recipe-scrapers
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


------


A simple web scraping tool for recipe sites.

.. code::

    pip install recipe-scrapers

then:

.. code:: python

    from recipe_scrapers import scrape_me

    # give the url as a string, it can be url from any site listed below
    scraper = scrape_me('http://allrecipes.com/Recipe/Apple-Cake-Iv/Detail.aspx')

    scraper.title()
    scraper.total_time()
    scraper.yields()
    scraper.ingredients()
    scraper.instructions()
    scraper.image()
    scraper.links()

Note: ``scraper.links()`` returns a dictionary object containing all of the <a> tag attributes. The attribute names are the dictionary keys.

Scrapers available for:
-----------------------

- `http://101cookbooks.com/ <http://101cookbooks.com/>`_
- `http://allrecipes.com/ <http://allrecipes.com/>`_
- `http://bbc.com/ <http://bbc.com/food/recipes>`_
- `http://bbc.co.uk/ <http://bbc.co.uk/food/recipes>`_
- `http://bbcgoodfood.com/ <http://bbcgoodfood.com>`_
- `http://bettycrocker.com/ <http://bettycrocker.com>`_
- `http://bonappetit.com/ <http://bonappetit.com>`_
- `https://www.budgetbytes.com/ <https://www.budgetbytes.com>`_
- `http://closetcooking.com/ <http://closetcooking.com>`_
- `http://cookstr.com/ <http://cookstr.com>`_
- `http://copykat.com/ <http://copykat.com>`_
- `https://cybercook.com.br/ <https://cybercook.com.br/>`_
- `https://en.wikibooks.org/ <https://en.wikibooks.org>`_
- `http://delish.com/ <http://delish.com>`_
- `http://epicurious.com/ <http://epicurious.com>`_
- `http://finedininglovers.com/ <https://www.finedininglovers.com>`_
- `https://food.com/ <https://www.food.com>`_
- `http://foodnetwork.com/ <http://www.foodnetwork.com>`_
- `http://foodrepublic.com/ <http://foodrepublic.com>`_
- `https://geniuskitchen.com/ <https://geniuskitchen.com>`_
- `https://greatbritishchefs.com/ <https://greatbritishchefs.com>`_
- `http://giallozafferano.it/ <http://giallozafferano.it>`_
- `http://gonnawantseconds.com/ <http://gonnawantseconds.com>`_
- `https://healthyeating.nhlbi.nih.gov/ <https://healthyeating.nhlbi.nih.gov>`_
- `https://heinzbrasil.com.br/ <https://heinzbrasil.com.br>`_
- `https://www.hellofresh.com/ <https://www.hellofresh.com>`_
- `https://www.hellofresh.co.uk/ <https://www.hellofresh.co.uk>`_
- `https://receitas.ig.com.br/ <https://receitas.ig.com.br>`_
- `https://inspiralized.com/ <https://inspiralized.com>`_
- `http://jamieoliver.com/ <http://www.jamieoliver.com>`_
- `https://justbento.com/ <https://justbento.com>`_
- `https://www.thekitchn.com/ <https://www.thekitchn.com/>`_
- `https://www.matprat.no/ <https://www.matprat.no/>`_
- `http://www.mindmegette.hu/ <http://www.mindmegette.hu/>`_
- `https://www.misya.info/ <https://www.misya.info>`_
- `http://mybakingaddiction.com/ <http://mybakingaddiction.com>`_
- `https://panelinha.com.br/ <https://panelinha.com.br>`_
- `http://paninihappy.com/ <http://paninihappy.com>`_
- `http://przepisy.pl/ <http://przepisy.pl>`_
- `http://realsimple.com/ <http://www.realsimple.com>`_
- `https://www.seriouseats.com/ <https://www.seriouseats.com>`_
- `http://simplyrecipes.com/ <http://www.simplyrecipes.co>`_
- `https://www.southernliving.com/ <https://www.southernliving.com/>`_
- `http://steamykitchen.com/ <http://steamykitchen.com>`_
- `https://www.tastesoflizzyt.com <https://www.tastesoflizzyt.com>`_
- `http://tastykitchen.com/ <http://tastykitchen.com>`_
- `http://thepioneerwoman.com/ <http://thepioneerwoman.com>`_
- `https://www.thespruceeats.com/ <https://www.thespruceeats.com/>`_
- `http://thehappyfoodie.co.uk/ <http://thehappyfoodie.co.uk>`_
- `http://thevintagemixer.com/ <http://www.thevintagemixer.com>`_
- `http://tine.no/ <http://tine.no>`_
- `http://twopeasandtheirpod.com/ <http://twopeasandtheirpod.com>`_
- `http://whatsgabycooking.com/ <http://whatsgabycooking.com>`_
- `http://yummly.com/ <http://yummly.com>`_


Contribute
----------

Part of the reason I want this open sourced is because if a site makes a design change, the scraper for it should be modified.

If you spot a design change (or something else) that makes the scraper unable to work for a given site - please fire an issue asap.

If you are programmer PRs with fixes are warmly welcomed and acknowledged with a virtual beer.


If you want a scraper for a new site added
------------------------------------------

- Open an `Issue <https://github.com/hhursev/recipe-scraper/issues/new>`_ providing us the site name, as well as a recipe link from it.
- If you are a developer and want to code the scraper on your own, `this is a wonderful example <https://github.com/hhursev/recipe-scraper/pull/29/files>`_ of how to do it.


For Devs / Contribute
---------------------

Assuming you have `python3` installed, navigate to the directory where you want this project to live in and drop these lines

.. code::

    git clone git@github.com:hhursev/recipe-scrapers.git &&
    cd recipe-scrapers &&
    python3 -m venv .venv &&
    source .venv/bin/activate &&
    pip install -r requirements.txt &&
    coverage run tests.py &&
    coverage report


Spacial thanks to:
------------------

All the `contributors that helped improving <https://github.com/hhursev/recipe-scrapers/graphs/contributors>`_  the package. You are awesome!
