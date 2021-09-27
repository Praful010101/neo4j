from django.shortcuts import render

from django.http.response import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import logging
from rest_framework.response import Response

logger = logging.getLogger(__name__)

class TestNeo4jConnectionView(APIView):
    serializer_class = serializers.TestNeo4jConnectionSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=kwargs)
        serializer.is_valid(raise_exception=True)
        response = serializer.parse_get_request(kwargs)
        return Response(response, status=status.HTTP_200_OK)

class SymptomTemplate(APIView):
    serializer_class = serializers.SymptomTemplateSerializer
    
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=kwargs)
        serializer.is_valid(raise_exception=True)
        response = serializer.parse_get_request(kwargs)
        if response:
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(response, status=status.HTTP_404_NOT_FOUND)
