@echo off
echo === Starting HTTP server on port 8001 ===
echo Open http://localhost:8001 in your browser
cd ..
python -m http.server 8001
pause