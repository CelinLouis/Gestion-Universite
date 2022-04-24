from rest_framework import serializers
from etudiant_db.models.filiere import Filiere


class FiliereSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filiere
        fields = '__all__'