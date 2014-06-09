from _ipython import _c
from _ipython import _p
import datetime
t = datetime.datetime.now().strftime("%y%m%d%H%M%S")
_c(t) # take screenshot
_p('![()](%s.png)' %(t)) # put link to clipboard
