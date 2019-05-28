from djangotasks import task
import json
from people.models import People

@task
def get_people_list_from_json_file():
  with open('people.json', 'r') as file:
    list = json.load(file)
  for record in list['data']:
    person = People(name = record[1], email = record[2], country = record[3])
    person.save()