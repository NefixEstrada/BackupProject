#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import json
from api.methods.files_methods import read_backups
from api.methods.commands_methods import get_output


# Get a backup by id
def get_backup(backup_id):
    backups = read_backups()
    for backup in backups:
        if backup["id"] == backup_id:
            return backup


# Get a list of archives by backup id
def get_archives(backup_id):
    backup_path = get_backup(backup_id)["path"]
    archives = json.loads(get_output(f"borg list --json {backup_path}"))["archives"]

    return archives
