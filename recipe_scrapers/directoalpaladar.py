import re

from ._abstract import AbstractScraper
from ._exceptions import StaticValueException


class DirectoAlPaladar(AbstractScraper):
    @classmethod
    def host(cls):
        return "directoalpaladar.com"

    def __init__(self, html, url, *args, **kwargs):
        # extruct fails when the page contains empty <script type="application/ld+json"> tags;
        # strip them before processing so self.schema works correctly.
        clean_html = re.sub(
            r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>\s*</script>',
            "",
            html,
        )
        super().__init__(clean_html, url, *args, **kwargs)

    def site_name(self):
        raise StaticValueException(return_value="Directo al Paladar")
