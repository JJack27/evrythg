@echo off
echo Running startup script:
echo %0 
doskey ed=gvim --remote-silent $*
if "%COMPUTERNAME%" EQU  "FP-SURFBRETT-2" goto FP_SURFBRETT_2
if "%COMPUTERNAME%" EQU  "R147032" goto R147032
:FP_SURFBRETT_2
set HOME=C:\Users\Murad\
rem set PYTHON=C:\Anaconda\python.exe
set PATH=%PATH%;C:\Users\Murad\Desktop\portableApps\MiniCapPortable;C:\Users\Murad\Desktop\portableApps\JPEGView64;%HOME%\AppData\Local\Pandoc;C:\Program Files\pstoedit;
:R147032
set PATH=%PATH%;C:\Users\mchl\Downloads\portableApps\MiniCap;C:\Users\mchl\Downloads\portableApps\JPEGView64;C:\Users\mchl\Downloads\portableApps\SumatraPDF-2.3;
:NEXT
cd /d %~dp0
rem cmd.exe
start gvim
ipython notebook --ip=localhost
rem echo System info: