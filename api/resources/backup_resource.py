#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import json
from flask_restful import Resource, reqparse
from api.methods.backups_methods import get_backup_path
from api.methods.commands_methods import get_output


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
    def post(self, backup_id):
        """
        Creates a new archive based on the paths specified in the backups.json file
        """
        pass

    # PUT
    def put(self, backup_id):
        """
        Edits the backup name or / and the paths to create the backup
        """
        pass
