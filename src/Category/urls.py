from django.conf.urls import url
from . import views



app_name='Category'

urlpatterns = [
    url(r'^$', views.all_categories, name='all_categories'),
    url(r'^(?P<id>\d+)$', views.category, name='category'),
]
 