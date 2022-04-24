from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from etudiant_db.models.filiere import Filiere
from etudiant_db.serializers.filiere import FiliereSerializer


class FiliereList(APIView):

    def get(self, resquest):
        filieres = Filiere.objects.all()
        serializer = FiliereSerializer(filieres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        data = request.data
        serializer = FiliereSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class FiliereEdit(APIView):

    def get_object(self, id):
        try:
            return Filiere.objects.get(id = id)
        except Filiere.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def get(self, request ,id):
        filere = self.get_object(id)
        serializer = FiliereSerializer(filere)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self, request, id):
        filere = self.get_object(id)
        filere.delete()
        return Response(status=status.HTTP_200_OK)

    
    def put(self, request , id):
        filere = self.get_object(id)
        data = request.data
        serializer = FiliereSerializer(filere, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)