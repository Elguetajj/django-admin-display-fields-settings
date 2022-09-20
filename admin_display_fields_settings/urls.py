from django.urls import path
from .ajax import changeFormHandler

app_name = "admin_display_fields_settings"

urlpatterns = [
    path('change_form/', changeFormHandler, name='changeFormHandler'),
]