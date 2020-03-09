"""Convert LaTeX-style subscripts and superscripts
to Unicode subscript and superscript characters.
"""

import fileinput
import re

subscripts = {
    '0': '₀',
    '1': '₁',
    '2': '₂',
    '3': '₃',
    '4': '₄',
    '5': '₅',
    '6': '₆',
    '7': '₇',
    '8': '₈',
    '9': '₉',
    '+': '₊',
    '-': '₋',
    '=': '₌',
    '(': '₍',
    ')': '₎',
    'a': 'ₐ',
    'e': 'ₑ',
    'h': 'ₕ',
    'k': 'ₖ',
    'l': 'ₗ',
    'm': 'ₘ',
    'n': 'ₙ',
    'o': 'ₒ',
    'p': 'ₚ',
    's': 'ₛ',
    't': 'ₜ',
    'x': 'ₓ',
}

superscripts = {
    '0': '⁰',
    '1': '¹',
    '2': '²',
    '3': '³',
    '4': '⁴',
    '5': '⁵',
    '6': '⁶',
    '7': '⁷',
    '8': '⁸',
    '9': '⁹',
    '+': '⁺',
    '-': '⁻',
    '=': '⁼',
    '(': '⁽',
    ')': '⁾',
    'i': 'ⁱ',
    'n': 'ⁿ',
}

def replace(text, char_dict):
    new_text = ""
    for char in text:
        new_text += char_dict.get(char, char)
    return new_text

def subscript(text):
    return replace(text, subscripts)

def superscript(text):
    return replace(text, superscripts)

def replace_match(match):
    if match.group(1) == "_":
        return subscript(match.group(2))
    elif match.group(1) == "^":
        return superscript(match.group(2))

def parse(line):
    # sub/superscript characters in _{} or ^{} braces (LaTeX-style)
    line = re.sub(r'([_^])\{([^}]*)\}', replace_match, line)
    # sub/superscript characters following _ or ^
    line = re.sub(r'([_^])(.)', replace_match, line)
    return line

if __name__ == "__main__":
    for line in fileinput.input():
        print(parse(line), end="")
