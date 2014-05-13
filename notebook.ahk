#Persistent 
Capslock::
Send,  ^a
sleep, 10
Send,  ^c
sleep, 10
IfWinExist, vim
{
IfWinNotActive
    {
	WinActivate ;
	Send, {ESC}
	sleep, 10
	Send, {G}
	sleep, 10
	Send, {o}
	sleep, 10
	Send, {ESC}
	sleep, 10
	Send,  {"}
	sleep, 10
	Send,  {+}
	sleep, 10
	Send,  p
    }
else
{
	Send,  {"}
	sleep, 10
	Send,  {+}
	sleep, 10
	Send,  y
	Send, {ALTDOWN}{TAB}{ALTUP}
}
}
Return
