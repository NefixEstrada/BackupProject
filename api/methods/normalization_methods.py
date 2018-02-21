#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import unicodedata
import string as string_library

# Normalize string
# TODO: - Better normalizer
def normalize_string(string):
    # Remove accents and non UTF-8 strings
    string = ''.join(letter for letter in unicodedata.normalize("NFKD", string) if letter in string_library.ascii_letters or letter == " ")
    characters_to_avoid = "|/&;:{}\$%#@= "
    for character in characters_to_avoid.split():
        string = string.replace(character, "_")
    return string.lower()


# Normalize parser
def normalize_parser(parser_args):
    return {arg_name: normalize_string(arg_value) for arg_name, arg_value in parser_args.items()}


# Beautify string
def beautify_string(string):
    return string.replace("_", " ").title()
