@echo off
call "%~dp0venvWindows\Scripts\activate.bat" && pip install -r requirements.txt pyinstaller && pyinstaller --onefile "%~dp0\main.py" 
