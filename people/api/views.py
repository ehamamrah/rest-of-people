from rest_framework import generics
from people.models import People
from .serializers import PeopleSerializer

class PeopleList(generics.ListAPIView):
  serializer_class = PeopleSerializer

  def get_queryset(self):
    return People.objects.all()