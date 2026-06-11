@echo off
echo === Cleaning temporary files ===
if exist "..\scss" rmdir /s /q "..\scss"
if exist "..\ts" rmdir /s /q "..\ts"
if exist "..\start-8001.bat" del "..\start-8001.bat"
echo Done.