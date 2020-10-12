from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializer import ImageLinkSerializer
import requests
import face_recognition
import PIL.Image
import numpy as np
# api_key = '9jOgLRpjTeROSeGfVFmjSNTH4Aj9cE81'
# api_secret = 'U1Ctbr3CijFS5NfLFJxYX0cRym0RF7m6'

@csrf_exempt
def api(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ImageLinkSerializer(data=data)

        if serializer.is_valid():

            data = serializer.data
            # pload = {'api_key': api_key, 'api_secret': api_secret, 'image_url': data['image_url'], 'return_attributes': 'gender,age'}
            # r = requests.post('https://api-us.faceplusplus.com/facepp/v3/detect', data=pload)

            file = requests.get(data['image_url'], stream=True).raw
            im = PIL.Image.open(file)
            image = np.array(im)
            face_locations = face_recognition.face_locations(image)

            response = {'face_locations': face_locations}

            return JsonResponse(response, status=200)

        return JsonResponse(serializer.errors, status=400)

    return HttpResponse("Error", status=400)
