from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mosaicaapi.models import UserTileScore

class UserTileScoreView(ViewSet):

    def retrieve(self, request, pk):

        try:
            userTileScore = UserTileScore.objects.get(pk=pk)
            serializer = UserTileScoreserializer(userTileScore)
            return Response(serializer.data)
        except UserTileScore.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):

        userTileScores = UserTileScore.objects.all()
        user_query = request.query_params.get('user', None)
        if user_query is not None:
          userTileScores = userTileScores.filter(user=user_query)
        user_query2 = request.query_params.get('tile', None)
        if user_query2 is not None:
          userTileScores = userTileScores.filter(tile=user_query2)
        serializer = UserTileScoreserializer(userTileScores, many=True)
        return Response(serializer.data)

    def create(self, request):

        userTileScore = UserTileScore.objects.create(
            uid=request.data["uid"],
        )
        serializer = UserTileScoreserializer(userTileScore)
        return Response(serializer.data)

    def update(self, request, pk):

        userTileScore = UserTileScore.objects.get(pk=pk)

        userTileScore.score=request.data["score"]
        userTileScore.date=request.data[""]
        userTileScore.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        userTileScore = UserTileScore.objects.get(pk=pk)
        userTileScore.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)  

class UserTileScoreserializer(serializers.ModelSerializer):
    class Meta:
        model = UserTileScore
        fields = ('id', 'user', 'tile', 'score', 'date')
        depth = 1
