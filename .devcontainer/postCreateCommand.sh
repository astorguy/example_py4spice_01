#!/bin/bash
# Exit immediately if a command exits with a non-zero status.
set -e

# Update package list and install ngspice
echo "--- Installing ngspice ---"
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y ngspice

# Install Python packages
echo "--- Installing Python packages ---"
# Note: The 'pip install' command is run by the 'remoteUser' (vscode),
# so the '--user' flag is appropriate here.
pip install --user \
    ipykernel==7.1.0 \
    matplotlib==3.10.7 \
    numpy==2.3.5 \
    py4spice==0.1.0

echo "🟢🟢🟢 CODESPACE READY 🟢🟢🟢"
