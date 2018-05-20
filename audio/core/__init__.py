#!/usr/bin/env python
# coding=utf-8

from audio.core.registry import Registry

Registry().create()

from .registry import Registry
from .settings import Settings
from .utils import Utils, is_linux, is_macosx, is_win