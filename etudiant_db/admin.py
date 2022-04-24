from django.contrib import admin
from etudiant_db.models.students import Etudiant
from etudiant_db.models.universite import Universite
from etudiant_db.models.type import Type
from etudiant_db.models.filiere import Filiere
from etudiant_db.models.level import Niveau

# Register your models here.
admin.site.register(Etudiant)
admin.site.register(Universite)
admin.site.register(Type)
admin.site.register(Filiere)
admin.site.register(Niveau)