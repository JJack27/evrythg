#Persistent 
^Space::
Send,  {"}
sleep, 10
Send,  {+}
sleep, 10
Send,  y
sleep, 10
IfWinExist, IPython
{
    WinActivate ;
Send, ^v
sleep, 10
Send, {ENTER}
sleep, 10
Send, {ALTDOWN}{TAB}{ALTUP} 
}
Return

#Persistent 
!Space::
Send,  {Esc}
sleep, 10
Send,  {"}
sleep, 10
Send,  {+}
sleep, 10
Send,  y
sleep, 10
Send,  y
sleep, 10
IfWinExist, IPython
{
    WinActivate ;
Send, ^v
sleep, 10
Send, {ENTER}
sleep, 10
Send, {ALTDOWN}{TAB}{ALTUP} 
}
Return

