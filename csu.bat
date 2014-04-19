@echo off
echo Running startup script:
echo %0 
doskey ed=gvim --remote-silent $*
echo System info:
cmd
