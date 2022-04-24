from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from etudiant_db.models.level import Niveau
from etudiant_db.serializers.level import NiveauSerializer

class LevelList(APIView):

    def get(self, request):
        niveaux = Niveau.objects.all().order_by('-date_created')
        serializer = NiveauSerializer(niveaux, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        data= request.data
        serializer = NiveauSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class LevelEdit(APIView):

    def get_object(self, id):
        try:
            return Niveau.objects.get(id=id)
        except Niveau.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def get(self, request, id):
        niveau = self.get_object(id)
        serializer = NiveauSerializer(niveau)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self, request, id):
        niveau = self.get_object(id)
        niveau.delete()
        return Response(status=status.HTTP_200_OK)


    def put(self, request, id):
        data = request.data
        niveau = self.get_object(id)
        serializer =  NiveauSerializer(niveau, data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)