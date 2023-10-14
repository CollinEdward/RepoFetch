#!/bin/bash

# Define the script name, output directory, and PyInstaller command
script_name="main.py"
output_dir="dist"
pyinstaller_cmd="pyinstaller"

# Check if PyInstaller is available
if ! command -v $pyinstaller_cmd &> /dev/null; then
    echo "Error: PyInstaller is not installed or not in the system's PATH."
    echo "Please install PyInstaller or ensure it's available in your PATH."
    exit 1
fi

# Run PyInstaller
$pyinstaller_cmd --name=RepoFetch --onefile $script_name

# Build the executable
$pyinstaller_cmd $script_name.spec

# Move the executable to the output directory
mv $script_name $output_dir

echo "Executable created in the $output_dir directory."
