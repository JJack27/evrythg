#Persistent 
^Space::
Send,  {"}
sleep, 10
Send,  {+}
sleep, 10
Send,  y
sleep, 10
IfWinExist, MATLAB
{
    WinActivate ;
Send, ^y
sleep, 10
Send, {ENTER}
sleep, 10
Send, {ALTDOWN}{TAB}{ALTUP} 
}
Return
