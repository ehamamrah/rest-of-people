from django.db import models

class People(models.Model):
  name      = models.CharField(max_length = 100, null = False, blank = False)
  email     = models.CharField(max_length = 100, null = False, blank = False, unique = True)
  country   = models.CharField(max_length = 100)
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

  @classmethod
  def people_list_generator(cls):
    from .tasks import get_people_list_from_json_file, read_json_file_details
    list_of_people_from_json = read_json_file_details()

    if len(People.objects.all()) < len(list_of_people_from_json):
      get_people_list_from_json_file()

    return People.objects.all()