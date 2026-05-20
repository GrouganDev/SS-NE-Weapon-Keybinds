#!/bin/bash
source ./venvLinux/bin/activate
pip install -r requirements.txt
pyinstaller --onefile main.py
