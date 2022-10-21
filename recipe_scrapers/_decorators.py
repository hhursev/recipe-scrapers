from functools import wraps

def opengraph_fallback(scraper_field):
    @wraps(scraper_field)
    def wrapper(self):
        try:
            result = scraper_field(self)
        except Exception:
            result = None
        if result:
            return result
        return getattr(self.opengraph, scraper_field.__name__)()
    return wrapper

def schemaorg_fallback(scraper_field):
    @wraps(scraper_field)
    def wrapper(self):
        try:
            result = scraper_field(self)
        except Exception:
            result = None
        if result:
            return result
        return getattr(self.schema, scraper_field.__name__)()
    return wrapper
