from django.urls import path
from etudiant_db.api.filiere import FiliereList, FiliereEdit

urlpatterns = [
    path('filieres/',FiliereList.as_view()),
    path('filieres/<int:id>', FiliereEdit.as_view())
    ]