# In Depth Guide: Ingredient Groups

!!! warning "Under Construction"
    This section is being updated. Some information may be outdated or inaccurate.

Sometimes a website will format lists of ingredients using groups, where each group contains the
ingredients needed for a particular aspect of the recipe. Recipe Schema has no way to represent
these groupings, so all of the ingredients are presented as a single list and information about
the groupings is lost.

Some examples of recipes that have ingredient groups are:

* <https://cooking.nytimes.com/recipes/1024570-green-salad-with-warm-goat-cheese-salade-de-chevre-chaud>
* <https://lifestyleofafoodie.com/air-fryer-frozen-french-fries>
* <https://www.bbcgoodfood.com/recipes/monster-cupcakes>

Not all websites use ingredient groups and those that do use ingredient groups will not use them
for all recipes.

This library allows a scraper to return the ingredients in the groups defined in the recipe if the
functionality is added to that scraper.

## `ingredient_groups()`

The `ingredient_groups()` function returns a list of `IngredientGroup` objects. Each
`IngredientGroup` is a dataclass that represents a group of ingredients:

```python
@dataclass
class IngredientGroup:
    ingredients: List[str]
    purpose: Optional[
        str
    ] = None  # this group of ingredients is {purpose} (e.g. "For the dressing")
```

The *purpose* is the ingredient group heading, such as *"For the dressing"*, *"For the sauce"* etc.
The *ingredients* is the list of ingredients that comprise that group.

This dataclass is defined in `_grouping_utils.py` and should be imported from there.

```python
from ._grouping_utils import IngredientGroup
```

The `ingredient_groups()` function has a default implementation in the `AbstractScraper` class that
returns a single `IngredientGroup` object with `purpose` set to `None` and `ingredients` set to the
output from the scraper's `ingredients()` function.

Adding ingredient group support to a scraper involves overriding the `ingredient_groups` function
for it. There are three important points to consider:

1. The schema.org Recipe format does not support groupings - so scraping from the HTML is required
in the implementation.
2. The ingredients found in `ingredients()` and `ingredient_groups()` should be the same because
we're presenting the same set of ingredients, just in a different way. There can sometimes be minor
differences in the ingredients in the schema and the ingredients in the HTML which needs to be
handled.
3. Not all recipes on a website will use ingredient groups, so the implementation must degrade
gracefully in cases where groupings aren't available. For recipes that don't have ingredient groups,
the output should be the same as default implementation
(i.e. a single `IngredientGroup` with `purpose=None` and `ingredients=ingredients()`).

In many cases the structure of how ingredients and group heading appear in the HTML is very similar.
Some helper functions have been developed to make the implementation easier.

## _grouping_utils.py

The `_grouping_utils.py` file contains a helper function (`group_ingredients(...)`)
that will handle the extraction of ingredients groups and their headings from the HTML, make sure
the ingredients in the groups match those return from `.ingredients()`, and then return the groups.

The `group_ingredients()` function takes four arguments:

```python
def group_ingredients(
    ingredients_list: List[str],
    soup: BeautifulSoup,
    group_heading: str,
    group_element: str,
) -> List[IngredientGroup]:
```

* `ingredients_list` is the output from the `.ingredients()` function of the scraper class. This is
* used to make the ingredients found in the HTML match those returned by `.ingredients()`.
* `soup` is the `BeautifulSoup` object for the scraper. The ingredient groups are extracted from
* this.
* `group_heading` is the CSS selector for the group headings. This selector must only match the
* group headings in the recipe HTML.
* `group_element` is the CSS selector for the ingredients. This selector must only match the
* ingredients in the recipe HTML.

### Example

Many recipe blogs use WordPress and the WordPress Recipe Manager plugin. This means they often use
the same HTML elements and CSS classes to represent the same things.
One such example is <https://rainbowplantlife.com>.

If we look at the recipe: <https://rainbowplantlife.com/vegan-pasta-salad/>

The group headings in this recipe are all `h4` headings inside an element with the
class `wprm-recipe-ingredient-group`. Therefore we can select all ingredient group headings
with the selector: `.wprm-recipe-ingredient-group h4`

The ingredients are all elements with the class `wprm-recipe-ingredient`. Therefore we can select
all ingredients with the selector: `.wprm-recipe-ingredient`

The implementation in the scraper looks like

```python
from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class RainbowPlantLife(AbstractScraper):
    ...

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )
```

That is all that is required to add support for ingredient groups to this scraper.

Some other examples of scrapers that support ingredient groups are:

* [BudgetBytes](https://github.com/hhursev/recipe-scrapers/blob/main/recipe_scrapers/budgetbytes.py)
* [NYTimes](https://github.com/hhursev/recipe-scrapers/blob/main/recipe_scrapers/nytimes.py)
* [PickUpLimes](https://github.com/hhursev/recipe-scrapers/blob/main/recipe_scrapers/pickuplimes.py)
* [RealFoodTesco](https://github.com/hhursev/recipe-scrapers/blob/main/recipe_scrapers/realfoodtesco.py)

**What if `group_ingredients()` doesn't work?**

The `group_ingredients` function relies on being able to identify all the group headings with a
single CSS selector and all the ingredients with a single CSS selector. However, this is not always
possible - it depends on how the website lays out its HTML.

In these cases, supporting ingredient groups may still be possible. The `group_ingredients()` helper
method is only that: an optional helper -- you can always implement custom grouping logic yourself
by overriding `ingredient_groups()` directly in your scraper if you can't find suitable CSS
selectors for the ingredients and groups.

An example of a scraper that supports ingredient groups without using the `group_ingredients()`
helper is [NIHHealthyEating](https://github.com/hhursev/recipe-scrapers/blob/main/recipe_scrapers/nihhealthyeating.py).

## Tests

Recipe websites often provide ingredient groupings on some, but not all, of their recipe webpages.
When this is the case, we should add at least two test cases for our scraper: one to cover a
recipe **with** ingredient groupings, and one to cover a recipe **without** them.

Test cases **without** ingredient groupings in the HTML are simpler, because every scraper test
case *automatically* inherits a test that checks to make sure the output of `.ingredients()` is
consistent with the output from `.ingredient_groups()`, and that provides all the test coverage
we need.

The test case **with** ingredient grouping should include an `ingredient_groups` item in the JSON
data with each section of the ingredients separated out in the applicable test case like this
example:

```json
    "ingredient_groups": [
      {
        "ingredients": [
            "1¾ cups Graham cracker crumbs",
            "½ cup melted unsalted butter",
            "2 tablespoons granulated sugar"
        ],
        "purpose": "Crust:"
      },
      {
        "ingredients": [
          "24 ounces cream cheese",
          "1½ cups powdered sugar (divided)",
          "⅓ cup sour cream",
          "2 teaspoons pure vanilla extract",
          "Juice of 1 lemon",
          "1¼ cups heavy whipping cream",
          "1 cup fresh raspberries (puréed)",
          "1 cup fresh blueberries (puréed)",
          "Whipped cream and fresh berries for garnish"
        ],
        "purpose": "Filling:"
      }
    ],
```
