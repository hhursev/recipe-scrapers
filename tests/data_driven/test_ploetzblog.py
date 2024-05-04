import pathlib
import unittest

from ..data_utils import load_test, run_mandatory_tests, run_optional_test


class PloetzblogTest(unittest.TestCase):

    def test_ploetzblog(self):
        testhtml = pathlib.Path(
            "tests/data_driven/test_data/ploetzblog.de/ploetzblog.testhtml"
        )
        testjson = testhtml.with_suffix(".json")

        expect, actual = load_test("ploetzblog.de", testhtml, testjson)

        run_mandatory_tests(self, expect, actual)
        run_optional_test(self, expect, actual)
