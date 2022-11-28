from django.db import models
from apps.base.models import BaseModel
from apps.state.models import StateUbication

class CityUbication(BaseModel):
    name = models.CharField(max_length=255, blank=False, null=True)
    state = models.ForeignKey(StateUbication, on_delete = models.CASCADE)


    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name

    