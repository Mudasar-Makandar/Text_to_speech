from rest_framework import serializers
from .models import Tts

class TtsSerializer(serializers.Serializer):
    text = serializers.CharField(read_only=True)
    lang = serializers.CharField(required=False)
