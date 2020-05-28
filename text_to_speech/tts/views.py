from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import FileResponse
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from gtts import gTTS
from io import BytesIO
import os
from django.conf import settings
from django.shortcuts import render
from django.templatetags.static import static
from .serializers import TtsSerializer

@api_view(["POST", "GET"])
def IdealWeight(request):

    try:
        if request.method == "GET":
        #height=json.loads(heightdata.body)

        #weight=str(height*10)
            weight="HIIIIII"

            return Response("Ideal weight should be:"+weight+" kg")

        elif request.method == "POST":
            return_data = gTTS(text=request.data["text"], lang='en')
            serializer = TtsSerializer(data=request.data)
            if serializer.is_valid():
                return Response(return_data.get_urls(), status=status.HTTP_201_CREATED)
            #return Response(return_data.get_urls())

    except ValueError as e:

        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

from .models import Tts
def home(request):
    mytext="Hi i am here"
    return_data = gTTS(text=mytext, lang='en')
    tts = Tts.objects.get(id=4)
    path = settings.MEDIA_ROOT
    audio_list = os.listdir(path + '/')
    context = {'audio_url':settings.MEDIA_URL,'audio' : audio_list}

    return render(request, 'home.html', context)

from django.shortcuts import render
from .forms import BlogCommentsForm

def home(request):
    form= BlogCommentsForm(request.POST or None)
    if form.is_valid():
        form.save()

    context= {'form': form,'audio_url':settings.MEDIA_URL }

    return render(request, 'home.html', context)
