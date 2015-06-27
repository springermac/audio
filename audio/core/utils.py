#!/usr/bin/env python
# coding=utf-8

import os
import re


class Utils(object):
    def __init__(self):
        super(Utils, self).__init__()
        if os.name == 'nt':
            self.badchars = re.compile(r'[\\/:\*?"<>\|]')
            self.badnames = re.compile(r'(aux|com[1-9]|con|lpt[1-9]|prn)(\.|$)')
        else:
            self.badchars = re.compile(r'[\\/\|]')
            self.badnames = re.compile('(?!)')

    def clean_name(self, s, check=False):
        s = str(s)
        name = self.badchars.sub('_', s)
        if self.badnames.match(name):
            name = '_'+name
        if check:
            return s == name
        return name
