# In Depth Guide: Scraper Functions

> **Draft**
> This in depth guide is intended to give more detail about the functions that make up the public API for scrapers.
>
>To include:
>
>* All functions, grouped by whether they're mandatory, inherited, optional
> * The return type for each function
> * Detail about what the content of the returned value should be

## Mandatory methods

The following fields are generally considered mandatory and efforts should be made to support them when creating a new scraper.

* `host() -> str`
* `title() -> str`
* `total_time() -> str`
* `image() -> str`
* `ingredients() -> List[str]`
* `instructions() -> str`
* `yields() -> str`

## Inherited methods

* `instruction_list()`
* `links() -> List[str]`
* `to_json() -> List[str, str]`
* `canonical_url() -> str`
* `language() -> str`

## Optional methods

The following fields are generally considered optional. If the website doesn't support them, that's fine. If it does (or you can extract the information from the html) go ahead and add the functionality.

* `prep_time() -> str`
* `cook_time() -> str`
* `ingredient_groups() -> List[IngredientGroup]`
* `nutrients() -> Dict[str, str]`?
* `category() -> str`
* `ratings() -> float`
* `reviews() -> Dict[str, str]`
