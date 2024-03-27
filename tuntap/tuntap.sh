#!/bin/bash


# Check if a filename is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <python_script>"
    exit 1
fi

# Execute the Python script with elevated privileges
sudo -E python3 "$@"

