#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import json
from flask_restful import Resource, reqparse
from api.methods.backups_methods import get_backup, get_archives
from api.methods.commands_methods import get_output, execute_command
from api.methods.normalization_methods import normalize_string, make_tree

# Archive resource
class Archive(Resource):

    # GET
    def get(self, backup_id, archive_name):
        """
        Get all the files of an archive
        """
        backup = get_backup(backup_id)
        content = get_output(f"borg list --json-lines {backup['path']}::{archive_name}").split('\n')[:-2]
        content = [json.loads(item) for item in content]

        tree_content = make_tree(content)
        return {"content": tree_content}, 200

    def put(self, backup_id, archive_name):
        """
        Renames an archive
        """
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, help="This is the new name that the archive is going to have")
        args = parser.parse_args()

        archives = get_archives(backup_id)

        if any(archive["name"] == args["name"] for archive in archives):
            return {"message": "Sorry, there's already an archive with that name. Please, use another name instead"}, 409

        elif not args["name"]:
            return {"message": "Sorry, the name can't be blank!"}, 400

        else:
            backup = get_backup(backup_id)
            execute_command(f"borg rename {backup['path']}::{archive_name} {normalize_string(args['name'])}")

            return {"message": "Successfully renamed the archive!"}, 200

    def delete(self, backup_id, archive_name):
        """
        Deletes an archive
        """
        backup = get_backup(backup_id)
        execute_command(f"borg delete --force {backup['path']}::{archive_name}")

        return {"message": "Successfully deleted the archive!"}, 200
