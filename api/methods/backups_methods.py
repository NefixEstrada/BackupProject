#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from api.methods.files_methods import read_backups


# Get a backup by id
def get_backup(backup_id):
    backups = read_backups()
    for backup in backups:
        if backup["id"] == backup_id:
            return backup
