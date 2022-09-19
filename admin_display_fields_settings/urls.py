from django.urls import path
from django.conf.urls import patterns
from .ajax import changeFormHandler


urlpatterns = patterns('',
    path('change_form/', changeFormHandler, name='changeFormHandler'),
)