from rest_framework.decorators import api_view,parser_classes
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import requests
import face_recognition
import PIL.Image
import numpy as np

from .serializer import ImageLinkSerializer


@csrf_exempt
@api_view(['POST'])
def api(request):
    # Declare file variable 
    file = None
    data = JSONParser().parse(request)

    #check if image was uploaded
    if 'file' in list(request.data):
        file = data['file']

    else:    
        serializer = ImageLinkSerializer(data=data)

        if serializer.is_valid():
            data = serializer.data
            file = requests.get(data['image_url'], stream=True).raw     # Get image from URL
        else:
            return JsonResponse(serializer.errors, status=400)

    # Convert Image file into Numpy Array
    im = PIL.Image.open(file)
    image = np.array(im)

    # Detect locations of face.
    face_locations = face_recognition.face_locations(image)
    response = {'face_locations': face_locations}

    return JsonResponse(response, status=200)
