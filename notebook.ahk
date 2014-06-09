#Persistent 
SetKeyDelay, 30
Capslock::
IfWinExist, vim
{
IfWinNotActive
    {
	WinActivate ;
    }
else
{
	Send, {ALTDOWN}{TAB}{ALTUP}
}
}
Return




