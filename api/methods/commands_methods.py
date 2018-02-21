#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import subprocess


# Execute a command
def execute_command(command):
    subprocess.run(command.split(" "))


# Get the output of the command
def get_output(command):
    command_output = subprocess.run(command.split(" "), stdout=subprocess.PIPE).stdout.decode("utf-8")
    return command_output
