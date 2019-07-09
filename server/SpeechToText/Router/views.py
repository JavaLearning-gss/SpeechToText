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

data = str()
count = 0
@csrf_exempt
def index(request):
    global count, data
    count += 1
    # print(count)
    if request.method == "POST":
        print(request.FILES.get("audioData", None))
        print(type(request.FILES['audioData']))

        default_storage.save('audio/' + '123' + '.wav', ContentFile(request.FILES['audioData'].read()))

        # """ 你的 APPID AK SK """
        # APP_ID = '16710665'
        # API_KEY = 'lAm7pwiagTIHIqksaTRQILnL'
        # SECRET_KEY = 'w4KIhKEKrmiNq4kBtD7Cu0hVjXgO2b1N'

        # client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

        # return_file = client.asr(request.FILES.get("audioData", None).read(), 'wav', 16000, {
        #     'dev_pid': 1536,
        # })
        # print(return_file)
        return HttpResponse('POST')
    else:
        return HttpResponse('GET')
        # print(request.method)
        # audio_file=open(r'../../demo1.wav','rb').read()
        # print(audio_file)
        # Blob = request.FILES['audioData'].read()

        # f=wave.open(r'../../demo.wav','wb')

        # f.setnchannels(1)
        # f.setsampwidth(2)
        # f.setframerate(16000)
        # f.writeframes(Blob)
        # f.close()

        # audio_file=open(r'../../demo.wav','rb').read()

    #     """ 你的 APPID AK SK """
    #     APP_ID = '16710665'
    #     API_KEY = 'lAm7pwiagTIHIqksaTRQILnL'
    #     SECRET_KEY = 'w4KIhKEKrmiNq4kBtD7Cu0hVjXgO2b1N'

    #     client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    #     return_file = client.asr(audio_file, 'wav', 16000, {
    #         'dev_pid': 1536,
    #     })
    #     f.close()
    #     # global data
    #     print(return_file)
    #     if return_file['err_no']==0:
    #         data=return_file['result']
    #         print(data)
    #         return HttpResponse(data)
    #     else:
    #         return HttpResponse('error')
    # else:
    #     # global data
    #     print(data)
    #     if len(data)>0:
    #         return HttpResponse(data)
    #     return HttpResponse('error')
    # return HttpResponse('ok')
