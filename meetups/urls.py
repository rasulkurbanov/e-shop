from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:meetup_slug>/success', views.confirmation, name='confirmation'),
    path('<slug:meetup_slug>', views.details, name='meetup-detail')
] 
