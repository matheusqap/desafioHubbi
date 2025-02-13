from uuid import uuid4
from django.db import models
from behaviors.behaviors import Timestamped
from django_lifecycle import LifecycleModelMixin

class BaseModel(LifecycleModelMixin, Timestamped):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    objects = models.Manager()

    class Meta:
        abstract = True