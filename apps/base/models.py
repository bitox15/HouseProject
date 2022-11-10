from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    
    id = models.AutoField(primary_key = True)
    state = models.BooleanField('state', default = True)
    created_date = models.DateField('Created Date', auto_now = False,  auto_now_add = timezone.now())
    modified_date = models.DateField('Modified Date', auto_now = True, auto_now_add = False )
    deleted_date = models.DateField('Deleted Date', auto_now = True, auto_now_add = False )

    class Meta:
        abstract = True
        verbose_name = 'Base Model'
        verbose_name_plural = 'Base Models'
