from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializer import ImageLinkSerializer
import json

@csrf_exempt
def api(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ImageLinkSerializer(data=data)
        if serializer.is_valid():
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    return HttpResponse("Error", status=400)
