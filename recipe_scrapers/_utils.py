def normalize_string(string):
    return string.replace(
        '\xa0', ' ').replace(  # &nbsp;
        '\n', ' ').replace(
        '  ', ' ').strip()
