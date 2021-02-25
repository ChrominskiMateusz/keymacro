from pyautogui import press, write, hotkey
from time import sleep

# double colon => returning single colon and not checkin' what's after
def double_colon():
    write(':')


def quit():
    pass


#example
def fyt():
    write('facebook.com')
    press('enter')
    sleep(0.15)
    hotkey('ctrl', 't')
    write('youtube.com')
    press('enter')


SHORTCUTS = {
    ':': double_colon,
    'quit': quit,
    'fyt': fyt
}
