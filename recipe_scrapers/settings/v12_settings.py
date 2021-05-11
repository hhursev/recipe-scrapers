# Settings that will make recipe-scrapers>=13.0.0 act almost identical as recipe-scrapers<13.0.0
SUPPRESS_EXCEPTIONS = True
META_HTTP_EQUIV = True
ON_EXCEPTION_RETURN_VALUES = {
    "title": "",
    "total_time": 0,
    "yields": "",
    "image": "",
    "ingredients": [],
    "instructions": "",
    "ratings": -1,
    "reviews": None,
    "links": [],
    "language": "en",
    "nutrients": {},
}
