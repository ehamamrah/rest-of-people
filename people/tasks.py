from celery import shared_task
import json

@shared_task
def read_json_file_details():
    with open('people.json', 'r') as file:
      list = json.load(file)
    return list['data']

@shared_task
def get_people_list_from_json_file():
  from people.models import People
  list = read_json_file_details()
  records = []
  for record in list:
    records += [
      People(name = record[1], email = record[2], country = record[3])
    ]
  People.objects.bulk_create(records)
  return People.objects.all()