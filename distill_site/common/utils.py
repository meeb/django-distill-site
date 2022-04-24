_allowed_lowercase_ascii_chars = 'abcdefghijklmnopqrstuvwxyz0123456789-_'


def lowercase_ascii_only(s):
    r = ''
    for c in str(s):
        if c in _allowed_lowercase_ascii_chars:
            r += c
    return r
