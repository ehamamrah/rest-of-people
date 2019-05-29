from rest_framework import generics
from people.models import People
from .serializers import PeopleSerializer
from .tasks import get_people_list_from_json_file, read_json_file_details
import json

class PeopleList(generics.ListAPIView):
  serializer_class = PeopleSerializer

  def get_queryset(self):
    list_of_people_from_json = read_json_file_details()

    if len(People.objects.all()) < len(list_of_people_from_json):
      get_people_list_from_json_file()

    return People.objects.all()