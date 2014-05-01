@echo off
echo Running startup script:
echo %0 
doskey ed=gvim --remote-silent $*
set PATH=%PATH%;C:\Users\mchl\Downloads\portableApps\JPEGView64\;C:\Users\mchl\Downloads\portableApps\MiniCap
echo System info:
cmd
