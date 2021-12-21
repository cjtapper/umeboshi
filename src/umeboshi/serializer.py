import pickle
from importlib import import_module

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class DefaultSerializer:
    def dumps(self, value):
        return pickle.dumps(value)

    def loads(self, value):
        return pickle.loads(value)


def load_class(path):
    """
    Loads class from path.
    """

    mod_name, klass_name = path.rsplit(".", 1)

    try:
        mod = import_module(mod_name)
    except AttributeError as e:
        raise ImproperlyConfigured(f'Error importing {mod_name}: "{e}"')

    try:
        klass = getattr(mod, klass_name)
    except AttributeError:
        raise ImproperlyConfigured(
            f'Module "{mod_name}" does not define a "{klass_name}" class'
        )

    if not hasattr(klass, "loads"):
        raise ImproperlyConfigured(
            f'Class "{klass_name}" does not define "loads" method'
        )

    if not hasattr(klass, "dumps"):
        raise ImproperlyConfigured(
            f'Class "{klass_name}" does not define "dumps" method'
        )

    return klass


def load_serializer(settings):

    if hasattr(settings, "UMEBOSHI_SERIALIZER"):
        return load_class(settings.UMEBOSHI_SERIALIZER)()
    else:
        return DefaultSerializer()


serializer = load_serializer(settings)
