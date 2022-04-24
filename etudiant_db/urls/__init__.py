from etudiant_db.urls.students import urlpatterns as StudentUrls
from etudiant_db.urls.universite import urlpatterns as UniverstUrls
from etudiant_db.urls.type import urlparterns as TypeUrls
from etudiant_db.urls.filiere import urlpatterns as FiliereUrls

urlpatterns = StudentUrls + UniverstUrls + TypeUrls + FiliereUrls