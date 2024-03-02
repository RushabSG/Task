from django.urls import path
from share_snippet.views import view_snippet, create_snippet

urlpatterns = [
    path('create', create_snippet, name='create_snippet'),
    path('<str:snippet_url>', view_snippet, name='view_snippet'),
]