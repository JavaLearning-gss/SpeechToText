# from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from aip import AipSpeech

# Create your views here.

CHINA_CODE = ['CHN', 'HKG', 'TWN', 'MAC']
CHINA_LANG = ['CHM', 'CHT']

@csrf_exempt
def index(request):

    if request.method == "POST":

        lang = request.POST.get('lang')
        countryCode = request.POST.get('countryCode')
        SENT_DICT = {'dev_pid': 1536, }

        # NEW_LOGIC
        if lang:
            if lang in CHINA_LANG:
                if countryCode == "HKG":
                    SENT_DICT['dev_pid'] = 1637
                else:
                    SENT_DICT['dev_pid'] = 1537
            else:
                SENT_DICT['dev_pid'] = 1737

        # """ 你的 APPID AK SK """
        APP_ID = '16710665'
        API_KEY = 'lAm7pwiagTIHIqksaTRQILnL'
        SECRET_KEY = 'w4KIhKEKrmiNq4kBtD7Cu0hVjXgO2b1N'

        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

        return_file = client.asr(
            request.FILES['audioData'].read(), 'wav', 16000, SENT_DICT)

        print(return_file) 

        return HttpResponse(return_file.get('result'))

    # else:
    #     template = get_template('demo.html')
    #     html = template.render(locals())
    #     return HttpResponse(html)
