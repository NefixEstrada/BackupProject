#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask import Flask
from flask_restful import Api

# Methods imports
from api.methods.add_endpoints import add_endpoints

# App initialization
app = Flask(__name__)
api = Api(app)


# Add endpoints
add_endpoints(api)

# Run the app
app.run(port=5000, debug=True)
