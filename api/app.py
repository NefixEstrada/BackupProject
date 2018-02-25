#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask import Flask
from flask_cors import CORS 
from flask_restful import Api

# Methods imports
from api.methods.add_endpoints import add_endpoints

# App initialization
app = Flask(__name__)
CORS(app)
api = Api(app)


# Add endpoints
add_endpoints(api)

# Run the app
app.run(port=5000, debug=True, host="192.168.5.24")
