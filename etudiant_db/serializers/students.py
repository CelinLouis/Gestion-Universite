from rest_framework import serializers
from etudiant_db.models.students import Etudiant


class EtudiantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Etudiant
        fields = '__all__'


class EtudiantPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Etudiant
        fields = ('id','nom','prenom','date_naissance','lieu_naissance','adresse','contact')