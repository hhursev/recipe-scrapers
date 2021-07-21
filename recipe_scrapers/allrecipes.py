import inspect
import logging
import re

from ._abstract import AbstractScraper

logging.basicConfig()
logger = logging.getLogger(__name__)


UNITIZERX = re.compile(r"^([0-9.]+)\s*([^0-9.]*)$")
EXT_NUTRS_SEL = "section.recipe-nutrition.nutrition-section div.nutrition-row"
EXT_NUTRS_CLASH = "Extended nutrient name clashes with basic nutrient:" "%s = %s vs %s"
EXT_NUTR_PCT = "Got unit type from a percentage value: %s = %s (%s)"
DICT_FIELDS = [
    "author",
    "canonical_url",
    "image",
    "ingredients",
    "instructions",
    "language",
    "links",
    "ratings",
    "site_name",
    "title",
    "total_time",
    "url",
    "yields",
]


class AllRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "allrecipes.com"

    def author(self):
        # NB: In the schema.org 'Recipe' type, the 'author' property is a
        # single-value type, not an ItemList.
        # allrecipes.com seems to render the author property as a list
        # containing a single item under some circumstances.
        # In those cases, the SchemaOrg class will fail due to the unexpected
        # type, and this method is called as a fallback.
        # Rather than implement non-standard handling in SchemaOrg, this code
        # provides a (hopefully temporary!) allrecipes-specific workaround.
        author = self.schema.data.get("author")
        if author and isinstance(author, list) and len(author) == 1:
            author = author[0].get("name")
        return author

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def nutrients(self):
        def unhandled(n):
            logger.warn(f"Unhandled AllRecipes extended nutrient format: {n}")

        # Find extended nutrients
        ext_nutrs = {}
        for node in self.soup.select(EXT_NUTRS_SEL):
            tupl = list(node.stripped_strings)
            if len(tupl) >= 2:
                name = tupl[0].strip(":")
                ext_nutrs[name] = tupl[1]
                if len(tupl) == 3:
                    if "%" in tupl[2]:
                        ext_nutrs[name + "%"] = tupl[2].strip(" %")
                    else:
                        unhandled(node)
            else:
                unhandled(node)

        # Marry basic and extended nutrients, reporting name clashes
        nutr = self.schema.nutrients()
        for name, value in ext_nutrs.items():
            if name in nutr:
                logger.warn(EXT_NUTRS_CLASH, name, value, ext_nutrs[name])
                nutr[f"Ext {name}"] = value
            else:
                nutr[name] = value

        return nutr

    def nutrients_unitized(self):
        unitized = {}
        for name, value in self.nutrients().items():
            try:
                new_value = UNITIZERX.match(value).groups()
            except AttributeError:
                new_value = (value, None)
            if name.endswith("%"):
                if new_value[1]:
                    logger.warn(EXT_NUTR_PCT, name, value, str(new_value[1]))
                else:
                    new_value = (value, "RDA")

            # Special cases: transfer unit types found in name
            if not new_value[1]:
                if "calories" in name:
                    new_value = (value, "calories")
            unitized[name] = (float(new_value[0]), new_value[1])
        return unitized

    def to_dict(self, html=False, unitized=False, skip_attribs=None):
        obj = {}
        for attrib_name in DICT_FIELDS:
            if skip_attribs and attrib_name in skip_attribs:
                continue
            attrib = getattr(self.__class__, attrib_name, None)
            if attrib:
                if inspect.isfunction(attrib) or inspect.ismethod(attrib):
                    obj[attrib_name] = attrib(self)
                else:
                    obj[attrib_name] = attrib
            else:
                logger.warn("Expected attrib not found: %s", attrib_name)
        if html:
            obj["html"] = str(self.soup)
        if unitized:
            obj["nutrients"] = self.nutrients_unitized()
        else:
            obj["nutrients"] = self.nutrients()
        return obj
