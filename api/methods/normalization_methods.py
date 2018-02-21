#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Normalize string
# TODO: - Better normalizer
def normalize_string(string):
    return string.lower().replace(" ", "_")


# Normalize parser
def normalize_parser(parser_args):
    return {arg_name: normalize_string(arg_value) for arg_name, arg_value in parser_args.items()}


# Beautify string
def beautify_string(string):
    return string.replace("_", " ").title()
