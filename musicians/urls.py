from django.urls import path
from musicians.views import MusicianView
# from .views import MusicianView


urlpatterns = [
    path("musicians/", MusicianView.as_view()),
]
