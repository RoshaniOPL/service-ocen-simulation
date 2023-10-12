from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from django.core.files.storage import default_storage
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import time, os, json, pandas as pd,numpy as np, binascii, uuid
from datetime import datetime
from faker import Faker
import random


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class StoreResponse(APIView):

    def post(self, request):


        url_endpoint = request.data["url_endpoint"]
        response_rate = int(request.data["response_rate"])
        time_delay = int(request.data["time_delay"])
        total_records = int(request.data["total_records"])


        status_error_mapping = {(200, 201, 204): 0,
                        (400, 401, 403, 404, 500): -1,}
        
        data = []
        fake = Faker()
        # Generate records based on the mapping
        for status_codes, error_message in status_error_mapping.items():
            num_records = total_records // 2  # Equal distribution
            for _ in range(num_records):
                status_code = fake.random_element(elements=status_codes)
                data.append({
                    'response_rate':(response_rate*total_records)//100,
                    'time_delay':time_delay,
                    'traceId': fake.password(length=15, special_chars=False, digits=True, lower_case=True),
                    'status_code': status_code,
                    'Error_message': error_message,
                    # 'input_data' : request.data,
                    'transactionTimestamp': fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
                })

        # Shuffle the data to randomize the order
        random.shuffle(data)

        # df = pd.DataFrame(data)
        # time.sleep(10) ### for static delay
        return JsonResponse({
                             "url_endpoint": url_endpoint,
                             "response_rate":response_rate,
                             "time_delay": time_delay,
                             "total_records":total_records,
                             "input_data": data})
                                    


