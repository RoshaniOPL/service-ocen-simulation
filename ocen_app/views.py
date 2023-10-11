from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from django.core.files.storage import default_storage
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import time, os, json, pandas as pd, binascii, uuid
from datetime import datetime

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class StoreResponse(APIView):

    def post(self, request):

        url_endpoint = request.data["url_endpoint"]
        print(request.data["response_rate"])
        response_rate = int(request.data["response_rate"])
        
        time_delay = int(request.data["time_delay"])
        # time.sleep(10) ### for static delay
        return JsonResponse({"status_code": 200,
                             "error_msg": "Success",
                             "url_endpoint": url_endpoint,
                             "response_rate":response_rate,
                             "time_delay": time_delay,
                             "ack": {
                                    "error": "0",
                                    "traceId": "",
                                    "timestamp": "timestamp"}})
                                    


