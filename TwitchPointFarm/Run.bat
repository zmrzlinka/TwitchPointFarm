@echo off
:start
"C:\Users\miros\AppData\Local\Programs\Python\Python310\python.exe" "C:\Users\miros\Documents\TwitchPointFarm\Manager.py"
timeout /t 1800 /nobreak >nul 2>&1
goto :start