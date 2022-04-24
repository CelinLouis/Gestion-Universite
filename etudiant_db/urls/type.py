from django.urls import path
from etudiant_db.api.type import TypeList, TypeEdit


urlparterns = [
    path('types/', TypeList.as_view()),
    path('types/<int:id>/', TypeEdit.as_view())
]