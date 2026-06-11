@echo off
cd /d "%~dp0"
echo ========================================
echo   Fengyu WANG Site - Port 8001
echo   http://localhost:8001
echo   Press Ctrl+C to stop
echo ========================================
python -m http.server 8001
pause

