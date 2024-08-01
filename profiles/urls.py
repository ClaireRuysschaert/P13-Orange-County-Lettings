from django.urls import path

from profiles import views

app_name = "profiles"

urlpatterns = [
    path("", views.index, name="profiles_index"),
    path("<int:profile_id>/", views.profile, name="profile"),
]
