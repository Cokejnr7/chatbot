from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .gpt import gpt3_completion
# Create your views here.


def home(request):
    return render(request, 'chat/chat.html')


@api_view(['POST'])
def getPrompt(request):
    data = request.data
    if not data:
        return Response("no data was sent", status=status.HTTP_400_BAD_REQUEST)

    response = gpt3_completion(data)

    return Response(response, status=status.HTTP_200_OK)
