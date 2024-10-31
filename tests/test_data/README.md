Test Data
---------

As a precondition for inclusion in this library, each recipe scraper is required to include test coverage to demonstrate that it can accurately retrieve recipe information from the website it relates to.

To achieve that, the development source repository includes a minimal number of test HTML files from the public web -- often only one or two per recipe website -- to confirm the scraper's behaviour.  These test files are not included in the [published releases](https://pypi.org/project/recipe-scrapers/) of the library.

If you would prefer for any of them to be removed, we recommend choosing one of these processes:

  * You may follow GitHub's [content removal request processes](https://docs.github.com/en/site-policy/content-removal-policies/submitting-content-removal-requests).

  * You may [contact us](https://github.com/hhursev/recipe-scrapers/blob/6a6a9144c2be5ce299ce3805ea9344e34afadaca/pyproject.toml#L12-L14) (the software maintainers of this library) privately by email.

  * You may [create a public bugreport for us](https://github.com/hhursev/recipe-scrapers/issues/new).  Please **do not** include your email address in your bugreport, because GitHub issues are public, and doing so could expose your email address to spammers.

Note that removal of test HTML may reduce our ability to support the affected website(s).
