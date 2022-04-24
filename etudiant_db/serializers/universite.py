from rest_framework import serializers
from etudiant_db.models.universite import Universite


class UniversiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Universite
        fields = '__all__' 