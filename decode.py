#!/usr/bin/python3
"""Decoding email address using Metrojobb hash."""
from html.parser import HTMLParser


def decode_hash(hash):
    """Use this function, Luke."""
    a = hash
    e = ''
    r = '0x' + a[0:2]
    n = 2
    while True:
        try:
            e += '&#' + \
                ('0' +
                 hex(int('0x' + str(int(a[n:n + 2], 16) ^ int(r, 16)), 16))
                 )[3:]
            n += 2
        except ValueError:
            h = HTMLParser()
            return(h.unescape(e))
            
            
if __name__ == '__main__':
    print(decode_hash(input('Enter the hashed email: ')))
