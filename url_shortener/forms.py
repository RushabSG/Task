from django.forms import ModelForm
from url_shortener.models import ShortUrlModel


class ShortUrlForm(ModelForm):
    class Meta:
        model = ShortUrlModel
        fields = ["original_url", "short_url"]
