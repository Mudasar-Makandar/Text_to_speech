from django import forms
from .models import Tts

class BlogCommentsForm(forms.ModelForm):
    class Meta:
        model= Tts
        fields= ["text", "lang",]
