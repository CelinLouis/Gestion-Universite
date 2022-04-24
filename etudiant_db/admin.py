from django.contrib import admin
from etudiant_db.models.students import Etudiant
from etudiant_db.models.universite import Universite
from etudiant_db.models.type import Type
from etudiant_db.models.filiere import Filiere

# Register your models here.
admin.site.register(Etudiant)
admin.site.register(Universite)
admin.site.register(Type)
admin.site.register(Filiere)