from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mosaicaapi.models import User

class UserView(ViewSet):

    def retrieve(self, request, pk):

        try:
            user = User.objects.get(pk=pk)
            serializer = Userserializer(user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):

        users = User.objects.all()
        uid_query = request.query_params.get('uid', None)
        if uid_query is not None:
          users = users.filter(uid=uid_query)
        serializer = Userserializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):

        user = User.objects.create(
            uid=request.data["uid"],
        )
        serializer = Userserializer(user)
        return Response(serializer.data)

    def update(self, request, pk):

        user = User.objects.get(pk=pk)

        user.uid=request.data["uid"]
        user.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)  

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'uid')
        depth = 1
