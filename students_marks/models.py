
from django.db import models
from django.db.models.fields import FloatField,CharField,DateTimeField,AutoField
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length = 20)
    Id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length =20)
    marks = models.FloatField()
    def __str__(self):
        return self.name