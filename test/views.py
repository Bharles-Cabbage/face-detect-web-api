from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializer import ImageLinkSerializer
import requests

api_key = 'rbwdAiYs2GrgTwmmKywElHeZzvZGe84c'
api_secret = 'x6NGRRKuk-Zci1eezK8rGGESSaMjpExm'
@csrf_exempt
def api(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ImageLinkSerializer(data=data)

        if serializer.is_valid():

            data = serializer.data
            pload = {'api_key': api_key, 'api_secret': api_secret, 'image_url': data['url'], 'return_attributes': 'gender,age'}
            r = requests.post('https://api-us.faceplusplus.com/facepp/v3/detect', data=pload)
                        
            return JsonResponse(r.json(), status=200)

        return JsonResponse(serializer.errors, status=400)

    return HttpResponse("Error", status=400)
