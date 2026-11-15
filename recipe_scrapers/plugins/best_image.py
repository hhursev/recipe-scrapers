import functools
import logging
import re
from collections import OrderedDict
from collections.abc import Iterator
from typing import ClassVar, Optional, Union
from urllib.parse import urljoin, urlsplit

from recipe_scrapers.settings import settings

from ._interface import PluginInterface

logging.basicConfig()
logger = logging.getLogger(__name__)


class BestImagePlugin(PluginInterface):
    """Select the best available recipe image when requested."""

    run_on_hosts = ("*",)
    run_on_methods = ("image",)

    _DIMENSION_PATTERN = re.compile(
        r"(?:^|[^0-9])(?P<width>\d{3,5})[xX](?P<height>\d{3,5})(?:[^0-9]|$)"
    )
    _QUERY_WIDTH_PATTERN = re.compile(r"[?&](?:w|width)=(\d{3,5})", re.IGNORECASE)
    _QUERY_HEIGHT_PATTERN = re.compile(r"[?&](?:h|height)=(\d{3,5})", re.IGNORECASE)
    _JUNK_URL_PATTERN = re.compile(
        r"(?:^|[/.-])(?:favicon|apple-touch-icon|icon(?:[.-][\w-]+)?|logo)(?:[/.?-]|$)",
        re.IGNORECASE,
    )
    _IMAGE_META_PROPS = frozenset(
        {
            "og:image",
            "og:image:url",
            "og:image:secure_url",
            "twitter:image",
            "twitter:image:src",
        }
    )
    _SOURCE_PRIORITY: ClassVar[dict[str, int]] = {
        "primary": 3,
        "schema": 2,
        "opengraph": 1,
        "twitter": 1,
    }

    @classmethod
    def run(cls, decorated):
        @functools.wraps(decorated)
        def decorated_method_wrapper(self, *args, **kwargs):
            logger.setLevel(settings.LOG_LEVEL)
            class_name = self.__class__.__name__
            method_name = decorated.__name__
            logger.debug(
                f"Decorating: {class_name}.{method_name}() with BestImagePlugin"
            )

            image = decorated(self, *args, **kwargs)

            if not getattr(self, "best_image_selection", False):
                return image

            candidates = cls._collect_candidates(self, image)
            if not candidates:
                return image

            best = cls._select_best_candidate(candidates)
            return best or image

        return decorated_method_wrapper

    @classmethod
    def _collect_candidates(cls, scraper, image) -> list[dict]:
        candidates: "OrderedDict[str, dict]" = OrderedDict()
        base_url = cls._resolve_base_url(getattr(scraper, "url", ""))

        def register(entry, source: str) -> None:
            for normalized in cls._normalize_entries(entry):
                cls._merge_candidate(candidates, normalized, source, base_url)

        register(image, "primary")

        schema_images = getattr(getattr(scraper, "schema", None), "data", {})
        if isinstance(schema_images, dict):
            register(schema_images.get("image"), "schema")

        cls._collect_meta_image_candidates(scraper, candidates, base_url)

        return list(candidates.values())

    @classmethod
    def _normalize_entries(cls, entry) -> Iterator[dict]:
        if not entry:
            return

        if isinstance(entry, (list, tuple, set)):
            for item in entry:
                yield from cls._normalize_entries(item)
            return

        if isinstance(entry, dict):
            url = entry.get("url") or entry.get("@id") or entry.get("contentUrl")
            if isinstance(url, list):
                url = url[0]
            if not url:
                return
            width = cls._parse_dimension(
                entry.get("width")
                or entry.get("pixelWidth")
                or entry.get("contentWidth")
            )
            height = cls._parse_dimension(
                entry.get("height")
                or entry.get("pixelHeight")
                or entry.get("contentHeight")
            )
            yield {
                "url": str(url).strip(),
                "width": width,
                "height": height,
            }
            return

        if isinstance(entry, str):
            entry = entry.strip()
            if not entry:
                return
            yield {"url": entry, "width": None, "height": None}
            return

    @classmethod
    def _collect_meta_image_candidates(
        cls,
        scraper,
        candidates: "OrderedDict[str, dict]",
        base_url: str,
    ) -> None:
        soup = getattr(scraper, "soup", None)
        if soup is None:
            return

        images: dict[str, dict] = {}
        current_url: Optional[str] = None
        for meta in soup.find_all("meta"):
            prop = (meta.get("property") or meta.get("name") or "").lower()
            content = meta.get("content")
            if not content:
                continue

            if prop in cls._IMAGE_META_PROPS:
                url = content.strip()
                current_url = url
                source = "twitter" if prop.startswith("twitter:") else "opengraph"
                if url not in images:
                    images[url] = {
                        "url": url,
                        "width": None,
                        "height": None,
                    }
                current = images[url]
                cls._merge_candidate(candidates, current, source, base_url)
            elif (
                prop == "og:image:width"
                and current_url is not None
                and current_url in images
            ):
                images[current_url]["width"] = cls._parse_dimension(content)
                cls._merge_candidate(
                    candidates, images[current_url], "opengraph", base_url
                )
            elif (
                prop == "og:image:height"
                and current_url is not None
                and current_url in images
            ):
                images[current_url]["height"] = cls._parse_dimension(content)
                cls._merge_candidate(
                    candidates, images[current_url], "opengraph", base_url
                )

    @classmethod
    def _merge_candidate(
        cls,
        candidates: "OrderedDict[str, dict]",
        candidate: Union[dict, None],
        source: str,
        base_url: str = "",
    ) -> None:
        if not candidate:
            return

        url = cls._normalize_url(candidate.get("url"), base_url)
        if not url:
            return

        width = cls._parse_dimension(candidate.get("width"))
        height = cls._parse_dimension(candidate.get("height"))

        existing = candidates.get(url)
        if existing is None:
            candidates[url] = {
                "url": url,
                "width": width,
                "height": height,
                "sources": {source},
                "order": len(candidates),
            }
            return

        if width is not None:
            existing["width"] = cls._max_dimension(existing.get("width"), width)
        if height is not None:
            existing["height"] = cls._max_dimension(existing.get("height"), height)
        existing.setdefault("sources", set()).add(source)

    @staticmethod
    def _resolve_base_url(url: str) -> str:
        url = (url or "").strip()
        if not url:
            return ""
        if url.startswith("//"):
            return "https:" + url
        if not url.startswith(("http://", "https://")):
            url = "http://" + url.lstrip("/")
        return url

    @classmethod
    def _normalize_url(cls, url, base_url: str = "") -> Optional[str]:
        if url is None:
            return None

        url = str(url).strip()
        if not url or url.startswith("data:"):
            return None

        if url.startswith("//"):
            url = "https:" + url
        elif not url.startswith(("http://", "https://")):
            resolved_base = cls._resolve_base_url(base_url)
            if resolved_base:
                url = urljoin(resolved_base, url)

        parts = urlsplit(url)
        if parts.scheme not in {"http", "https"} or not parts.netloc:
            return None

        return url

    @classmethod
    def _is_junk_url(cls, url: str) -> bool:
        path = urlsplit(url).path
        return bool(cls._JUNK_URL_PATTERN.search(path))

    @classmethod
    def _source_priority(cls, sources: set[str]) -> int:
        if not sources:
            return 0
        return max(cls._SOURCE_PRIORITY.get(source, 0) for source in sources)

    @staticmethod
    def _max_dimension(current, new):
        if current is None:
            return new
        if new is None:
            return current
        try:
            return max(int(current), int(new))
        except (TypeError, ValueError):
            return current

    @classmethod
    def _parse_dimension(cls, value):
        if value is None:
            return None
        if isinstance(value, (int, float)):
            return int(value)
        if isinstance(value, str):
            match = re.search(r"\d+", value)
            if match:
                try:
                    return int(match.group())
                except ValueError:
                    return None
            return None
        if isinstance(value, dict):
            for key in ("value", "maxValue", "minValue"):
                if key in value:
                    parsed = cls._parse_dimension(value[key])
                    if parsed is not None:
                        return parsed
        return None

    @classmethod
    def _select_best_candidate(cls, candidates: list[dict]) -> Optional[str]:
        best_candidate: Optional[dict] = None
        best_score: tuple[int, ...] = (-1, -1, -1, 0)

        for candidate in candidates:
            score = cls._score_candidate(candidate)
            if score > best_score:
                best_candidate = candidate
                best_score = score

        if best_candidate:
            return best_candidate.get("url")
        return None

    @classmethod
    def _score_candidate(cls, candidate: dict) -> tuple[int, int, int, int]:
        url = candidate.get("url", "")
        if cls._is_junk_url(url):
            return (-1, 0, 0, candidate.get("order", 0))

        width, height = cls._ensure_dimensions(candidate)
        area = 0
        if width and height:
            area = width * height
        elif width or height:
            side = width or height
            if side:
                area = side * side

        source_priority = cls._source_priority(candidate.get("sources", set()))
        secure = 1 if url.startswith("https://") else 0
        order = -candidate.get("order", 0)
        return (area, source_priority, secure, order)

    @classmethod
    def _ensure_dimensions(cls, candidate: dict) -> tuple[Optional[int], Optional[int]]:
        width = candidate.get("width")
        height = candidate.get("height")
        if width and height:
            return int(width), int(height)

        dims = cls._extract_dimensions_from_url(candidate.get("url", ""))
        if dims:
            width = width or dims[0]
            height = height or dims[1]
            candidate["width"] = width
            candidate["height"] = height

        return (
            int(width) if width is not None else None,
            int(height) if height is not None else None,
        )

    @classmethod
    def _extract_dimensions_from_url(cls, url: str) -> Optional[tuple[int, int]]:
        if not url:
            return None

        match = cls._DIMENSION_PATTERN.search(url)
        if match:
            try:
                return int(match.group("width")), int(match.group("height"))
            except ValueError:
                return None

        width = cls._find_query_dimension(cls._QUERY_WIDTH_PATTERN, url)
        height = cls._find_query_dimension(cls._QUERY_HEIGHT_PATTERN, url)
        if width and height:
            return width, height

        return None

    @staticmethod
    def _find_query_dimension(pattern: re.Pattern[str], url: str) -> Optional[int]:
        match = pattern.search(url)
        if match:
            try:
                return int(match.group(1))
            except ValueError:
                return None
        return None
