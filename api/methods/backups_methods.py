#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from api.methods.files_methods import read_backups


# Get the path of a backup by id
def get_backup_path(backup_id):
    backups = read_backups()
    for backup in backups:
        if backup["id"] == backup_id:
            return backup["path"]

# Get the directories that the backup where the backup has to be created
def get_backup_directories(backup_id):
    backups = read_backups()
    for backup in backups:
        if backup["id"] == backup_id:
            return backup["directories"]
