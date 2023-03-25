from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .gpt import gpt3_completion, trial
from .models import Prompt
from .serializers import PromptSerializer
# Create your views here.


def home(request):
    return render(request, 'chat/chat.html')


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def getPrompt(request):
    data = request.data

    if not data:
        return Response("no data was sent", status=status.HTTP_400_BAD_REQUEST)

    print(data)
    try:
        prompt = Prompt.objects.get(owner=request.user)
    except Prompt.DoesNotExist:
        prompt = Prompt()

    # prompt.text += ''

    # response = gpt3_completion(data)
    response = ""

    return Response(response, status=status.HTTP_200_OK)


class PromptView(generics.ListAPIView):
    serializer_class = PromptSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Prompt.objects.filter(owner=self.request.user)
