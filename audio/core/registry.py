#!/usr/bin/env python
# coding=utf-8


class Registry(object):
    __instance__ = None

    def __new__(cls):
        if not cls.__instance__:
            cls.__instance__ = object.__new__(cls)
        return cls.__instance__

    @classmethod
    def create(cls):
        registry = cls()
        registry.service_list = {}
        registry.functions_list = {}
        registry.initialising = True
        return registry

    def get(self, key):
        """

        :param key:
        :return: :raise KeyError:
        """
        if key in self.service_list:
            return self.service_list[key]
        else:
            if not self.initialising:
                raise KeyError('Service %s not found in list' % key)

    def register(self, key, reference):
        """

        :param key:
        :param reference:
        :raise KeyError:
        """
        if key in self.service_list:
            raise KeyError('Duplicate service exception %s' % key)
        else:
            self.service_list[key] = reference
