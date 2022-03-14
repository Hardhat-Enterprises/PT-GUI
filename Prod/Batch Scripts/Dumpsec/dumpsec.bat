@echo off

DumpSec.exe /rpt=userscol /saveas=csv /outfile=dumpsec.txt

@echo File dumpsec.txt created

@echo off
timeout 2 >nul
exit