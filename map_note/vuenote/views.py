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
    def post(request):  # post request를 처리하는 함수
        serializer = NoteSerializer(data=request.data)  # 받아온 데이터를 serializer에 저장
        if serializer.is_valid():
            serializer.save()   # 데이터베이스에 저장
        return HttpResponse("save")

    @staticmethod
    def get(request):   # get request를 처리하는 함수
        info = Note.objects.all()   # 가지고있는 모든 데이터를 데이터베이스에서 불러와 info에 저장
        serializer = NoteSerializer(info, many=True)    # serializer로 만든다
        return JsonResponse(serializer.data, safe=False)    # Json 포맷으로 으로 response

    @staticmethod
    def delete(request):    # delete request를 처리하는 함수
        deletemodel = request.data  # 받아온 데이터를 deletemodel 에 저장한다
        d_memo = str(deletemodel['memo'])
        d_latitudes = float(deletemodel['latitudes'])
        d_longitudes = float(deletemodel['longitudes'])
        queryset = Note.objects.filter(memo=d_memo, latitudes=d_latitudes, longitudes=d_longitudes)   # 테이블에서 필터를 통해 조회한후 queryset에 저장
        queryset.delete()   # 해당 데이터를 데이터베이스에서 삭제

        return HttpResponse("delete")
