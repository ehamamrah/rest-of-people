from rest_framework import generics
from people.models import People
from .serializers import PeopleSerializer
from .tasks import get_people_list_from_json_file, read_json_file_details
from rest_framework.response import Response
import json

class PeopleList(generics.ListAPIView):
  serializer_class = PeopleSerializer

  def list(self, request):
    queryset   = PeopleList.__people_list_generator()
    serializer = PeopleSerializer(queryset, many=True)
    content = {
      'message': 'success',
      'data':    serializer.data
    }
    return Response(content)

  @classmethod
  def __people_list_generator(cls):
    list_of_people_from_json = read_json_file_details()

    if len(People.objects.all()) < len(list_of_people_from_json):
      get_people_list_from_json_file()

    return People.objects.all()