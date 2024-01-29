from django.db import models
from django.conf import settings


class CustomBaseModel(models.Model):
    """
    Abstract base class for models
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        object_name = self.__class__.__name__
        if hasattr(self, "name"):
            object_name = self.name
        return f"({self.id}) ({object_name})"

