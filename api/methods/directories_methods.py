#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import os


# Check directory
def check_directory(path):
    if os.path.exists(path) and os.access(path, os.R_OK):
        return True

    else:
        return False


# Check directories array
def check_directories_array(directories):
    bad_directories = []
    for directory in directories:
        if not check_directory(directory):
            bad_directories.append(directory)

    if len(bad_directories) == 0:
        return True, []

    else:
        return False, bad_directories
