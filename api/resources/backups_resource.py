#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import os
import json
from flask_restful import Resource, reqparse
from api.methods.commands_methods import execute_command, get_output
from api.methods.files_methods import read_settings, read_backups, write_backups
from api.methods.normalization_methods import normalize_string
from api.methods.directories_methods import check_directory, check_directories_array


# Backups resource
class Backups(Resource):

    # GET
    def get(self):
        """
        List all the backups stored in settings.json
        """
        backups = read_backups()

        return backups, 200

    # POST
    # TODO: - Location header
    # TODO: - Check if there's already an existing backup with that name
    # TODO: - Encryption stuff
    # TODO: - Folders to make the backup
    # TODO: - Deleting method just deletes one backup
    def post(self):
        """
        Create a new backup repository
        """
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=True, help="This is the name that is going to be displayed")
        parser.add_argument("directories", type=str, required=True, help="This are the directories that the backup is going to have")
        args = parser.parse_args()

        backups_path = read_settings("backups_path")
        repo_directory_name = normalize_string(args["name"])
        backup_path = os.path.join(backups_path, repo_directory_name)
        directories_to_backup = [directory for directory in args["directories"].split(", ")]
        bad_directories = check_directories_array(directories_to_backup)

        if (not check_directory(backups_path)) or (check_directory(backup_path)):
            return {"message": "Sorry, either the backup already exists or the user doesn't have permissions to read / write in the backups directory specified in the settings"}, 409

        elif len(bad_directories) != 0:
            return {"message": f"Sorry, the directories {bad_directories} weren't found or the user doesn't have permissions to read them"}, 404

        execute_command(f"borg init -e none {backup_path}")
        backup_info = json.loads(get_output(f"borg info --json {backup_path}"))

        new_backup = {
            "id": backup_info["repository"]["id"],
            "path": backup_info["repository"]["location"],
            "name": args["name"],
            "directories": directories_to_backup
        }

        backups = read_backups()
        backups.append(new_backup)
        write_backups(backups)

        return {"message": "Successfully created the backup!"}, 201

    # DELETE
    def delete(self):
        """
        Deletes all the backups
        """
        backups = read_backups()
        for backup in backups:
            execute_command(f"rm -rf {backup['path']}")

        write_backups([])

        return {"message": "Successfully deleted all the backups!"}, 200
