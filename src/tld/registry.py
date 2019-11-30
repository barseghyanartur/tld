__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2019 Artur Barseghyan'
__license__ = 'MPL-1.1 OR GPL-2.0-only OR LGPL-2.0-or-later'
__all__ = (
    'Registry',
    'REGISTRY',
)


class Registry(type):

    registry = {}

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)
        # Here the name of the class is used as key but it could be any class
        # parameter.
        if getattr(new_cls, '_uid', None):
            cls.registry[new_cls._uid] = new_cls
        return new_cls

    @property
    def _uid(cls):
        return getattr(cls, 'uid', cls.__name__)

    @classmethod
    def get_registry(cls):
        return dict(cls.registry)


REGISTRY = Registry.registry
