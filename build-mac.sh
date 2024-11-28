#!/bin/bash

# Ensure the script exits if any command fails
set -e

# Run PyInstaller to create the standalone executable
arch -x86_64 pyinstaller client-mac.spec

# Print a message indicating that the build is complete
echo "Build complete. Executable created."