#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource
from api.methods.backups_methods import get_backup
from api.methods.commands_methods import execute_command

# Archive resource
class Archive(Resource):

    # GET
    def get(self, backup_id, archive_name):
        """
        Get all the files of an archive
        """
        pass

    def put(self, backup_id, archive_name):
        """
        Renames an archive
        """
        pass

    def delete(self, backup_id, archive_name):
        """
        Deletes an archive
        """
        backup = get_backup(backup_id)
        execute_command(f"borg delete --force {backup['path']}::{archive_name}")

        return {"message": "Successfully deleted the archive!"}, 200
