from django.db import models
from apps.users.models import User

class TypeHousing(models.Model):
    type = models.CharField(max_length = 55, unique = True, null = False)

    class Meta:
        verbose_name = 'Type Housing'
        verbose_name_plural = 'Types housing'

    def __str__(self):
        return self.type



class Housing(models.Model):
    id = models.AutoField(primary_key = True)
    adress = models.CharField(max_length = 255, unique = True, blank = False, null = False) 
    phone_number = models.CharField(max_length = 55, blank = True, null = False)
    type = models.ForeignKey(TypeHousing, on_delete = models.CASCADE)
    description = models.TextField(max_length = 300, blank = True)
    
    
    class Meta:
        verbose_name = 'Housing'
    
    def __str__(self):
        return self.adress    