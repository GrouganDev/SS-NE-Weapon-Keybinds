#!/bin/bash
sudo apt-get update
sudo apt-get install python3-dev
sudo apt install python3-venv
python3 -m venv venvLinux
source ./venvLinux/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
