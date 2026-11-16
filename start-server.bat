@echo off
echo Menjalankan local web server untuk Undangan Lia & Rizki...
cd /d "%~dp0"
start "" http://localhost:8080
python -m http.server 8080
pause
