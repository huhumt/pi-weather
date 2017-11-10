#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def print_processbar(precentage):

    """
    print processbar when download file
    """

    buf = ''
    cur_process = (int(precentage * 100)) / 2

    for i in range(1, 51):
        # fill buffer
        if i <= cur_process:
            buf += '='
        else:
            buf += ' '

    # print process bar
    sys.stdout.write("[%s]  %.2f%%\r" % (buf, precentage))
    # force print buffered data onto screen
    sys.stdout.flush()
