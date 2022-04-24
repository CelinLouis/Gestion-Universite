from numpy import True_
from etudiant_db.models.universite import Universite
from etudiant_db.serializers.universite import UniversiteSerializer
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response


class UniversiteList(APIView):

    def get(self, request):
        universite = Universite.objects.all().order_by('-date_created')
        serializer = UniversiteSerializer(universite, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        data = request.data
        serializer = UniversiteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UniversiteEdit(APIView):

    def get_object(self, id):
        try:
            return Universite.objects.get(id=id)
        except Universite.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def get(self, request, id):
        universite = self.get_object(id)
        serializer = UniversiteSerializer(universite)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self, request, id):
        universite = self.get_object(id)
        universite.delete()
        return Response(status=status.HTTP_200_OK)


    def put(self, request, id):
        universite = self.get_object(id)
        data = request.data
        serializer = UniversiteSerializer(universite,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)