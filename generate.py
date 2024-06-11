# mypy: allow-untyped-defs

# generate.py generates a new recipe scraper.
import ast
import json
import os
import sys

import requests

from recipe_scrapers._abstract import HEADERS
from recipe_scrapers._utils import get_host_name

template_class_name = "Template"
template_host_name = "example.com"


def generate_scraper(class_name, host_name):
    with open("templates/scraper.py") as source:
        code = source.read()
        program = ast.parse(code)

        state = GenerateScraperState(class_name, host_name, code)
        for node in ast.walk(program):
            if not state.step(node):
                break

        output = f"recipe_scrapers/{class_name.lower()}.py"
        with open(output, "w") as target:
            target.write(state.result())


def generate_scraper_test(class_name, host_name):
    if not os.path.isdir(f"tests/test_data/{host_name}"):
        os.mkdir(f"tests/test_data/{host_name}")

    testjson = {
        "host": host_name,
        "canonical_url": "",
        "site_name": "",
        "author": "",
        "language": "",
        "title": "",
        "ingredients": "",
        "ingredient_groups": "",
        "instructions": "",
        "instructions_list": "",
        "total_time": "",
        "yields": "",
        "image": "",
        "description": "",
    }

    output = f"tests/test_data/{host_name}/{class_name.lower()}.json"
    with open(output, "w") as target:
        json.dump(testjson, target, indent=2)


def init_scraper(class_name):
    with open("recipe_scrapers/__init__.py", "r+") as source:
        code = source.read()
        program = ast.parse(code)

        state = InitScraperState(class_name, code)
        for node in ast.walk(program):
            if not state.step(node):
                break

        source.seek(0)
        source.write(state.result())
        source.truncate()


def generate_test_data(class_name, host_name, content):
    output = f"tests/test_data/{host_name}/{class_name.lower()}.testhtml"
    with open(output, "w", encoding="utf-8") as target:
        target.write(content.decode(encoding="utf-8"))


class ScraperState:
    def __init__(self, code):
        self.code = code
        self.line_offsets = get_line_offsets(code)
        self.replacer = Replacer(code)

    def result(self):
        return self.replacer.result()

    def _offset(self, node):
        return self.line_offsets[node.lineno - 1] + node.col_offset

    def _replace(self, replacement_text, start, length):
        self.replacer.replace(replacement_text, start, length)


class GenerateScraperState(ScraperState):
    def __init__(self, class_name, host_name, code):
        super().__init__(code)
        self.class_name = class_name
        self.host_name = host_name

    def step(self, node):
        if isinstance(node, ast.ClassDef) and node.name == template_class_name:
            offset = self._offset(node)
            segment_end = self.code.index(template_class_name, offset)
            self._replace(self.class_name, segment_end, len(template_class_name))

        if isinstance(node, ast.Constant) and node.value == template_host_name:
            offset = self._offset(node)
            segment_end = self.code.index(template_host_name, offset)
            self._replace(self.host_name, segment_end, len(template_host_name))

        return True


class InitScraperState(ScraperState):
    def __init__(self, class_name, code):
        super().__init__(code)
        self.class_name = class_name
        self.module_name = class_name.lower()
        self.state = "import"
        self.last_node = None

    def step(self, node):
        if self.state == "import":
            return self._import(node)
        elif self.state == "init":
            return self._init(node)
        else:
            return False

    def _import(self, node):
        if isinstance(node, ast.Module) or isinstance(node, ast.Import):
            return True

        if isinstance(node, ast.ImportFrom):
            if node.module > self.module_name and node.level > 0:
                offset = self._offset(node)
                import_statement = (
                    f"\nfrom .{self.module_name} import {self.class_name}"
                )
                self._replace(import_statement, offset, 0)
                self.state = "init"
            self.last_node = node
        elif isinstance(self.last_node, ast.ImportFrom):
            offset = (
                self.line_offsets[self.last_node.lineno - 1]
                + self.last_node.end_col_offset
            )
            segment_end = self.code.index("\n", offset)
            import_statement = f"\nfrom .{self.module_name} import {self.class_name}"
            self._replace(import_statement, segment_end, 0)
            self.state = "init"
            return self._init(node)

        return True

    def _init(self, node):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if (
                    hasattr(target, "id")
                    and target.id == "SCRAPERS"
                    and isinstance(node.value, ast.Dict)
                ):
                    for key in node.value.keys:
                        if (
                            isinstance(key, ast.Call)
                            and isinstance(key.func, ast.Attribute)
                            and isinstance(key.func.value, ast.Name)
                        ):
                            if key.func.value.id > self.class_name:
                                offset = self._offset(key)
                                init_statement = f" {self.class_name}.host(): {self.class_name},\n   "
                                self._replace(init_statement, offset, 0)
                                return False
                            self.last_node = key

            if isinstance(self.last_node, ast.Call):
                offset = (
                    self.line_offsets[self.last_node.lineno - 1]
                    + self.last_node.end_col_offset
                )
                segment_end = self.code.index("\n", offset)
                init_statement = f"\n    {self.class_name}.host(): {self.class_name},"
                self._replace(init_statement, segment_end, 0)
                return False

        return True


class Replacer:
    def __init__(self, code):
        self.code = code
        self.delta = 0
        self.replacements = []

    def replace(self, replacement_text, start, length):
        self.replacements.append((replacement_text, start, length))

    def result(self):
        code = self.code
        for replacement_text, start, length in self.replacements:
            start = start + self.delta
            end = start + length
            code = code[:start] + replacement_text + code[end:]
            self.delta += len(replacement_text) - length

        return code


def get_line_offsets(code):
    offset = 0
    indices = [0]
    try:
        while True:
            index = code.index("\n", offset)
            indices.append(index)
            offset = index + 1
    except ValueError:
        return indices


def main():
    if len(sys.argv) < 3:
        print("Usage: generate.py ScraperClassName url")
        exit(1)

    class_name = sys.argv[1]
    url = sys.argv[2]
    host_name = get_host_name(url)
    testhtml = requests.get(url, headers=HEADERS).content

    generate_scraper(class_name, host_name)
    generate_scraper_test(class_name, host_name)
    generate_test_data(class_name, host_name, testhtml)
    init_scraper(class_name)


if __name__ == "__main__":
    main()
