from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from vuenote.models import Note
from vuenote.serializers import NoteSerializer


class NoteView(APIView):
    @staticmethod
    def post(request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return HttpResponse("good")

    @staticmethod
    def get(request):
        info = Note.objects.all()
        serializer = NoteSerializer(info, many=True)
        return JsonResponse(serializer.data, safe=False)

    @staticmethod
    def delete(request):
        serializer = NoteSerializer(data=request.data)
        print(serializer)
        print(request.data)
        return HttpResponse("delete")
