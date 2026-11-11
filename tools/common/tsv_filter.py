"""Drop TSV rows on copy when a column equals a given value.

Add a DropRule to reuse this for another platform, file, column, or value.
A rule applies only when its platform and filename match. None means "any".
The comparison is the whole cell, not a substring, so the same text in another
column is left alone. Line endings of the kept rows are unchanged.
"""

import shutil
import sys


class DropRule:
    def __init__(self, column, values, platforms=None, filenames=None, reason=""):
        """column is a header name or a 0-based index."""
        self.column = column
        self.values = tuple(values)
        self.platforms = None if platforms is None else tuple(platforms)
        self.filenames = None if filenames is None else tuple(filenames)
        self.reason = reason

    def applies(self, platform, filename):
        if self.platforms is not None and platform not in self.platforms:
            return False
        if self.filenames is not None and filename not in self.filenames:
            return False
        return True


# iOS builds use the platform id "mobile". These portrait sprites are on
# PC/Steam and absent from the iOS sprites/logos sheet; loading them crashes
# the credits. Steam ("desk") has no rule, so the source rows stay.
DROP_RULES = (
    DropRule(
        column="portrait",
        values=("Logos/DolbyDigital", "Logos/DigitalSurround"),
        platforms=("mobile",),
        filenames=("dialog.tsv",),
        reason="portrait sprite is missing on this platform and crashes the credits",
    ),
)


def rules_for(platform, filename):
    return [rule for rule in DROP_RULES if rule.applies(platform, filename)]


def _encode(value):
    return value.encode("utf-8") if isinstance(value, str) else value


def _column_index(headers, column):
    if isinstance(column, int):
        if column < 0 or column >= len(headers):
            raise ValueError(f"Column index {column} is outside the header ({len(headers)} columns)")
        return column
    name = _encode(column)
    if name not in headers:
        raise ValueError(f"Column {column!r} is not in the header")
    return headers.index(name)


def filter_tsv(data, rules):
    """Return (filtered_bytes, per_rule_counts) for rules that already apply."""
    lines = data.splitlines(keepends=True)
    counts = {rule: 0 for rule in rules}
    if not lines or not rules:
        return data, counts

    headers = lines[0].rstrip(b"\r\n").split(b"\t")
    resolved = []
    for rule in rules:
        index = _column_index(headers, rule.column)
        resolved.append((rule, index, {_encode(value) for value in rule.values}))

    kept = [lines[0]]
    for line in lines[1:]:
        cells = line.rstrip(b"\r\n").split(b"\t")
        matched = None
        for rule, index, values in resolved:
            if index < len(cells) and cells[index] in values:
                matched = rule
                break
        if matched is None:
            kept.append(line)
        else:
            counts[matched] += 1
    return b"".join(kept), counts


def copy_with_rules(source_path, dest_path, platform, filename):
    """Copy source to dest, dropping rows that match rules for this copy.

    Returns how many rows were removed. With no matching rule this is a plain copy.
    """
    rules = rules_for(platform, filename)
    if not rules:
        shutil.copy(source_path, dest_path)
        return 0

    with open(source_path, "rb") as src:
        filtered, counts = filter_tsv(src.read(), rules)
    with open(dest_path, "wb") as dst:
        dst.write(filtered)
    shutil.copymode(source_path, dest_path)

    removed = 0
    for rule, count in counts.items():
        if not count:
            continue
        removed += count
        values = ", ".join(rule.values)
        detail = f": {rule.reason}" if rule.reason else ""
        print(
            f"Removed {count} row(s) from {filename} "
            f"where {rule.column} is {values} for platform '{platform}'{detail}"
        )
    return removed


def main(argv):
    if len(argv) != 5:
        print(
            f"Usage: {argv[0] if argv else 'tsv_filter.py'} "
            "<source> <dest> <platform> <filename>",
            file=sys.stderr,
        )
        return 1
    copy_with_rules(argv[1], argv[2], argv[3], argv[4])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
