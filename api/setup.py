#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import sys
from urllib import request
import subprocess
import json
import argparse


# Check Python version and if pip is installed
def check_python_and_pip():
    if not sys.version_info >= (3, 6):
        print("Python 3.6 or newer is required to use Backup Project. Please, install it.")
        sys.exit(1)

    else:
        # Try using Pip, if it's not available, ask if the user wants to install it
        try:
            import pip

        except ImportError:
            response = input("Pip isn't installed, do you want to install it? [Y/n]: ")

            if response == "Y" or response == "y" or response == "":
                request.urlretrieve("https://bootstrap.pypa.io/get-pip.py")
                command = f"sudo python-{sys.version_info[0]}.{sys.version_info[1]} get-pip.py"
                subprocess.run(command.split(" "))

                import pip

            else:
                print("You need pip in order to use Backup Project. Please, install it.")
                sys.exit(1)


# Install dependencies
def install_dependencies():
    create_venv_command = f"python{sys.version_info[0]}.{sys.version_info[1]} -m venv venv"
    install_dependencies_command = "./venv/bin/pip install -r requirements.txt"
    subprocess.run(create_venv_command.split(" "))
    subprocess.run(install_dependencies_command.split(" "))


# Create the files
# TODO: Check if the path is correct and if we have permissions on it
def generate_files():
    parser = argparse.ArgumentParser()
    parser.add_argument("--address", "-a", help="Ip adress of the server")
    parser.add_argument("--path", "-p", help="Path of the folder that is going to store all the backups")
    args = parser.parse_args()
    response = {}

    if args.address:
        response["ip_host"] = args.address
    else:
        response["ip_host"] = "0.0.0.0"

    if args.path:
        response["backups_path"] = args.path
    else:
        response["backups_path"] = input("Please, specify the path where the backups are going to be located: ")

    with open("backups.json", "w+") as file:
        to_write = {"backups": []}
        json.dump(to_write, file, indent=4)

    with open("../settings.json", "w+") as file:
        to_write = {"settings": {"backups_path": response["backups_path"], "ip_host": response["ip_host"]}}
        json.dump(to_write, file, indent=4)


# Run the functions
if __name__ == "__main__":
    check_python_and_pip()
    install_dependencies()
    generate_files()
    print(f"Installation successful! To run Backup Program, simply execute 'python{sys.version_info[0]}.{sys.version_info[1]} run_api.py'")
