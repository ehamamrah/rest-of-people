from django.conf.urls import url
from .views import PeopleList

app_name = 'people_api'

urlpatterns = [
  url(r'^$', PeopleList.as_view(), name = 'people_list')
]