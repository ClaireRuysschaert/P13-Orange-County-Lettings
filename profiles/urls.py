from django.contrib import admin
from django.urls import path

from oc_lettings_site import views

app_name = "profiles"

urlpatterns = [
    path("", views.profiles_index, name="profiles_index"),
    path("<int:profile_id>/", views.profile, name="profile"),
]
