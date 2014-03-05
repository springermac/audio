#!/usr/bin/env python
# coding=utf-8

import re


class Utils(object):
    def __init__(self):
        super(Utils, self).__init__()
        self.badchars = re.compile(r'[^A-Za-z0-9-_. ]+|^\.|\.$|^ | $|^$')
        self.badnames = re.compile(r'(aux|com[1-9]|con|lpt[1-9]|prn)(\.|$)')

    def make_name(self, s):
        name = self.badchars.sub('_', s)
        if self.badnames.match(name):
            name = '_'+name
        return name
