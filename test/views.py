from rest_framework.decorators import api_view,parser_classes
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import requests
import face_recognition
import PIL.Image
import numpy as np

from .serializer import ImageLinkSerializer, ImageUploadSerializer


@csrf_exempt
@api_view(['POST', 'PUT'])
def api(request):
    # Declare file variable 
    file = None
    
    if request.method == "POST":
        # Handle Image Uploaded
        serializer = ImageUploadSerializer(request.data, many=True)
        return JsonResponse(serializer.data['ext'], status=400)

    elif request.method == "PUT":

        serializer = ImageLinkSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.data
            file = requests.get(data['image_url'], stream=True).raw     # Get image from URL
            # return JsonResponse(data, status=400)
        else:
            return JsonResponse(serializer.errors, status=400)



    # Convert Image file into Numpy Array
    im = PIL.Image.open(file)
    image = np.array(im)

    # Detect locations of face.
    face_locations = face_recognition.face_locations(image)
    response = {'face_locations': face_locations}

    return JsonResponse(response, status=200)
