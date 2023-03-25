from django.urls import path
from .views import home, getPrompt, PromptView

urlpatterns = [
    path('', home),
    path('prompt/', getPrompt),
    path('prompts/', PromptView.as_view())
]
