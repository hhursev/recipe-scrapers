=================
recipe-scrapers
=================

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
.. image:: https://github.com/hhursev/recipe-scrapers/actions/workflows/unittests.yaml/badge.svg?branch=main
    :target: unittests
    :alt: GitHub Actions Unittests
.. image:: https://coveralls.io/repos/hhursev/recipe-scraper/badge.svg?branch=main&service=github
    :target: https://coveralls.io/github/hhursev/recipe-scraper?branch=main
    :alt: Coveralls
.. image:: https://img.shields.io/github/license/hhursev/recipe-scrapers?
    :target: https://github.com/hhursev/recipe-scrapers/blob/main/LICENSE
    :alt: License

-------

A reliable python tool for scraping recipe data from popular cooking websites. Extract structured
recipe information including ingredients, instructions, cooking times, and nutritional data
with ease. Supports 400+ major recipe websites out of the box.


Quick Links
-----------
- `Documentation <https://docs.recipe-scrapers.com>`_
- `Supported Sites <https://docs.recipe-scrapers.com/getting-started/supported-sites/>`_
- `Contributing Guide <https://docs.recipe-scrapers.com/contributing/home/>`_
- `Issue Tracker <https://github.com/hhursev/recipe-scrapers/issues>`_
- `Share Project Ideas <https://github.com/hhursev/recipe-scrapers/issues/9>`_


Installing
----------
.. code:: shell

    pip install recipe-scrapers


Basic Usage
-----------
.. code:: python

    from urllib.request import urlopen
    from recipe_scrapers import scrape_html

    # Example recipe URL
    url = "https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/"
    # retrieve the recipe webpage HTML
    html = urlopen(url).read().decode("utf-8")

    # pass the html alongside the url to our scrape_html function
    scraper = scrape_html(html, org_url=url)

    # Extract recipe information
    print(scraper.title())          # "Spinach and Feta Turkey Burgers"
    print(scraper.total_time())     # 35
    print(scraper.yields())         # "4 servings"
    print(scraper.ingredients())    # ['1 pound ground turkey', '1 cup fresh spinach...']
    print(scraper.instructions())   # 'Step 1: In a large bowl...'

    # For a complete list of available methods:
    help(scraper)


HTTP Clients
------------
Some Python HTTP clients you can use to retrieve HTML include:

- `requests`_: Popular and feature-rich
- `httpx`_: Modern, supports async/await
- `urllib.request`_: Included in Python's standard library

Please refer to their documentation to find out what options (timeout configuration, proxy
support, etc) are available.

.. _requests: https://pypi.org/project/requests/
.. _httpx: https://pypi.org/project/httpx/
.. _urllib.request: https://docs.python.org/3/library/urllib.request.html


Supported Sites
---------------
We support a wide range of recipe websites out of the box. Check our
`supported sites list <https://docs.recipe-scrapers.com/getting-started/supported-sites/>`_
for the full list.

You can also get the full list programmatically with:

.. code:: python

    from recipe_scrapers import SCRAPERS

    SCRAPERS.keys()


Documentation
-------------
For detailed usage instructions, examples, and API reference, visit our
`documentation <https://docs.recipe-scrapers.com>`_.


Contributing
------------
We welcome contributions! Please read our
`contribution guide <https://docs.recipe-scrapers.com/contributing/home/>`_ to get started.


Special Thanks
--------------
To all the `contributors <https://github.com/hhursev/recipe-scrapers/graphs/contributors>`_ who
help make this project better!

.. image:: https://contrib.rocks/image?repo=hhursev/recipe-scrapers
   :target: https://github.com/hhursev/recipe-scrapers/graphs/contributors


Share Your Project
------------------
Have an idea for using recipe-scrapers? Check out
our `project ideas wall <https://github.com/hhursev/recipe-scrapers/issues/9>`_ for inspiration
or to share your own project!
