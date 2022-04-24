from rest_framework import serializers
from etudiant_db.models.level import Niveau


class NiveauSerializer(serializers.ModelSerializer):

    class Meta:
        model = Niveau
        fields = '__all__'