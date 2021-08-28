from django.shortcuts import render
from rest_framework import generics
from api.models import Tags_info
from api.serializers import TagsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import *
import uuid


class GetResults(APIView):
    serializer_class = TagsSerializer

    def get(self, request):
        task_id = self.request.query_params.get("id")
        info = Tags_info.objects.get(task_id=task_id)
        return Response(info.info, status=200)


class ScanUrl(APIView):
    def get(self, request):
        url = self.request.query_params.get("url")
        task_id = str(uuid.uuid4())
        url_parse.delay(url, task_id)
        return Response({'task_id': task_id}, status=200)
