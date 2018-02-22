#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import unicodedata
import string as string_library


# Normalize string
def normalize_string(string):
    print(string)
    # Remove accents and non UTF-8 strings
    string = "".join(letter for letter in unicodedata.normalize("NFKD", string) if letter in string_library.ascii_letters or letter == " ")
    string = string.replace(" ", "_")

    # Remove consecutive _'s
    new_string = []
    for number in range(len(string)):
        current_character = string[number]
        if not(number != 0 and current_character == string[number - 1] and current_character == "_"):
            new_string.append(current_character)
    new_string = "".join(new_string)

    if new_string[0] == "_":
        new_string = new_string[1:]

    elif new_string[-1] == "_":
        new_string = new_string[:-1]

    return new_string


# Normalize parser
def normalize_parser(parser_args):
    return {arg_name: normalize_string(arg_value) for arg_name, arg_value in parser_args.items()}


# Beautify string
def beautify_string(string):
    return string.replace("_", " ").title()
