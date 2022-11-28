from django.db import models
from apps.base.models import BaseModel

class StateUbication(BaseModel):
    name = models.CharField(max_length=255, blank=False,null=True)

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'

    def __str__(self):
        return self.name
