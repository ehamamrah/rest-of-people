from django.db import models

# Create your models here.
class People(models.Model):
  name    = models.CharField('Full Name', max_length = 100, null = False, blank = False)
  email   = models.CharField('Email', max_length = 100, null = False, blank = False)
  country = models.CharField('Country', max_length = 100)

  def __str__(self):
    return self.name