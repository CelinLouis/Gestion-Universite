from rest_framework import serializers
from etudiant_db.models.type import Type


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = '__all__'