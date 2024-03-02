from django import forms
from share_snippet.models import TextSnippetModel

class SnippetForm(forms.ModelForm):
    class Meta:
        model = TextSnippetModel
        fields = ['text', 'secret_key']
