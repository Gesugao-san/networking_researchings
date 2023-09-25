#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter


if __name__ == '__main__':
    lexer = get_lexer_by_name('ssdp')
    formatter = TerminalFormatter()
    code = 'NOTIFY * HTTP/1.1\r\nHOST: localhost:1900'
    msg = highlight(code, lexer, formatter)
    print(msg)






