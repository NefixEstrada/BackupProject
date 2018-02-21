#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import json
from time import gmtime, strftime
from flask_restful import Resource, reqparse
from api.methods.backups_methods import get_backup_path, get_backup_directories
from api.methods.commands_methods import get_output, execute_command
from api.methods.normalization_methods import normalize_parser


# Backup resource
class Backup(Resource):

    # GET
    def get(self, backup_id):
        """
        Gets a list of all the archives of a specific backup
        """
        backup_path = get_backup_path(backup_id)
        archives = json.loads(get_output(f"borg list --json {backup_path}"))["archives"]

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

        if not args["name"]:
            name = strftime("%Y-%m-%d_%H:%M:%S", gmtime())
        backup_path = get_backup_path(backup_id)
        backup_directories = " ".join(get_backup_directories(backup_id))

        execute_command(f"borg create {backup_path}::{name} {backup_directories}")
        return None, 200

    # PUT
    def put(self, backup_id):
        """
        Edits the backup name or / and the paths to create the backup
        """
        pass
