#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import json


# Read the settings
def read_settings(key):
    with open("../settings.json") as file:
        json_file = json.load(file)["settings"]

    if key:
        return json_file[key]
    else:
        return json_file


# Read the backups
def read_backups():
    with open("backups.json") as file:
        json_file = json.load(file)

    return json_file["backups"]


# Write to the backups
def write_backups(content):
    with open("backups.json", "w") as file:
        to_write = {"backups": content}
        json.dump(to_write, file, indent=4)
