import os
import subprocess
import argparse

TEMPLATE_REPO = "https://github.com/Aksel588/AegisPy"

def create_project(name):
    base_dir = os.path.join(os.getcwd(), name)
    if os.path.exists(base_dir):
        print(f"Error: Directory '{name}' already exists.")
        return

    print(f"Cloning template repo into '{base_dir}'...")
    subprocess.run(["git", "clone", TEMPLATE_REPO, base_dir], check=True)
    print(f"Project '{name}' created at {base_dir}")

def main():
    parser = argparse.ArgumentParser(description="Aegispy CLI")
    parser.add_argument('command', choices=['new'], help='Command to run')
    parser.add_argument('name', help='Project name')
    args = parser.parse_args()

    if args.command == 'new':
        create_project(args.name)

if __name__ == "__main__":
    main()