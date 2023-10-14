#!/bin/bash

# Define the script name and output directory
script_name="main.py"
output_dir="dist"

# Full path to the pyinstaller command
pyinstaller_cmd="/home/redhat/.local/bin/pyinstaller"

# Run PyInstaller
$pyinstaller_cmd --name=RepoFetch --onefile $script_name

# Build the executable
$pyinstaller_cmd $script_name.spec

# Move the executable to the output directory
mv $script_name $output_dir

echo "Executable created in the $output_dir directory."
