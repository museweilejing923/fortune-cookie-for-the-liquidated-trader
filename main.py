#!/usr/bin/env python3
"""Fortune-cookie writer for a freshly liquidated trader.

One fixed fortune is kept in FORTUNE and written to disk only after it
has survived every rule in RULES. A fortune has to look forward, so the
word "will" is part of the bargain. The program is fully deterministic:
same input, same bytes, every run.
"""

import sys

FORTUNE = "You will lose everything, then gain wisdom. Wisdom is non-refundable and cannot be withdrawn."
CHAR_CAP = 160
WORD_CAP = 20
TARGET = "/output/entry.txt"
ENDERS = (".", "!", "?")
PUNCT = frozenset(".,!?;:'\"-() ")


def abort(why):
    print(f"bad fortune: {why}", file=sys.stderr)
    raise SystemExit(1)


def _nonempty(text):
    return bool(text.strip()) if text else False


def _fits_chars(text):
    return len(text) <= CHAR_CAP


def _fits_words(text):
    return len(text.split()) <= WORD_CAP


def _no_controls(text):
    return not any(ord(ch) < 32 for ch in text)


def _clean_edges(text):
    return text == text.strip() and "  " not in text and "\n" not in text


def _lettered(text):
    return any(ch.isalpha() for ch in text)


def _not_just_punct(text):
    return any(ch not in PUNCT for ch in text)


def _not_just_numbers(text):
    return not text.strip().isdigit()


def _ends_well(text):
    return text.rstrip().endswith(ENDERS)


def _looks_forward(text):
    return "will" in text.lower()


def _no_zero_width_joiner(text):
    # A zero-width joiner is invisible ink: it changes nothing the eye
    # sees while changing the bytes, so it has no place in a fortune.
    return "\u200d" not in text


RULES = (
    ("fortune is empty", _nonempty),
    ("fortune tops the 20 word limit", _fits_words),
    ("fortune tops the 160 character limit", _fits_chars),
    ("fortune ends without punctuation", _ends_well),
    ("fortune holds control characters", _no_controls),
    ("fortune has messy edges or a newline", _clean_edges),
    ("fortune has no letters", _lettered),
    ("fortune is only punctuation", _not_just_punct),
    ("fortune is only digits", _not_just_numbers),
    ("a fortune must look forward and say 'will'", _looks_forward),
    ("a fortune must not hide a zero-width joiner", _no_zero_width_joiner),
)


def validate(text):
    for problem, test in RULES:
        if not test(text):
            abort(problem)


def main():
    validate(FORTUNE)
    with open(TARGET, "w", encoding="utf-8") as out:
        out.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
