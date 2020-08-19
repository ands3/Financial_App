from django.db import models

# Create your models here.
class GDP(models.Model):
    
    GDP_realtime_start = models.DateField()
    GDP_date = models.DateField()
    GDP_value = models.FloatField()
    
class GNP(models.Model):
    
    GNP_realtime_start = models.DateField()
    GNP_date = models.DateField()
    GNP_value = models.FloatField()