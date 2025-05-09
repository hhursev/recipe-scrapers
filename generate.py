# generate.py generates a new recipe scraper.
import ast
import json
import sys
from pathlib import Path
import re

import requests

from recipe_scrapers._abstract import HEADERS
from recipe_scrapers._utils import get_host_name

TEMPLATE_CLASS = "Template"
TEMPLATE_HOST = "example.com"
BASE_DIR = Path(__file__).parent
SCRAPERS_DIR = BASE_DIR / "recipe_scrapers"
TEST_DATA_DIR = Path("tests/test_data")


def main():
    if len(sys.argv) < 3:
        print("Usage: python generate.py <ScraperClassName> <url1> [url2 ...]")
        sys.exit(1)

    class_name = sys.argv[1]
    urls = sys.argv[2:]

    for idx, url in enumerate(urls, start=1):
        suffix = f"_{idx}" if len(urls) > 1 else ""
        name = f"{class_name}{suffix}"
        module_file = SCRAPERS_DIR / f"{name.lower()}.py"
        if module_file.exists():
            print(f"Error: Scraper '{name}' already exists at {module_file}")
            continue

        host = get_host_name(url)
        html = requests.get(url, headers=HEADERS).content

        _generate_scraper(name, host)
        _generate_tests_and_data(name, host, html)
        _register_scraper(name)

        print(f"Successfully generated scraper for {name} ({host})")


def _generate_scraper(class_name, host):
    template = BASE_DIR / "templates/scraper.py"
    code = template.read_text()
    tree = ast.parse(code)
    replacer = _TemplateReplacer(code, class_name, host)

    for node in ast.walk(tree):
        replacer.apply(node)

    out = SCRAPERS_DIR / f"{class_name.lower()}.py"
    out.write_text(replacer.result())


def _generate_tests_and_data(class_name, host, html):
    dest = TEST_DATA_DIR / host
    dest.mkdir(parents=True, exist_ok=True)

    data = {
        k: ""
        for k in (
            "host",
            "canonical_url",
            "site_name",
            "author",
            "language",
            "title",
            "ingredients",
            "instructions_list",
            "total_time",
            "yields",
            "image",
            "description",
        )
    }
    data["host"] = host

    (dest / f"{class_name.lower()}.json").write_text(json.dumps(data, indent=2) + "\n")
    (dest / f"{class_name.lower()}.testhtml").write_bytes(html)


def _register_scraper(class_name):
    module = class_name.lower()
    init_path = SCRAPERS_DIR / "__init__.py"
    lines = init_path.read_text().splitlines()

    new_import = f"from .{module} import {class_name}"
    import_re = re.compile(r"^from \.[\w]+ import [\w]+$")
    idxs = [i for i, line in enumerate(lines) if import_re.match(line)]
    existing = [lines[i] for i in idxs]
    if new_import not in existing:
        underscore_imports = [
            imp for imp in existing if imp.split()[1].startswith("._")
        ]
        regular_imports = [
            imp for imp in existing if not imp.split()[1].startswith("._")
        ] + [new_import]
        underscore_imports = sorted(
            underscore_imports, key=lambda imp: imp.split()[-1].lower()
        )
        regular_imports = sorted(
            regular_imports, key=lambda imp: imp.split()[-1].lower()
        )
        all_imports = underscore_imports + regular_imports
        start, end = idxs[0], idxs[-1]
        lines = lines[:start] + all_imports + lines[end + 1 :]

    new_entry = f"    {class_name}.host(): {class_name},"
    out, block, in_block = [], [], False
    for line in lines:
        if line.strip().startswith("SCRAPERS") and line.strip().endswith("{"):
            in_block = True
            out.append(line)
            continue
        if in_block:
            if line.strip() == "}":
                block.append(new_entry)
                sorted_block = sorted(set(block), key=lambda e: e.lower())
                out.extend(sorted_block)
                out.append(line)
                in_block = False
            else:
                block.append(line)
            continue
        out.append(line)

    init_path.write_text("\n".join(out) + "\n")


class _TemplateReplacer:
    def __init__(self, code, class_name, host):
        self.code = code
        self.class_name = class_name
        self.host = host
        self.repls = []
        self.lines = [0] + [i + 1 for i, c in enumerate(code) if c == "\n"]

    def apply(self, node):
        if isinstance(node, ast.ClassDef) and node.name == TEMPLATE_CLASS:
            pos = self._pos(node)
            end = self.code.index(TEMPLATE_CLASS, pos)
            self._add(end, len(TEMPLATE_CLASS), self.class_name)
        elif isinstance(node, ast.Constant) and node.value == TEMPLATE_HOST:
            pos = self._pos(node)
            end = self.code.index(TEMPLATE_HOST, pos)
            self._add(end, len(TEMPLATE_HOST), self.host)

    def _pos(self, node):
        return self.lines[node.lineno - 1] + node.col_offset

    def _add(self, start, length, text):
        self.repls.append((start, length, text))

    def result(self):
        code, delta = self.code, 0
        for start, length, text in sorted(self.repls, key=lambda x: x[0]):
            s = start + delta
            code = code[:s] + text + code[s + length :]
            delta += len(text) - length
        return code


class _InitRegistrar:
    def __init__(self, class_name, code):
        self.class_name = class_name
        self.module = class_name.lower()
        self.code = code
        self.stage = "import"
        self.repls = []
        self.lines = [0] + [i + 1 for i, c in enumerate(code) if c == "\n"]

    def step(self, node):
        if self.stage == "import":
            return self._handle_import(node)
        if self.stage == "init":
            return self._handle_init(node)
        return False

    def _handle_import(self, node):
        if isinstance(node, ast.ImportFrom) and node.level > 0:
            pos = self.lines[node.lineno - 1] + node.end_col_offset
            text = f"\nfrom .{self.module} import {self.class_name}"
            self._add(pos, 0, text)
            self.stage = "init"
        return True

    def _handle_init(self, node):
        if isinstance(node, ast.Assign):
            if any(getattr(t, "id", None) == "SCRAPERS" for t in node.targets):
                if isinstance(node.value, ast.Dict):
                    key = next(
                        (k for k in node.value.keys if isinstance(k, ast.Call)), None
                    )
                    if key:
                        pos = self.lines[key.lineno - 1] + key.end_col_offset
                        entry = f"\n    {self.class_name}.host(): {self.class_name},"
                        self._add(pos, 0, entry)
                        return False
        return True

    def _add(self, start, length, text):
        self.repls.append((start, length, text))

    def result(self):
        code, delta = self.code, 0
        for start, length, text in sorted(self.repls, key=lambda x: x[0]):
            s = start + delta
            code = code[:s] + text + code[s + length :]
            delta += len(text) - length
        return code


if __name__ == "__main__":
    main()
