from pyautogui import press
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
            return SHORTCUTS[short]
    return False


def short_to_full(typed):
    shortcut = ''.join(typed)
    to_execute = check_shorts(shortcut)
    if to_execute is False:
        return False
    
    press('backspace', presses=len(shortcut) + 1)   # +1 for ':'
    to_execute()

    if shortcut == 'quit':
        sys_exit()
    return True
