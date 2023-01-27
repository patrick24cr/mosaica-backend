from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mosaicaapi.models import Question, ResponseSet

class QuestionView(ViewSet):

    def list(self, request):
        questions = Question.objects.all()
        tile_query = request.query_params.get('tile', None)
        if tile_query is not None:
          questions = questions.filter(tile=tile_query)
        serializer = Questionserializer(questions, many=True)
        return Response(serializer.data)


class Questionserializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('english', 'spanish', 'aspect1', 'aspect2', 'aspect3', 'aspect4')
        depth = 1
