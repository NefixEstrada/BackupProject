#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import json


# Read the settings
def read_settings(key):
    with open("settings.json") as f:
        json_file = json.load(f)["settings"]

    if key:
        return json_file[key]

    return json_file


# Read the backups
def read_backups():
    with open("api/backups.json") as f:
        json_file = json.load(f)

    return json_file["backups"]


# Write to the backups
def write_backups(content):
    with open("api/backups.json", "w") as f:
        to_write = {"backups": content}
        json.dump(to_write, f, indent=4)
