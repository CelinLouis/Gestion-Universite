from django.urls import path
from etudiant_db.api.students import StudentsList, StudentsEdit

urlpatterns = [
    path('studentes/', StudentsList.as_view()),
    path('studentes/<int:id>/', StudentsEdit.as_view()),
]