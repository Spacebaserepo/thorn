"""Dispatcher doing nothing."""


from . import base

__all__ = ['Dispatcher']


class Dispatcher(base.Dispatcher):

    def send(self, *args, **kwargs):
        pass
