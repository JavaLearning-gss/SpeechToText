# from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import base64
from aip import AipSpeech
import wave
import numpy as np
import scipy.signal as signal

# Create your views here.


@csrf_exempt
def index(request):

    if request.method == "POST":

        """ 你的 APPID AK SK """
        APP_ID = '16710665'
        API_KEY = 'lAm7pwiagTIHIqksaTRQILnL'
        SECRET_KEY = 'w4KIhKEKrmiNq4kBtD7Cu0hVjXgO2b1N'

        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

        return_file = client.asr(request.FILES['audioData'].read(), 'wav', 16000, {
            'dev_pid': 1536,
        })

        return HttpResponse(return_file.get('result'))

