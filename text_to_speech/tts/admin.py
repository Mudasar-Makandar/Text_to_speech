from django.contrib import admin
from .models import Tts
# Register your models here.

class TtsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tts, TtsAdmin)
