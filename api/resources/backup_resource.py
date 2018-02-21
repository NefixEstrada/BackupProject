#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource, reqparse


# Backup resource
class Backup(Resource):

    # GET
    def get(self):
        """
        Gets a list of all the archives of a specific backup
        """
        pass

    # POST
    def post(self):
        """
        Creates a new archive based on the paths specified in the settings.json file
        """
        pass

    # PUT
    def put(self):
        """
        Edits the backup name or / and the paths to create the backup
        """
        pass
