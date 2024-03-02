from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from share_snippet.forms import SnippetForm
from share_snippet.models import TextSnippetModel
import hashlib
# Create your views here.

def create_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save()
            return redirect('view_snippet', snippet_url=snippet.url)
    else:
        form = SnippetForm()
    return render(request, 'create_snippet.html', {'form': form})

def view_snippet(request, snippet_url):
    snippet = get_object_or_404(TextSnippetModel, url=snippet_url)
    secret_key = request.GET.get('secret_key')
    if secret_key == snippet.secret_key:
        content = snippet.text
    else:
        content = "This snippet is encrypted. Please provide the correct key to decrypt."
    return render(request, 'view_snippet.html', {'snippet': snippet, 'content': content})
