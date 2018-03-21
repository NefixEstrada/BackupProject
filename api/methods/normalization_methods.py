#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import unicodedata
import string as string_library


# Normalize string
def normalize_string(string):
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

    return new_string.lower()


# Normalize parser
def normalize_parser(parser_args, ignore=[]):
    normalized_parser = {}
    for arg_name, arg_value in parser_args.items():
        if arg_value != "" or arg_name not in ignore:
            normalized_parser[arg_name] = normalize_string(arg_value)
        else:
            normalized_parser[arg_name] = arg_value
    return normalized_parser


# Beautify string
def beautify_string(string):
    return string.replace("_", " ").title()


# Make tree from a JSON string
#
# Huge thanks to apianti, without him, I'd still be stuck with this function (in fact, he made it entirely)
#
# Make tree from a JSON string
def make_tree(content):
    def get_children(parent_content, item, splitted_path):
        if len(splitted_path) == 0:
            parent_content.update(item)
            return
        child_name = splitted_path.pop(0)
        child_content = {}
        for child in parent_content["child"]:
            if child["name"] == child_name:
                child_content = child
                break

        if "name" not in child_content:
            child_content["name"] = child_name
            child_content["path"] = parent_content["path"] + "/" + child_name
            child_content["type"] = "d"
            child_content["child"] = []
            parent_content["child"].append(child_content)

        get_children(child_content, item, splitted_path)

    # Transform the output of the command into a tree
    tree_content = []
    for item in content:
        splitted_path = item["path"].split("/")
        parent_name = splitted_path.pop(0)
        parent_content = {}
        for parent in tree_content:
            if parent["name"] == parent_name:
                parent_content = parent
                break

        if "name" not in parent_content:
            parent_content["name"] = parent_name
            parent_content["path"] = parent_name
            parent_content["type"] = "d"
            parent_content["child"] = []
            tree_content.append(parent_content)

        get_children(parent_content, item, splitted_path)

    return tree_content