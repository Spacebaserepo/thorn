from django.db import models


class ChoicesCharField(models.CharField):
    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        try:
            del kwargs['choices']
        except KeyError:
            pass
        return name, path, args, kwargs
