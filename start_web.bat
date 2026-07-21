@echo off
title Duy Nghich Viet Truyen - Web Server

rem Chuyen thu muc lam viec ve noi chua file bat nay
cd /d "%~dp0"

echo Dang khoi dong Web Server cuc bo (Port 8000)...

rem Tim va tat tien trinh python dang chiem port 8000 neu co
for /f "tokens=5" %%a in ('netstat -aon ^| find ":8000" ^| find "LISTENING"') do taskkill /f /pid %%a >nul 2>&1

rem Khoi dong server
start /B python server.py
echo.
echo Dang tao duong link Public co dinh...
echo =========================================================
echo Duong link cua ban LUON LUON LA: https://duynghichtruyen1.loca.lt
echo Ban hay luu link nay lai va gui cho ban be nhe!
npx localtunnel --port 8000 --subdomain duynghichtruyen1
pause
