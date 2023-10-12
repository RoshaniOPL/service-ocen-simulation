from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
import random
from datetime import datetime

class APISimulatorView(APIView):
    def post(self, request):
        """
        Handle the POST request for simulating API responses.
        Args:
            request: The HTTP request object containing data.
        Returns:
            Response: An JSON response containing simulated API responses.
        """

        try:
            data = request.data
            response_rate = int(data.get("response_rate", 0)) / 100  # Success rate
            no_of_simulation_response = int(data.get("no_of_simulation_response", 0))

            # Define a list of common HTTP status codes
            success_http_status_codes = [200, 201, 204]
            error_http_status_codes = [400, 401, 403, 404, 500]

            # Simulate API responses with random status codes
            simulated_status_codes = []
            success_responses_count = int(response_rate * no_of_simulation_response)
            
            for _ in range(no_of_simulation_response):
                if success_responses_count > 0:
                    status_code = random.choice(success_http_status_codes)
                    success_responses_count -= 1
                else:
                    status_code = random.choice(error_http_status_codes)
                simulated_status_codes.append(status_code)
            random.shuffle(simulated_status_codes)

            # Create a list of simulated responses
            simulated_response = []
            for i, status_code in enumerate(simulated_status_codes, 1):
                is_success = status_code in success_http_status_codes
                response = {
                    "status_code": status_code,
                    "error": 0 if is_success else -1,
                    "timestamp": datetime.now()
                }
                simulated_response.append(response)

            # Prepare the response data
            response_data = {
                "data": data,
                "response": simulated_response,
                "error": 0,
                "status": HTTP_200_OK
            }

            return Response(response_data, status=HTTP_200_OK)

        except Exception as e:
            error_response = {
                "data": None,
                "response": None,
                "error": str(e),
                "status": HTTP_400_BAD_REQUEST
            }
            return Response(error_response, status=HTTP_400_BAD_REQUEST)
