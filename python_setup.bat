@echo offf
py -m pip install --upgrade pip && py -m venv venvWindows && call "%~dp0venvWindows\Scripts\activate.bat" && pip install -r requirements.txt 