import functools
import requests
from bs4 import BeautifulSoup
from language_tags import tags

from ._schemaorg import (
    SchemaOrg,
    SchemaOrgException
)


# some sites close their content for 'bots', so user-agent must be supplied
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
}


class AbstractScraper:
    class Decorators:
        """
        Define decorators for AbstractScraper methods here.
        """
        @staticmethod
        def schema_org_priority(decorated):
            """
            Use SchemaOrg parser with priority (if there's data in it)
            On exception raised - continue by default.
            If there's no data (no schema implemented on the site) - continue by default
            """
            @functools.wraps(decorated)
            def schema_org_priority_wrapper(self, *args, **kwargs):
                function = getattr(self.schema, decorated.__name__)
                if not function:
                    raise SchemaOrgException(
                        "Function '{}' not found in schema"
                        .format(decorated.__name)
                    )

                if not self.schema.data:
                    return decorated(self, *args, **kwargs)

                try:
                    value = function(*args, **kwargs)
                except SchemaOrgException:
                    return decorated(self, *args, **kwargs)
                return value or decorated(self, *args, **kwargs)

            return schema_org_priority_wrapper

        @staticmethod
        def bcp47_validate(decorated):
            @functools.wraps(decorated)
            def bcp47_validate_wrapper(self, *args, **kwargs):
                tag = tags.tag(decorated(self, *args, **kwargs))
                return str(tag) if tag.valid else None
            return bcp47_validate_wrapper

        @staticmethod
        def default_exception_handling(decorated):
            """
            As web scraping is too unpredictable in nature, handle
            whatever exceptions may arise with defaulting values.

            If you wish to handle exceptions on your own you can pass the
            default_exception_handling=False flag.

            Example:
            from recipe_scrapers import scrape_me
            scraper = scrape_me('<recipe_url>', default_exception_handling=False)
            scraper.total_time()  # and etc.
            """
            @functools.wraps(decorated)
            def default_exception_handling_wrapper(self, *args, **kwargs):
                if self.default_exception_handling:
                    try:
                        return decorated(self, *args, **kwargs)
                    except:
                        on_exception_return = {
                            'title': '',
                            'total_time': 0,
                            'yields': '',
                            'image': '',
                            'ingredients': [],
                            'instructions': '',
                            'reviews': -1,
                            'links': [],
                            'language': 'en',
                        }
                        return on_exception_return.get(decorated.__name__)
                else:
                    return decorated(self, *args, **kwargs)

            return default_exception_handling_wrapper

    def __init__(self, url, test=False, meta_http_equiv=False, default_exception_handling=True):
        if test:  # when testing, we load a file
            with url:
                page_data = url.read()
        else:
            page_data = requests.get(url, headers=HEADERS).content

        self.default_exception_handling = default_exception_handling
        self.meta_http_equiv = meta_http_equiv
        self.soup = BeautifulSoup(page_data, "html.parser")
        self.schema = SchemaOrg(page_data)
        self.url = url
        # if self.schema.data:
        #     print("Class: %s has schema." % (
        #         self.__class__.__name__
        #     ))

    def url(self):
        return self.url

    def host(self):
        """ get the host of the url, so we can use the correct scraper """
        raise NotImplementedError("This should be implemented.")

    @Decorators.default_exception_handling
    @Decorators.schema_org_priority
    def title(self):
        raise NotImplementedError("This should be implemented.")

    @Decorators.default_exception_handling
    @Decorators.schema_org_priority
    def total_time(self):
        """ total time it takes to preparate the recipe in minutes """
        raise NotImplementedError("This should be implemented.")

    @Decorators.default_exception_handling
    @Decorators.schema_org_priority
    def yields(self):
        """ The number of servings or items in the recipe """
        raise NotImplementedError("This should be implemented.")

    @Decorators.default_exception_handling
    @Decorators.schema_org_priority
    def image(self):
        """
        Image of the recipe

        Try to fetch it from og:image if not implemented.
        """
        try:
            image = self.soup.find(
                'meta',
                {'property': 'og:image', 'content': True}
            )
            return image.get('content')
        except AttributeError:  # if image not found
            raise NotImplementedError("This should be implemented.")

    @Decorators.default_exception_handling
    @Decorators.bcp47_validate
    @Decorators.schema_org_priority
    def language(self):
        """
        Human language the recipe is written in.

        May be overridden by individual scrapers.
        """
        candidate_languages = set()
        html = self.soup.find(
            'html',
            {'lang': True}
        )
        candidate_languages.add(html.get('lang'))

        # Deprecated: check for a meta http-equiv header
        # See: https://www.w3.org/International/questions/qa-http-and-lang
        meta_language = self.soup.find(
            'meta',
            {
                'http-equiv': lambda x: x and x.lower() == 'content-language',
                'content': True
            }
        ) if self.meta_http_equiv else None
        if meta_language:
            for language in meta_language.get('content').split(','):
                candidate_languages.add(language)
                break

        # If other langs exist, remove 'en' commonly generated by HTML editors
        if len(candidate_languages) > 1 and 'en' in candidate_languages:
            candidate_languages.remove('en')

        # Return the first candidate language
        for language in candidate_languages:
            return language

    @Decorators.default_exception_handling
    @Decorators.schema_org_priority
    def ingredients(self):
        raise NotImplementedError("This should be implemented.")

    @Decorators.default_exception_handling
    @Decorators.schema_org_priority
    def instructions(self):
        raise NotImplementedError("This should be implemented.")

    @Decorators.default_exception_handling
    @Decorators.schema_org_priority
    def ratings(self):
        raise NotImplementedError("This should be implemented.")

    @Decorators.default_exception_handling
    def reviews(self):
        raise NotImplementedError("This should be implemented.")

    @Decorators.default_exception_handling
    def links(self):
        invalid_href = ('#', '')
        links_html = self.soup.findAll('a', href=True)

        return [
            link.attrs
            for link in links_html
            if link['href'] not in invalid_href
        ]
