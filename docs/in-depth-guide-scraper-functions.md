# In Depth Guide: Scraper Functions

Each website scraper has a number of functions that return information about the recipe that has been scraped. Due to the variability in how recipes are written, not all of them are always applicable. These functions fall into three categories:

1. Mandatory functions

   These functions can be expected to be available for all Scraper classes and combined provide the majority of the information for a recipe.

2. Inherited functions

   These functions are always available for all Scraper classes. They are implemented in the `AbstractScraper` base class and rarely require overriding in the Scraper class.

3. Optional functions

   These functions provide extra information about a recipe, from the particular websites that support them.

All of the examples below come from https://www.bbcgoodfood.com/recipes/monster-cupcakes.

```py
>>> from recipe_scrapers import scrape_html
>>> scraper = scrape_html(html=None, org_url="https://www.bbcgoodfood.com/recipes/monster-cupcakes", online=True)
```

## Mandatory functions

### `author() -> str`

Returns the author of the recipe. This is typically a person's name but can sometimes be an organization or the name of the website the recipe came from. If the recipe does not explicitly define an author, this should return the name of the website.

```py
>>> scraper.author()
'Good Food team'
```

### `host() -> str`

Returns the host of the website the Scraper class is for. This is a constant `str` set in each Scraper class.

```python
>>> scraper.host()
'bbcgoodfood.com'
```
### `description() -> str`

Returns a description of the recipe. This is normally a sentence or short paragraph describing the recipe. Often the website defines the description, but sometimes it has to be inferred from the page content.

```py
>>> scraper.description()
'Let your little monsters do their worst, decorating these spooky Halloween treats'
```

### `image() -> str`

Returns the URL to the main image associated with the recipe, usually a photograph of the completed recipe.

```py
>>> scraper.image()
'https://images.immediate.co.uk/production/volatile/sites/30/2020/08/recipe-image-legacy-id-405483_12-cee017a.jpg?resize=768,574'
```
### `ingredients() -> List[str]`

Returns the ingredients needed to make the recipe as a `list` of `str`. Each element of the list is usually a single sentence stating an ingredient, the required amount and any additional comments. The elements of the list should mirror the ingredients written on the website and should not include non-ingredient sentences such as sub-headings.

```py
>>> scraper.ingredients()
[
	'250g self-raising flour',
	'25g cocoa powder',
 	'175g light muscovado sugar',
 	'85g unsalted butter , melted',
 	'5 tbsp vegetable or sunflower oil',
 	'150g pot fat-free natural yogurt',
 	'1 tsp vanilla extract',
 	'3 large eggs',
 	'85g unsalted butter , softened',
 	'1 tbsp milk',
 	'½ tsp vanilla extract',
 	'200g icing sugar , sifted',
 	'food colourings (optional)',
 	'sweets and sprinkles, to decorate'
]
```

### `instructions() -> str`

Returns a single `str` containing all instruction steps. Where a recipe has multiple instructions, each step is separated in the returned `str` by a newline character (`\n`).

```py
>>> scraper.instructions()
'Heat oven to 190C/170C fan/gas 5 and line a 12-hole muffin tin with deep cake cases. Put all the cake ingredients into a large bowl and beat together with electric hand beaters until smooth. Spoon the mix into the cases, then bake for 20 mins until risen and a skewer inserted into the middle comes out dry. Cool completely on a rack. Can be made up to 3 days ahead and kept in an airtight container, or frozen for up to 1 month.\nFor the frosting, work the butter, milk and vanilla into the icing sugar until creamy and pale. Colour with food colouring, if using, then create your own gruesome monster faces using sweets and sprinkles.'
```

> [!IMPORTANT]
>
> Occasionally, a recipe will have steps that have new lines within them. At the moment, this library cannot distinguish between a newline within a step and a newline between steps.

### `title() -> str`

Returns the title of the recipes, usually a short sentence or phrase.

```py
>>> scraper.title()
'Monster cupcakes'
```

### `total_time() -> int`

Returns the total time required to complete the recipe, in minutes.

```py
>>> scraper.total_time()
50
```

### `yields() -> str`

Returns the number of items or servings the recipe will make. This `str` includes the quantity and unit of the yield, for example: 4 servings, 6 items, 12 cookies.

```py
>>> scraper.yields()
'12 items'
```

## Inherited functions

### `canonical_url() -> str`

Returns the canonical URL for the scraped recipe. The canonical URL is the direct URL (defined by the website) at which the recipe can be found. This URL will generally not contain any query parameters or fragments, except those required to load the recipe.

```py
>>> scraper.canonical_url()
'https://www.bbcgoodfood.com/recipes/monster-cupcakes'
```

### `ingredient_groups() -> List[IngredientGroup]`

Returns a `list` of groups of ingredients. Some recipes on some websites will present the ingredients in groups, where each group contains the ingredients required for a particular aspect of the recipe.

Each element of the returned `list` is an `IngredientGroup` object. An `IngredientGroup` object has a `purpose` (for example, *for the sauce*) and a `list` of ingredients.

> [!IMPORTANT]
>
> All scrapers inherit this function. By default, it returns a single group with purpose of `None` and the ingredients set to the output of `ingredients()`. This function should be overridden in scrapers for website that use ingredient groups. See [this guide](in-depth-guide-ingredient-groups.md) for help on implementing this.

