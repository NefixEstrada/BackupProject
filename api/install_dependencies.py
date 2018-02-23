#!venv/bin/python
# -*- coding: utf-8 -*-

# Imports
import subprocess


# Install the dependencies
def install_dependencies():
    command = "pip -r requirements.txt"
    subprocess.run(command.split(" "))
