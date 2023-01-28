from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mosaicaapi.models import BadQuestionReport, User, Question

class BadQuestionReportView(ViewSet):
    
    def list(self, request):

        reports = BadQuestionReport.objects.all()
        serializer = BadQuestionReportserializer(reports, many=True)
        return Response(serializer.data)

    def create(self, request):
        category = ""
        if (request.data["problemWithEnglish"] == True and request.data["problemWithSpanish"] == True):
            category = 'english and spanish'
        if (request.data["problemWithEnglish"] == True and request.data["problemWithSpanish"] == False):
            category = 'english'
        if (request.data["problemWithEnglish"] == False and request.data["problemWithSpanish"] == True):
            category = 'spanish'
        if (request.data["problemWithEnglish"] == False and request.data["problemWithSpanish"] == False):
            category = 'neither'
        report = BadQuestionReport.objects.create(
            user=User.objects.get(pk=request.data["user"]),
            question=Question.objects.get(pk=request.data["question"]),
            userDescription=request.data["problemDescription"],
            problemCategory=category,
        )
        serializer = BadQuestionReportserializer(report)
        return Response(serializer.data)


class BadQuestionReportserializer(serializers.ModelSerializer):
    class Meta:
        model = BadQuestionReport
        fields = ('user', 'question', 'userDescription', 'problemCategory')
        depth = 2
