# In Depth Guide: HTML Scraping

!!! warning "Under Construction"
    This section is being updated. Some information may be outdated or inaccurate.

The preferred method of scraping recipe information from a web page is to use the schema.org
Recipe data. This is a machine readable, structured format intended to provide a standardised
method of extracting information. However, whilst most recipe websites use the schema.org Recipe
format, not all do, and for those websites that do, it does not always include all the information
we are looking for. In these cases, we can use HTML scraping to extract the information from
the HTML markup.

## `soup`

Each scraper has a `BeautifulSoup` object that can be accessed using the `self.soup` attribute.
The `BeautifulSoup` object is a representation of the web page HTML that has been parsed into a
format that we can query and extract information from.

The [Beautiful Soup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) is the best resource for learning how to use `BeautifulSoup`
objects to interact with HTML documents.

This guide covers a number of common patterns that are used in this library.

## `_schema_cls` and `_opengraph_cls`

It should rarely be necessary to override the default behaviour of schema.org and OpenGraph
metadata retrieval; recipe websites should generally adhere to their respective standard formats
when including metadata on their webpages.  However, bugs/mistakes do happen - if you need to
override the implementations provided by the `SchemaOrg` and `OpenGraph` classes, you can subclass
from those and add a `_schema_cls` or `_opengraph_cls` attribute to your scraper class to instruct
the library to use them instead.

## Finding a single element

The `self.soup.find()` function returns the first element matching the arguments. This is useful if
you are trying to extract some information that should only occur once, for example the prep time
or total time.

```python
# To find a particular element
self.soup.find("h1") # Returns the first h1 element

# To find an element with particular class (note the underscore at the end of class_)
self.soup.find(class_"total-time") # Returns the first element with total-time class.

# To find an element with a particular ID
self.soup.find(id="total-time")

# You can include multiple arguments to be more specific
# To find the first h1 element with "title" class
self.soup.find("h1", class_="title")
```

`self.soup` returns a `bs4.element.Tag` object. Usually we just want the text from the selected
element and the best way to do that is to use `.get_text()`.

```python
title_tag = self.soup.select("h1") # bs4.element.Tag object
title_text = title_tag.get_text() # str
```

`.get_text()` will get the text from all child elements, as it would appear in your browser, so
there is no need to iterate through all the children, call `.get_text()` on each one, then join
the results afterwards.

