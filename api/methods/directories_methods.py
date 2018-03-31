#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import os


# Check directory
def check_directory(path):
    return os.path.exists(path) and os.access(path, os.R_OK)


# Check directories array
def check_directories_array(directories):
    bad_directories = []
    for directory in directories:
        if not check_directory(directory):
            bad_directories.append(directory)

    if not bad_directories:
        return False, bad_directories

    return []
