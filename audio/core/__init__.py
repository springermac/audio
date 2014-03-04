#!/usr/bin/env python
# coding=utf-8

from audio.core.registry import Registry

Registry().create()

from .registry import Registry
from .settings import Settings