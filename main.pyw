from pynput.keyboard import Key, Listener
from keyboard_usage import short_to_full, get_max_shortcut_len

last_typed = list()
started_short = False
MAX_LEN_TO_TYPE = get_max_shortcut_len() + 3  # 3 as error margin


def main():
    with Listener(on_press=on_press) as lnr:
        lnr.join()


def on_press(key):
    check_backspace(key)

    # will not check special buttons like Key.shift, only 'a', ':', ...
    if len(str(key)) != 3:
        return
    
    pressed = str(key).split("'")[1]
    handle_key(pressed=pressed)
    

def handle_key(pressed):
    global started_short
    if started_short:
        last_typed.append(pressed)
        result = short_to_full(last_typed)
        
        if result or not result and len(last_typed) > MAX_LEN_TO_TYPE:
            last_typed.clear()
            started_short = False

    elif pressed == ':':
        started_short = True


def check_backspace(key):
    global started_short
    if str(key) == 'Key.backspace':
        if len(last_typed):
            last_typed.pop()
        else:
            started_short = False


if __name__ == '__main__':
    main()
