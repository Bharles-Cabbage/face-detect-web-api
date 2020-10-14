from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializer import ImageLinkSerializer
import requests
import face_recognition
import PIL.Image
import numpy as np


@csrf_exempt
@api_view(['POST'])
def api(request):
    # Declare file variable 
    file = None

    #check if image was uploaded
    if 'file' in request.data:
        file = request.data['file']

    else:    
        data = JSONParser().parse(request)
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


    # return JsonResponse({'err': 'Bad Request. Only accepting POST requests.'}, status=400)
