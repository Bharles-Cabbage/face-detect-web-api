from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializer import ImageLinkSerializer
import requests
import face_recognition
import PIL.Image
import numpy as np


@csrf_exempt
def api(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ImageLinkSerializer(data=data)

        if serializer.is_valid():
            data = serializer.data

            # Search for Face Locations
            file = requests.get(data['image_url'], stream=True).raw
            im = PIL.Image.open(file)
            image = np.array(im)

            face_locations = face_recognition.face_locations(image)
            response = {'face_locations': face_locations}

            return JsonResponse(response, status=200)

        return JsonResponse(serializer.errors, status=400)

    return JsonResponse({'err': 'Bad Request. Only accepting POST requests.'}, status=400)
