# cli.py
#
# This file implements the command-line interface (CLI) for the Aegispy framework.
# It allows users to quickly scaffold new projects from a template repository.
#
# Usage:
#   python cli.py new <project_name>
#
# This will clone the template repository into a new directory with the given project name.
#
# You can extend this CLI by adding more commands to the argparse setup.
#
"""
Aegispy CLI for project scaffolding and management.
Run 'python cli.py new <project_name>' to create a new project from the template.
"""

import os
import subprocess
import argparse

TEMPLATE_REPO = "https://github.com/Aksel588/AegisPy"

def create_project(name):
    """
    Clone the template repository into a new directory with the given name.
    Args:
        name (str): The name of the new project directory.
    """
    base_dir = os.path.join(os.getcwd(), name)
    if os.path.exists(base_dir):
        print(f"Error: Directory '{name}' already exists.")
        return

    print(f"Cloning template repo into '{base_dir}'...")
    subprocess.run(["git", "clone", TEMPLATE_REPO, base_dir], check=True)
    print(f"Project '{name}' created at {base_dir}")

def main():
    """
    Parse command-line arguments and execute the requested command.
    """
    parser = argparse.ArgumentParser(description="Aegispy CLI")
    parser.add_argument('command', choices=['new'], help='Command to run')
    parser.add_argument('name', help='Project name')
    args = parser.parse_args()

    if args.command == 'new':
        create_project(args.name)

if __name__ == "__main__":
    main()