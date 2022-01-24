from ctypes import *
import sys
import os
from time import sleep
from rpa import *

def is_admin():
    try:
        return windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    # Principal
    block_input = windll.user32.BlockInput 
    block_input(True)
    teste()
    block_input(False)
else:
    res = windll.shell32.ShellExecuteW(
    None, 'runas',
    '"' + sys.executable + '"',
    '"' + os.getcwd() + '\\user.py' + '"',
    None, 1)
    if res <= 32:
	    raise WindowsError(f'ShellExecute returned error code {res}')

    

