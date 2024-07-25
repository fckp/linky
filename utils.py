import random

def get_charmap(a, b):
    return list(map(chr, range(a, b)))

symbols = get_charmap(33, 49) + get_charmap(58, 65) + get_charmap(91, 97) + ['~']
numbers = get_charmap(48, 58)
letters = get_charmap(97, 123)
letters += list(map(str.upper, letters))

def gen_str(length, use_letters=True, use_numbers=True, use_symbols=False):
    charmap = []
    if use_letters:
        charmap += letters
    if use_numbers:
        charmap += numbers
    if use_symbols:
        charmap += symbols
    result = ""
    for i in range(length):
        result += random.choice(charmap)
    return result