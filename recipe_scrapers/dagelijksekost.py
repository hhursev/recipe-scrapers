from ._abstract import AbstractScraper
import json


def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize DP table
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Compute distances
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,  # Deletion
                dp[i][j - 1] + 1,  # Insertion
                dp[i - 1][j - 1] + cost,
            )  # Substitution

    return dp[m][n]


def find_json(blocks):
    res = []
    for block in blocks:
        if not block.string or "self.__next_f.push" not in block.string:
            continue
        start_idx = block.string.find(":[")
        end_idx = block.string.rfind('"')
        if start_idx == -1 or end_idx == -1 or start_idx >= end_idx:
            continue
        json_content = block.string[start_idx + 1 : end_idx]
        try:
            unescaped_content = json_content.encode(
                "latin-1", "backslashreplace"
            ).decode("unicode-escape")
            res.extend(json.loads(unescaped_content))
        except json.JSONDecodeError:
            continue
    return res


def find_instructions(data):
    results = []
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "instructions":
                results.append(value)
            elif isinstance(value, (dict, list)):
                results.extend(find_instructions(value))
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (dict, list)):
                results.extend(find_instructions(item))
    return results


def parse_instructions(instructions):
    try:
        return "\n".join([instructions[key] for key in sorted(instructions, key=int)])
    except (KeyError, ValueError):
        return None


class DagelijkseKost(AbstractScraper):
    @classmethod
    def host(cls):
        return "dagelijksekost.vrt.be"

    def canonical_url(self):
        if "@id" in self.schema.data:
            extracted_url = self.schema.data["@id"]
            if extracted_url.startswith("http"):
                return extracted_url
        return self.url

    def instructions(self):
        script_blocks = self.soup.find_all("script")
        recipe_json = find_json(script_blocks)
        instruction_candidates = find_instructions(recipe_json)

        short_instructions = self.schema.instructions()

        first_instruction = short_instructions.split("\n")[0]
        if not first_instruction:
            return short_instructions

        # Probably always matches exactly, but just in case, allow some fuzziness
        dist = min(3, len(first_instruction) // 5)

        for instructions in instruction_candidates:
            if "0" not in instructions:
                continue

            if levenshtein_distance(first_instruction, instructions["0"]) > dist:
                continue

            parsed_instructions = parse_instructions(instructions)

            if not parsed_instructions:
                continue

            return parsed_instructions

        return short_instructions