As an example, consider one of the ingredients in [this recipe](https://rainbowplantlife.com/instant-pot-jackfruit-curry/#wprm-recipe-container-5618). The markup looks like this:

```html
<li class="wprm-recipe-ingredient" style="list-style-type: none;" data-uid="0">
  <span class="wprm-checkbox-container">
    <input type="checkbox" id="wprm-checkbox-1" class="wprm-checkbox" aria-label="&nbsp;1 tablespoon coconut oil (or oil of choice)">
    <label for="wprm-checkbox-1" class="wprm-checkbox-label">
      <span class="sr-only screen-reader-text wprm-screen-reader-text">▢ </span>
    </label>
  </span>
  <span class="wprm-recipe-ingredient-amount">1</span>
  <span class="wprm-recipe-ingredient-unit">tablespoon</span>
  <span class="wprm-recipe-ingredient-name">coconut oil</span>
  <span class="wprm-recipe-ingredient-notes wprm-recipe-ingredient-notes-normal">(or oil of choice)</span>
</li>
```

We can select this element using its tag and class (we're pretending this recipe only has this one
ingredient), and extract the text like so:

```python
ingredient_tag = self.soup.find("li", class_="wprm-recipe-ingredient")
ingredient_text = ingredient_tag.get_text()
# '1 tablespoon coconut oil (or oil of choice)'
```

The Beautiful Soup documentation for `find` is [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find).

### Normalizing strings

A convenience function called `normalize_string()` is provided in the `_utils` package. This
function will convert any characters escaped for HTML to their actual character (e.g. `&amp;`
to `&`) and remove unnecessary white space. It is best practice to always use this when extracting
text from the HTML.

```python
from ._utils import normalize_string

# ...
ingredient_tag = self.soup.find("li", class_="wprm-recipe-ingredient")
ingredient_text = normalize_string(ingredient_tag.get_text())
```

### Getting yields

A convenience function called `get_yields()` is provided in the `_utils` package. This function
accepts a `str` or `bs4.element.Tag` and will return the yield, handling many of the common
formats yields can appear in and normalizing them to a standard format.

```python
from ._utils import get_yields

# ...
yield_tag = self.soup.find(class_="wprm-recipe-servings")
yield_text = get_yields(yield_tag)
# or
yield_text = get_yields(yield_tag.get_text())
# both return '4 servings'
```

### Getting times

A convenience function called `get_minutes()` is provided in the `_utils` package. This function
accepts a `str` or `bs4.element.Tag` and will return the number of minutes as an `int`. This
function handles a number of common formats that times can be expressed in.

```python
from ._utils import get_minutes

# ...
prep_time_tag = self.soup.find(class_="wprm-recipe-prep_time-minutes")
prep_time_value = get_minutes(prep_time_tag)
# or
prep_time_value = get_minutes(prep_time_tag.get_text())
# both return 25
```

## Finding multiple elements

Some information in a recipe, like the ingredients or instructions, come in the form of lists where
we need to find multiple elements with the same attributes. We can use `self.soup.find_all()` for
this. `find_all` uses the same arguments as `find`, it just returns a list of `bs4.element.Tag`
objects with all the matching elements.

Using the same site as above, we can find all the ingredients like so

```python
ingredient_tags = self.soup.find_all("li", class_="wprm-recipe-ingredient")
ingredients_text = [normalize_string(tag.get_text()) for tag in ingredient_tags]
"""
[
 '2 (20-ounce // 565g) cans of jackfruit (in water or brine)*',
 '1 tablespoon coconut oil (or oil of choice)',
 '1 1/2 teaspoons cumin seeds',
 '1 1/2 teaspoons black mustard seeds (can substitute brown mustard seeds)',
 '1 large yellow onion, diced',
 ...
]
"""
```

The Beautiful Soup documentation for `find_all` is [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all).

## Using CSS selectors

If you are already familiar with CSS selectors, then you can use `select()` to achieve the same
result as `find_all()`, or `select_one()` to achieve the same result as `find`.

```python
# Match all li elements with wprm-recipe-ingredient class
ingredient_tag = self.soup.select("li.wprm-recipe-ingredient")
```

The Beautiful Soup documentation for `select` is [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors-through-the-css-property). MDN has a guide on
CSS selectors [here](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors).

## Finding elements using a partial attribute

Sometimes you might want to find elements using a part of an attribute. This is particularly
helpful for websites that automatically generate CSS in a way that appends a random string to
the end of class names.

An example of this is [cooking.nytimes.com](https://cooking.nytimes.com/recipes/1024605-cumin-and-cashew-yogurt-rice). If we wanted to select the yield element from
this page, we could use the class `ingredients_recipeYield__DN65p`. However when the website is
updated in the future, the `DN65p` at the end of the class name is likely to change, so we only
want to use part of the class name.

There are two ways we can do this:

### Using `find`

Instead of using a string in the arguments we pass to `find`, we can use a regular expression
instead.

```python
yield_tag = self.soup.find(class_=re.compile("ingredients_recipeYield"))
yield_text = yield_tag.get_text()
# Yield:4 servings
```

### Using `select`

CSS also supports partial attribute matching. MDN has a useful guide [here](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors).

```python
# Select elements where class contains 'ingredients_recipeYield'
yield_tag = self.soup.select("[class*='ingredients_recipeYield']")

# Select tags where class starts with 'ingredients_recipeYield'
yield_tag = self.soup.select("[class^='ingredients_recipeYield']")
```
