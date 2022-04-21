from etudiant_db.models.students import Etudiant
from etudiant_db.serializers.students import EtudiantSerializer, EtudiantPostSerializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

class StudentsList(APIView):

    def get(self, request):
        students = Etudiant.objects.all().order_by('-date_ajoute')
        serializer = EtudiantSerializer(students, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    
    def post(self, request):
        data = request.data
        serializer = EtudiantPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class StudentsEdit(APIView):

    def get_object(self, id):
        try:
            return Etudiant.objects.get(id=id)
        except Etudiant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def get(self, request, id):
        etudiant = self.get_object(id)
        serializer = EtudiantSerializer(etudiant)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self, request, id):
        etudiant = self.get_object(id)
        etudiant.delete()
        return Response(status=status.HTTP_200_OK)


    def put(self, request, id):
        etudiant = self.get_object(id)
        data=request.data
        serializer = EtudiantPostSerializer(etudiant, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)