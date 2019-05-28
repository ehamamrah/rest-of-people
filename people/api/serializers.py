from rest_framework import serializers
from people.models import People

class PeopleSerializer(serializers.ModelSerializer):
  class Meta:
    model  = People
    fields = [
      'id',
      'name',
      'email',
      'country',
      'timestamp'
    ]