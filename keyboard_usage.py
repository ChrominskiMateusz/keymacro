from pyautogui import press, write
from shorts import SHORTCUTS
from sys import exit as sys_exit

def get_max_shortcut_len():
    max = 0
    for short in SHORTCUTS.keys():
        if len(short) > max:
            max = len(short)
    return max


def check_shorts(shortcut):
    for short in SHORTCUTS.keys():
        if shortcut == short:
            return SHORTCUTS[short]()
    return False


def short_to_full(typed):
    shortcut = ''.join(typed)
    to_print = check_shorts(shortcut)
    if to_print is False:
        return False
    
    press('backspace', presses=len(shortcut) + 1)   # +1 for ':'
    write(to_print)
    
    if shortcut == 'quit':
        sys_exit()
    return True
