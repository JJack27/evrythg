#Persistent 
SetKeyDelay, 30
Capslock::
Send,  ^a
Send,  ^c
Send,  {ESC}
IfWinExist, vim
{
IfWinNotActive
    {
	WinActivate ;
	Send, {ESC}
	Send, {G}
	Send, {o}
	Send, {Enter}
	Send, {ESC}
	Send, {"}
	Send, {+}
	Send, p
	Send, j
	Send, $
    }
else
{
	Send, {ALTDOWN}{TAB}{ALTUP}
}
}
Return




