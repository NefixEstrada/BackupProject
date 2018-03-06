#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import json
from time import gmtime, strftime
from flask_restful import Resource, reqparse
from api.methods.backups_methods import get_backup, get_archives
from api.methods.commands_methods import execute_command
from api.methods.files_methods import read_backups, write_backups
from api.methods.normalization_methods import normalize_string


# Backup resource
class Backup(Resource):

    # GET
    def get(self, backup_id):
        """
        Gets a list of all the archives of a specific backup
        """
        archives = get_archives(backup_id)

        return {"archives": archives}, 200

    # POST
    # TODO: Normalize parser
    # TODO: ERR: Archive already exists
    # TODO: progress
    def post(self, backup_id):
        """
        Creates a new archive based on the paths specified in the backups.json file
        """
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, help="This is the name that the archive is going to have (not recommended)")
        args = parser.parse_args()

        archives = get_archives(backup_id)

        if not args["name"]:
            args["name"] = strftime("%Y-%m-%d_%H:%M:%S", gmtime())

        else:
            args["name"] = normalize_string(args["name"])

            if any(archive["name"] == args["name"] for archive in archives):
                return {"message": "Sorry, there's already an archive with that name. Please, use another name instead"}, 409

        backup_path = get_backup(backup_id)["path"]
        backup_directories = " ".join(get_backup(backup_id)["directories"])

        execute_command(f"borg create {backup_path}::{args['name']} {backup_directories}")

        return {"message": "Successfully created the backup. Please allow some time to let the backup finish"}, 201

    # PUT
    # TODO: Check if the directories are valid
    # TODO: Check if there were parameters passed (204)
    # TODO: Change the name of the folder where the repo is located
    # TODO: Normalize paths
    def put(self, backup_id):
        """
        Edits the backup name or / and the paths to create the backup
        """
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, help="The new name that the backup is going to have")
        parser.add_argument("directories", type=str, help="A json array of the directories that are going to be backuped")
        args = parser.parse_args()

        new_backup = get_backup(backup_id)
        if args["name"]:
            new_backup["name"] = args["name"]
        elif args["directories"]:
            new_backup["directories"] = [directory for directory in args["directories"].replace(" ", "").split(",")]

        backups = read_backups()
        for backup in backups:
            if backup["id"] == backup_id:
                for key in new_backup:
                    backup[key] = new_backup[key]

        write_backups(backups)

        return get_backup(backup_id), 200

    # DELETE
    # TODO: Check if the directory is correct
    def delete(self, backup_id):
        """
        Deletes a specific backup based on the id passed
        """
        backups = read_backups()
        for backup in backups:
            if backup["id"] == backup_id:
                execute_command(f"rm -rf {backup['path']}")
                backups.remove(backup)

        write_backups(backups)

        return {"message": "Successfully deleted the backup!"}, 200
