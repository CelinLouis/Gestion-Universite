from django.urls import path
from etudiant_db.api.universite import UniversiteList, UniversiteEdit

urlpatterns = [
    path('university/', UniversiteList.as_view()),
    path('university/<int:id>/', UniversiteEdit.as_view())
]