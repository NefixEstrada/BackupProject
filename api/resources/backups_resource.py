#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import os
import json
from flask_restful import Resource, reqparse
from api.methods.commands_methods import execute_command, get_output
from api.methods.files_methods import read_settings, read_backups, write_backups
from api.methods.normalization_methods import normalize_parser, beautify_string


# Backups resource
class Backups(Resource):

    # GET
    def get(self):
        backups = read_backups()

        return backups, 200

    # POST
    # TODO: - Location header
    # TODO: - Check if there's already an existing backup with that name
    # TODO: - Encryption stuff
    # TODO: - Folders to make the backup
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=True, help="This is the name that is going to be displayed")
        args = normalize_parser(parser.parse_args())

        backups_path = read_settings("backups_path")
        backup_path = os.path.join(backups_path, args["name"])
        execute_command(f"borg init -e none {backup_path}")
        backup_info = json.loads(get_output(f"borg info --json {backup_path}"))

        new_backup = {
            "id": backup_info["repository"]["id"],
            "path": backup_info["repository"]["location"],
            "name": beautify_string(args["name"])
        }

        backups = read_backups()
        backups.append(new_backup)
        write_backups(backups)

        return {"message": "Successfully created the backup!"}, 201

    # DELETE
    def delete(self):
        backups = read_backups()
        print(backups)
        print(len(backups))

        for backup in backups:
            execute_command(f"rm -rf {backup['path']}")
            backups.remove(backup)
            print(backup)

        write_backups(backups)

        return {"message": "Successfully deleted all the backups!"}, 200
