from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404


# Create your views here.
@api_view(['GET'])
def index(request):
    # return HttpResponse("Hello, World!")
    return Response(status=status.HTTP_200_OK)