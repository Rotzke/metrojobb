#!/usr/bin/python3
"""Decoding email address using Metrojobb hash."""
from html.parser import HTMLParser


def decode_hash(hashed):
    """Use this function, Luke."""
    email = ''
    prefix = '0x' + hashed[0:2]
    slicer = 2
    while True:
        try:
            email += '&#' + \
                ('0' +
                 hex(int(
                     '0x' + str(
                         int(hashed[slicer:slicer + 2], 16) ^ int(prefix, 16)),
                     16))
                 )[3:]
            slicer += 2
        except ValueError:
            parser = HTMLParser()
            return parser.unescape(result)


if __name__ == '__main__':
    print(decode_hash(input('Enter the hashed email: ')))
