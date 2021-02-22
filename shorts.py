# double colon => returning single colon and not checkin' what's after
def double_colon():
    return ':'


def quit():
    return ''


SHORTCUTS = {
    ':': double_colon,
    'quit': quit
}
