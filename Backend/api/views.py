from django.shortcuts import render
from rest_framework import generics
from api.models import Tags_info
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import *
import uuid
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError



class GetResults(APIView):

    def get(self, request):
        task_id = self.request.query_params.get("id")
        try:
            uuid.UUID(task_id, version=4)
        except ValueError as e:
            return Response({'error: Invalid request'}, status=400)
        info = Tags_info.objects.get(task_id=task_id)
        return Response(info.info, status=200)


class ScanUrl(APIView):
    def get(self, request):
        url = self.request.query_params.get("url")
        validate = URLValidator()
        try:
            validate(url)
        except ValidationError as e:
            return Response({'error: Invalid request'}, status=400)
        task_id = str(uuid.uuid4())
        url_parse.delay(url, task_id)
        return Response({'task_id': task_id}, status=200)
