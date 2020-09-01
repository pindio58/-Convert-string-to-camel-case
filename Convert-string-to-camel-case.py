import re


def to_camel_case (text):
    container = re.split ('[- _]' , text)
    if not text: return ''

    elif text[0].isupper(): return ''.join (name.title () for name in container)

    else: return container[0] + ''.join (name.title () for name in container[1:])

