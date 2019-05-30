from rest_framework import generics
from people.models import People
from .serializers import PeopleSerializer
from rest_framework.response import Response
import json

class PeopleList(generics.ListAPIView):
  serializer_class = PeopleSerializer

  def list(self, request):
    queryset   = People.people_list_generator()
    serializer = PeopleSerializer(queryset, many=True)
    content = {
      'message': 'success',
      'data':    serializer.data
    }
    return Response(content)