@echo off
echo Ðang cau hinh GitHub...
echo.
set /p repo_url="Nhap link GitHub Repository cua ban (VD: https://github.com/username/novel_web.git): "
if "%repo_url%"=="" (
    echo Ban chua nhap link! Vui long chay lai script.
    pause
    exit /b
)
echo.
echo Dang them remote va push code len GitHub...
git remote add origin %repo_url%
git branch -M main
git push -u origin main
echo.
echo Hoan thanh! Da push source code len GitHub cua ban.
pause
