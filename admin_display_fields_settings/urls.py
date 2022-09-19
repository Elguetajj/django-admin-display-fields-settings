from django.urls import path
from .ajax import changeFormHandler


urlpatterns = [
    path('change_form/', changeFormHandler, name='changeFormHandler'),
]