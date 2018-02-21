#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Resources imports
from api.resources.backups_resource import Backups
from api.resources.backup_resource import Backup


# Add all the endpoints to the API
def add_endpoints(api):
    root = "/api"
    api.add_resource(Backups, f"{root}/backups")
    api.add_resource(Backup , f"{root}/backup/<backup_id>")