```py
>>> scraper.ingredient_groups()
[
	IngredientGroup(
		ingredients=[
			'250g self-raising flour',
			'25g cocoa powder',
			'175g light muscovado sugar',
			'85g unsalted butter , melted',
			'5 tbsp vegetable or sunflower oil',
			'150g pot fat-free natural yogurt',
			'1 tsp vanilla extract', '3 large eggs'
		],
		purpose=None),
	IngredientGroup(
		ingredients=[
			'85g unsalted butter , softened',
			'1 tbsp milk',
			'½ tsp vanilla extract',
			'200g icing sugar , sifted',
			'food colourings (optional)',
			'sweets and sprinkles, to decorate'
		],
		purpose='For the frosting and decorating')
]
```

### `instruction_list()`

Return a `list` of instructions. This `list` is generated by splitting the output of `instructions()` on newline characters.

```py
>>> scraper.instructions_list()
[
	'Heat oven to 190C/170C fan/gas 5 and line a 12-hole muffin tin with deep cake cases. Put all the cake ingredients into a large bowl and beat together with electric hand beaters until smooth. Spoon the mix into the cases, then bake for 20 mins until risen and a skewer inserted into the middle comes out dry. Cool completely on a rack. Can be made up to 3 days ahead and kept in an airtight container, or frozen for up to 1 month.',
 	'For the frosting, work the butter, milk and vanilla into the icing sugar until creamy and pale. Colour with food colouring, if using, then create your own gruesome monster faces using sweets and sprinkles.'
]
```

### `language() -> str`

Returns the language of recipe page, as defined within the page's HTML.
This is typically a two-letter BCP 47 language code, such as 'en' for English or 'de' for German,
but may also include the dialect or variation, such as 'en-US' for American English.

The language code is based on BCP 47 standards.
For a comprehensive list of BCP 47 language codes, refer to this GitHub Gist:
https://gist.github.com/typpo/b2b828a35e683b9bf8db91b5404f1bd1

```py
>>> scraper.language()
'en'
```

### `links() -> List[Dict[str, str]]`

Returns a `list` of all links found in the page HTML defined in an `<a>` element. For each link, the attributes of the HTML element are returned as a `dict`.

```py
>>> scraper.links()
[
	{
		'class': ['popup-toggle-button'],
		'aria-label': 'Toggle main-navigation popup',
  		'aria-haspopup': 'true',
  		'href': '#main-navigation-popup'
	},
	... # etc.
]
```

### `site_name() -> str | None`

Returns the website name, as defined in the page's HTML. If the page does not define this, this function returns `None`

```py
>>> scraper.site_name()
None
```

### `to_json() -> List[str, str]`

Returns the output of all functions implemented by this scraper as a `dict`.

```py
>>> scraper.to_json()
{
	'author': 'Good Food team',
	'canonical_url': 'https://www.bbcgoodfood.com/recipes/monster-cupcakes',
	'category': 'Treat',
	... # etc.
}
```

## Optional functions

### `category() -> str`

Semi-structured field that can contain a mix of cuisine type (for example, country names), mealtime (breakfast/dinner/etc) and dietary properties (gluten-free, vegetarian). The value is defined by the website, so it may overlap with other scraper functions (e.g. `cuisine()`).

```py
>>> scraper.category()
'Treat'
```

### `cook_time() -> int`

Returns the time to cook the recipe in minutes, excluding any time to prepare ingredients.

```py
>>> scraper.cook_time()
20
```

### `cuisine() -> str`

Returns the cuisine of the recipe.

```py
>>> scraper.cuisine()
# Not implemented!
```

### `nutrients() -> Dict[str, str]`

Returns a `dict` of nutrition information. Each nutrition item is usually given per unit of yield, e.g. per servings, per item. The keys of the `dict` are the nutrients (including calories) and the values are the amount of that nutrient, including the unit.

```py
>>> scraper.nutrients()
{
	'calories': '389 calories',
 	'fatContent': '19 grams fat',
 	'saturatedFatContent': '9 grams saturated fat',
 	'carbohydrateContent': '53 grams carbohydrates',
 	'sugarContent': '36 grams sugar',
 	'fiberContent': '1 grams fiber',
 	'proteinContent': '5 grams protein',
 	'sodiumContent': '0.3 milligram of sodium'
}
```

### `prep_time() -> int`

Returns the time to prepare the ingredients for the recipe in minutes.

```py
>>> scraper.prep_time()
30
```

### `ratings() -> float`

Returns the recipe rating. When available, this is usually the average of all the ratings given to the recipe on the website.

```py
scraper.ratings()
# Not implemented!
```

### `ratings_count() -> float`

Returns the total number of ratings contributed to the recipes rating.

```py
scraper.ratings_count()
# Not implemented!
```

### `reviews() -> List[Dict[str, str]]`

Returns a `list` of reviews about the recipe from the website. Each review is a `dict` containing the reviewer's name (`str`) and their review (`str`).

### `equipment() -> List[str] | None`

Returns a list of cooking equipment needed for provided recipe.

```py
>>> scraper.equipment()
['Mixing Bowl', 'Whisk', 'Baking Tray']
```

### `cooking_method() -> str`

Returns the method of cooking the recipe.

```py
>>> scraper.cooking_method()
'Stovetop'
```

### `keywords() -> list`

Returns a `list` of keywords associated with a recipe.

```py
>>> scraper.keywords()
['easy', 'quick', 'dinner']
```

### `dietary_restrictions"() -> List[str] | None`

Returns the dietary restrictions specified by the recipe.

```py
>>> scraper.dietary_restrictions()
['Vegan Diet', 'Vegetarian Diet']
```
