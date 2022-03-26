import json
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(["GET"])
def test_home_api(request):
    return Response(data=json.dumps({"aa":"bb"}))


def test_home(request):
    return HttpResponse("home page")