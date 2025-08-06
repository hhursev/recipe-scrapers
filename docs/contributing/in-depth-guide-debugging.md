# In Depth Guide: Debugging

> **Draft**
> This in depth guide is intended to give more guidance on debugging scrapers during
> development and handling exceptions.
>
>To be populated at a later date.

## Updating test data

Over time websites change their layout and underlaying html, it is not uncommon for this to interfere
with the scrapers.  It is then useful to download new test data, which can be done with the script
update_test.py found in the scripts directory.

The updated files should be inspected so that any changes are correct before they are commited.

An example:
```sh
$ python scripts/update_test.py tests/test_data/ica.se/ica.json

$ git status tests/test_data/ica.se/
On branch update-test
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   tests/test_data/ica.se/ica.json
	modified:   tests/test_data/ica.se/ica.testhtml

no changes added to commit (use "git add" and/or "git commit -a")

$ git diff tests/test_data/ica.se/ica.json
diff --git a/tests/test_data/ica.se/ica.json b/tests/test_data/ica.se/ica.json
index 0fdc152f..cd34bac8 100644
--- a/tests/test_data/ica.se/ica.json
+++ b/tests/test_data/ica.se/ica.json
@@ -17,8 +17,8 @@
     "1 tsk torkad basilika",
     "2 1/2 dl torrt vitt vin",
     "1 1/2 fiskbuljongtärning",
-    "2 - 2 1/2 dl Oatly iMat eller vispgrädde",
-    "1 dl Oatly iMat Fraiche eller crème fraiche",
+    "2 dl vispgrädde",
+    "1 dl crème fraiche",
     "2 dl vatten",
     "1 pkt saffran (à 0,5 g)",
     "1 tsk salt",
... # Truncated
```

Here we see that some ingredients have been updated (changed from branded versions to unbranded for those
not familiar with Swedish) but the parsing is still working.

In other cases the process might fail in various ways:

* The website is blocking scraping or there is some other problem with fetching the html file. In this case you
  may have to obtain the data in som other way (but keep in mind recipe-scrapers
  [policy to not circumvent any technical access controls](../copyright-and-usage.md#librarys-role))
* The scraper do no longer parse the data correctly. Then it is of to the debuging bench to isolate the problem
  and fix the scraper to work again.
* Some historic tests do not have a correct url for the recipe. In that case you must try to find it and update
  the json file by hand before you rerun the script.


!!! warning "Use with caution"
    This is a tool ment for updating data when debuging, do _not_ use it to mass test scrapers
    and carpet bomb the project with bug reports. It is better to focus on one scraper and try
    learn how to fix the problem.
