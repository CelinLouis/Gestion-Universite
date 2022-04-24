from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from etudiant_db.models.type import Type
from etudiant_db.serializers.type import TypeSerializer


class TypeList(APIView):

    def get(self, request):
        types = Type.objects.all().order_by()
        serializer = TypeSerializer(types, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        data = request.data
        serializer = TypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class TypeEdit(APIView):

    def get_object(self, id):
        try:
            return Type.objects.get(id=id)
        except Type.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def get(self, request, id):
        type = self.get_object(id)
        serializer = TypeSerializer(type)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self, request, id):
        type= self.get_object(id)
        type.delete()
        return Response(status=status.HTTP_200_OK)


    def put(self, request, id):
        type = self.get_object(id)
        data = request.data
        serializer = TypeSerializer(type, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST) 