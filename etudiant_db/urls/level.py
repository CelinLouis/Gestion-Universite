from django.urls import path
from etudiant_db.api.level import LevelList

urlpatterns = [
    path('levels/', LevelList.as_view()),
    ]