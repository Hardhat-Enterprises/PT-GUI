@echo off

 

set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )

 

SET count=0
SET /p subnet=Please enter IP address range: 

 

:start
SET /a count=%count%+1

 

cls
ECHO. & ECHO Trying %subnet%.%count% & ECHO.

 

ping -n 1 -w 1000 %subnet%.%count% >nul  
IF %errorlevel%==0 echo %subnet%.%count% UP >> c:\results.log  
IF %errorlevel%==1 echo %subnet%.%count% DOWN >> c:\results.log

 

IF %count%==254 goto :eof

 

GOTO start