# mypy: allow-untyped-defs

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
        field = scraper_field.__name__
        try:
            return getattr(self.opengraph, field)()
        except NotImplementedError as e:
            msg = f"OpenGraph extractor does not implement '{field}' field"
            raise NotImplementedError(msg) from e

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
        field = scraper_field.__name__
        try:
            return getattr(self.schema, field)()
        except NotImplementedError as e:
            msg = f"Schema.org extractor does not implement '{field}' field"
            raise NotImplementedError(msg) from e

    return wrapper
