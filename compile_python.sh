#!/bin/bash
sudo apt-get install python3-dev
sudo apt install python3.12-venv
python3 -m venv venvLinux
source ./venvLinux/bin/activate
pip install -r requirements.txt
pyinstaller --onefile main.py
